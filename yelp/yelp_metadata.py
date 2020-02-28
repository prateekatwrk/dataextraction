# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:12:30 2020

@author: prateek
"""


import requests
import sys
import os
import time


def fetch():
  done = 5
  i = 1
   
  for page in range(0,400,20):
   
        url = 'https://www.yelp.com/biz/bar-louie-dallas-6??start=%i' % (
                        page)
 
        source_code = requests.get(url)

        plain_text = source_code.text.encode('utf-8')

        if not os.path.exists("Data/Met-Data/"):
                os.makedirs("Data/Met-Data/")
        file = page/20
               
        with open("Data/Met-Data/%i.html" % file , "wb") as output_file:
                output_file.write(plain_text)

        if i == 20:
            done = 100

        sys.stdout.write("\r[%s%s] %d%% Completed" %
                             ('=' * i, ' ' * (20 - i), done))
        done = done + 5
        i += 1

        sys.stdout.flush()
        
if __name__ == "__main__":
    start = time.time()
    fetch()
    end = time.time()
    print('\nTime Taken : ', end - start, 'seconds')
    
    
    
    
    
    
    
    
    
    