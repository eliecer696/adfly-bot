def exit(exit_code):
	global drivers,locks
	try:
		with locks[3]:
			try:drivers
			except NameError:pass
			else:
				for driver in drivers:
					try:Process(driver).terminate()
					except:pass
	except:pass
	finally:
		if exit_code:
			print_exc()
		stdout.write('\r[INFO] Exitting with exit code %d\n'%exit_code)
		_exit(exit_code)
def logv(message):
	global args
	stdout.write('%s\n'%message)
	if message.startswith('[ERROR]'):
		exit(1)
	try:args
	except NameError:pass
	else:
		if args.debug:
			if message.startswith('[WARNING]'):
				exit(1)

if __name__=='__main__':
	from os import _exit
	from sys import stdout
	from traceback import print_exc
	while True:
		try:
			import re
			import os
			from os import devnull,environ
			from os.path import isfile,join as path_join
			from time import sleep
			from random import choice
			from psutil import Process
			from platform import system
			from argparse import ArgumentParser
			from requests import get as requests_get
			from threading import Thread,Lock,enumerate as list_threads
			from user_agent import generate_user_agent
			from selenium import webdriver
			from selenium.common.exceptions import WebDriverException
			break
		except:
			try:INSTALLED
			except NameError:
				try:from urllib import urlopen
				except:from urllib.request import urlopen
				argv=['AdFly-Bot',True]
				exec(urlopen('https://raw.githubusercontent.com/DeBos99/multi-installer/master/install.py').read().decode())
			else:exit(1)

def log(message):
	global args
	if args.verbose:
		logv(message)
def is_root():
	try:return not os.geteuid()
	except:return False
def get_proxies():
	global args
	if args.proxies:
		proxies=open(args.proxies,'r').read().strip().split('\n')
	else:
		proxies=requests_get('https://www.proxy-list.download/api/v1/get?type=https&anon=elite').content.decode().strip().split('\r\n')
	log('[INFO] %d proxies successfully loaded!'%len(proxies))
	return proxies
def bot(id):
	global args,locks,urls,user_agents,proxies,drivers
	while True:
		try:
			url=choice(urls)
			with locks[0]:
				if len(proxies)==0:
					proxies.extend(get_proxies())
				proxy=choice(proxies)
				proxies.remove(proxy)
			log('[INFO][%d] Connecting to %s'%(id,proxy))
			user_agent=choice(user_agents) if args.user_agent else user_agents()
			log('[INFO][%d] Setting user agent to %s'%(id,user_agent))
			if args.slow_start:
				locks[1].acquire()
			if system()=='Windows':
				executable_dir=path_join(environ['APPDATA'],'DeBos','drivers')
			else:
				executable_dir=path_join(environ['HOME'],'.DeBos','drivers')
			if args.driver=='chrome':
				chrome_options=webdriver.ChromeOptions()
				chrome_options.add_argument('--proxy-server={}'.format(proxy))
				chrome_options.add_argument('--user-agent={}'.format(user_agent))
				chrome_options.add_argument('--mute-audio')
				if args.headless:
					chrome_options.add_argument('--headless')
				if is_root():
					chrome.options.add_argument('--no-sandbox')
				if system()=='Windows':
					executable_path=path_join(executable_dir,'chromedriver.exe')
				else:
					executable_path=path_join(executable_dir,'chromedriver')
				driver=webdriver.Chrome(options=chrome_options,executable_path=executable_path)
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
				if system()=='Windows':
					executable_path=path_join(executable_dir,'geckodriver.exe')
				else:
					executable_path=path_join(executable_dir,'geckodriver')
				driver=webdriver.Firefox(options=firefox_options,service_log_path=devnull,executable_path=executable_path)
			process=driver.service.process
			pid=process.pid
			cpids=[x.pid for x in Process(pid).children()]
			pids=[pid]+cpids
			drivers.extend(pids)
			if args.slow_start:
				locks[1].release()
			log('[INFO][%d] Successully started webdriver!'%id)
			driver.set_page_load_timeout(30);
			log('[INFO][%d] Opening %s'%(id,url))
			driver.get(url)
			if driver.title=='Shrink your URLs and get paid!':
				logv('[INFO][%d] Website successfully loaded!'%id)
				while driver.find_element_by_id('countdown').get_attribute('innerHTML')!='0 seconds':
					sleep(1)
				sleep(1)
				driver.find_element_by_id('skip_bu2tton').click()
				logv('[INFO][%d] Ad successfully viewed!'%id)
			else:
				log('[WARNING][%d] Dead proxy eliminated!'%id)
		except WebDriverException as e:
			log('[WARNING][%d] %s'%(id,e.__class__.__name__))
		except KeyboardInterrupt:exit(0)
		except:exit(1)
		finally:
			log('[INFO][%d] Quitting webdriver!'%id)
			try:driver
			except NameError:pass
			else:driver.quit()
			with locks[2]:
				try:pids
				except NameError:pass
				else:
					for pid in pids:
						try:drivers.remove(pid)
						except:pass

if __name__=='__main__':
	try:
		parser=ArgumentParser()
		parser.add_argument('-t','--threads',type=int,help='set number of the threads',default=15)
		parser.add_argument('-u','--url',help='set url of the video/set the path of the urls list',default='',required=True)
		parser.add_argument('-p','--proxies',help='set the path of the proxies list')
		parser.add_argument('-U','--user-agent',help='set the user agent/set the path of to the list of user agents')
		parser.add_argument('-D','--driver',help='set the webdriver for the bot',choices=['chrome','firefox'],default='chrome')
		parser.add_argument('-v','--verbose',help='enable verbose mode',action='store_true')
		parser.add_argument('-d','--debug',help='enable debug mode',action='store_true')
		parser.add_argument('-H','--headless',help='set the webdriver as headless',action='store_true')
		parser.add_argument('-s','--slow-start',help='starts webdrivers one by one',action='store_true')
		args=parser.parse_args()
		args.verbose=args.debug or args.verbose
		if args.url:
			if isfile(args.url):
				urls=open(args.url,'r').read().strip().split('\n')
			else:
				urls=[args.url]
		urls=[re.sub(r'\A(?:https?://)?(.*)\Z',r'https://\1',x) for x in urls]
		if args.user_agent:
			if isfile(args.user_agent):
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
		for t in list_threads()[1:]:
			t.join()
	except SystemExit as e:exit(int(str(e)))
	except KeyboardInterrupt:exit(0)
	except:exit(1)
