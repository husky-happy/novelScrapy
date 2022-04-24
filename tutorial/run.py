from scrapy.cmdline import execute
import sys
import os
website = 'chyks'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(("scrapy crawl "+str(website)).split())