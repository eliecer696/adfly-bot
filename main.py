import re
import requests
from os import _exit,path
from sys import stdin
from time import sleep
from random import choice,uniform
from argparse import ArgumentParser
from threading import Thread
from traceback import print_exc
from collections import deque
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.common.proxy import Proxy,ProxyType

parser=ArgumentParser()
parser.add_argument('-t','--threads',type=int,help='set number of the threads',default=15)
parser.add_argument('-u','--url',help='set url of the video/set the path of the urls list',default='',required=True)
parser.add_argument('-p','--proxies',help='set the path of the proxies list')
parser.add_argument('-d','--driver',help='set the driver for the bot',choices=['chrome','firefox'],default='chrome')
parser.add_argument('-hd','--headless',help='set the driver as headless',action='store_true')
args=parser.parse_args()

def exit(exit_code):
	if exit_code!=0:
		print_exc()
	_exit(exit_code)
def update_proxies():
	global proxies
	if args.proxies:
		proxies=open(args.proxies,'r').read().split('\n')
	else:
		proxies=re.findall(re.compile('<td>([\d.]+)</td>'),str(requests.get('https://www.sslproxies.org/').content))
		proxies=['%s:%s'%x for x in list(zip(proxies[0::2],proxies[1::2]))]
	proxies=deque(proxies)
	print('%d proxies successfully loaded!'%len(proxies))
def bot():
	try:
		while True:
			url=choice(urls)
			if len(proxies)==0:
				update_proxies()
			proxy=proxies.pop()
			print(proxy)
			try:
				if args.driver=='chrome':
					chrome_options=webdriver.ChromeOptions()
					chrome_options.add_argument('--proxy-server={}'.format(proxy))
					if args.headless:
						chrome_options.add_argument('--headless')
					driver=webdriver.Chrome(options=chrome_options)
				else:
					options=webdriver.FirefoxOptions()
					options.headless=args.headless
					firefox_profile=webdriver.FirefoxProfile()
					firefox_profile.set_preference('network.proxy.type',1)
					firefox_profile.set_preference('network.proxy.http',proxy.split(':')[0])
					firefox_profile.set_preference('network.proxy.http_port',proxy.split(':')[1])
					firefox_profile.set_preference('network.proxy.ssl',proxy.split(':')[0])
					firefox_profile.set_preference('network.proxy.ssl_port',proxy.split(':')[1])
					firefox_profile.update_preferences()
					driver=webdriver.Firefox(firefox_profile=firefox_profile,options=options)
				driver.set_page_load_timeout(120);
				try:
					driver.get(url)
					if not any(x in driver.page_source for x in ['ERR_','<html><head></head><body></body></html>']):
						driver.find_element_by_id('skip_bu2tton').click()
						print('Success!')
					driver.quit()
				except TimeoutException:pass
			except WebDriverException:pass
	except KeyboardInterrupt:exit(0)
	except:exit(1)

try:
	if args.url:
		if path.isfile(args.url):
			urls=list(filter(None,open(args.url,'r').read().split('\n')))
		else:
			urls=[args.url]
	urls=[re.sub(r'\A(?:https?://)?(.*)\Z',r'https://\1',x) for x in urls]
	update_proxies()
	for i in range(args.threads):
		t=Thread(target=bot)
		t.daemon=True
		t.start()
		sleep(uniform(2.0,4.0))
	stdin.read(1)
	exit(0)
except KeyboardInterrupt:exit(0)
except:exit(1)
