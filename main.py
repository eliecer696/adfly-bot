from __future__ import print_function
import re
import psutil
import requests
from os import _exit,path,devnull
from sys import stdout
from time import sleep
from random import choice
from colorama import Fore
from argparse import ArgumentParser
from traceback import format_exc,print_exc
from threading import Thread,Lock
from user_agent import generate_user_agent
from selenium import webdriver
from selenium.common.exceptions import *

def exit(exit_code):
	global drivers
	if exit_code==1:
		print_exc()
	try:drivers
	except NameError:pass
	else:
		for driver in drivers:
			try:psutil.Process(driver).terminate()
			except:pass
	_exit(exit_code)
def print(message):
	if message.startswith('[ERROR]'):
		colour=Fore.RED
	elif message.startswith('[WARNING]'):
		colour=Fore.YELLOW
	elif message.startswith('[INFO]'):
		colour=Fore.GREEN
	else:
		colour=Fore.RESET
	stdout.write('%s%s%s\n'%(colour,message,Fore.RESET))
def get_proxies():
	global args
	if args.proxies:
		proxies=open(args.proxies,'r').read().strip().split('\n')
	else:
		proxies=requests.get('https://www.proxy-list.download/api/v1/get?type=https&anon=elite').content.decode().strip().split('\r\n')
	print('[INFO][0] %d proxies successfully loaded!'%len(proxies))
	return proxies
def bot(id):
	global locks,urls,user_agents,proxies
	while True:
		try:
			url=choice(urls)
			with locks[0]:
				if len(proxies)==0:
					proxies.extend(get_proxies())
				proxy=choice(proxies)
				proxies.remove(proxy)
			print('[INFO][%d] Connecting to %s'%(id,proxy))
			user_agent=choice(user_agents) if args.user_agent else user_agents()
			print('[INFO][%d] Setting user agent to %s'%(id,user_agent))
			try:
				if args.slow_start:
					locks[1].acquire()
				if args.driver=='chrome':
					chrome_options=webdriver.ChromeOptions()
					chrome_options.add_argument('--proxy-server={}'.format(proxy))
					chrome_options.add_argument('--user-agent={}'.format(user_agent))
					chrome_options.add_argument('--mute-audio')
					if args.headless:
						chrome_options.add_argument('--headless')
					driver=webdriver.Chrome(options=chrome_options)
				else:
					firefox_options=webdriver.FirefoxOptions()
					firefox_options.preferences.update({
						'media.volume_scale':'0.0',
						'general.useragent.override':user_agent,
						'network.proxy.type':1,
						'network.proxy.http':proxy.split(':')[0],
						'network.proxy.http_port':int(proxy.split(':')[1]),
						'network.proxy.ssl':proxy.split(':')[0],
						'network.proxy.ssl_port':int(proxy.split(':')[1])
					})
					if args.headless:
						firefox_options.add_argument('--headless')
					driver=webdriver.Firefox(options=firefox_options,service_log_path=devnull)
				process=driver.service.process
				pid=process.pid
				cpids=[x.pid for x in psutil.Process(pid).children()]
				pids=[pid]+cpids
				drivers.extend(pids)
				if args.slow_start:
					locks[1].release()
				print('[INFO][%d] Successully started webdriver!'%id)
				driver.set_page_load_timeout(30);
				print('[INFO][%d] Opening %s'%(id,url))
				driver.get(url)
				if not any(x in driver.page_source for x in ['ERR_','<html><head></head><body></body></html>']):
					print('[INFO][%d] Website successfully loaded!'%id)
					while driver.find_element_by_id('countdown').get_attribute('innerHTML')!='0 seconds':
						sleep(1)
					sleep(1)
					driver.find_element_by_id('skip_bu2tton').click()
					print('[INFO][%d] Ad successfully viewed!'%id)
				else:
					print('[WARNING][%d] Dead proxy eliminated!'%id)
			except TimeoutException:
				print('[WARNING][%d] Request timed out!'%id)
			except NoSuchWindowException:
				print('[ERROR][%d] Window has been closed unexpectedly!'%id)
			except (NoSuchElementException,ElementNotVisibleException):
				print('[ERROR][%d] Skip ad button not found!'%id)
			except ElementNotVisibleException:
				print('[ERROR][%d] Skip ad button is not visible!'%id)
			except ElementClickInterceptedException:
				print('[ERROR][%d] Skip ad button could not be clicked!'%id)
			finally:
				with locks[2]:
					print('[INFO][%d] Quitting webdriver!'%id)
					try:driver.quit()
					except:print('[ERROR][%d] Error quitting webdriver!'%id)
					for pid in pids:
						try:drivers.remove(pid)
						except:pass
		except KeyboardInterrupt:pass
		except:
			with locks[3]:exception=format_exc()

if __name__=='__main__':
	try:
		parser=ArgumentParser()
		parser.add_argument('-t','--threads',type=int,help='set number of the threads',default=15)
		parser.add_argument('-u','--url',help='set url of the video/set the path of the urls list',default='',required=True)
		parser.add_argument('-p','--proxies',help='set the path of the proxies list')
		parser.add_argument('-us','--user-agent',help='set the user agent/set the path of to the list of user agents')
		parser.add_argument('-d','--driver',help='set the webdriver for the bot',choices=['chrome','firefox'],default='chrome')
		parser.add_argument('-hd','--headless',help='set the webdriver as headless',action='store_true')
		parser.add_argument('-s','--slow-start',help='starts webdrivers one by one',action='store_true')
		args=parser.parse_args()
		if args.url:
			if path.isfile(args.url):
				urls=open(args.url,'r').read().strip().split('\n')
			else:
				urls=[args.url]
		urls=[re.sub(r'\A(?:https?://)?(.*)\Z',r'https://\1',x) for x in urls]
		if args.user_agent:
			if path.isfile(args.user_agent):
				user_agents=open(args.user_agent,'r').read().strip().split('\n')
			else:
				user_agents=[args.user_agent]
		else:
			user_agents=generate_user_agent
		locks=[Lock() for _ in range(4)]
		drivers=[]
		proxies=[]
		for i in range(args.threads):
			t=Thread(target=bot,args=(i+1,))
			t.daemon=True
			t.start()
		while True:
			try:exception
			except:pass
			else:
				print(exception)
				exit(2)
			sleep(0.25)
	except KeyboardInterrupt:exit(0)
	except:exit(1)
