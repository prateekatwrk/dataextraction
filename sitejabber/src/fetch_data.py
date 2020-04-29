# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:41:35 2019

@author: prateek
"""

import codecs
from lxml import html
import requests


page = requests.get('https://www.sitejabber.com/reviews/allergybuyersclub.com?page=2#reviews')
tree = html.fromstring(page.content)
'''
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print ('Buyers: ', buyers)
print ('Prices: ', prices)
'''

#This will create a list of reviews:
review = tree('//div[@class="review_title"]title()')
print ('Review: ', review)




