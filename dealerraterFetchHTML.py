# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:49:32 2019

@author: Prateek
"""


import requests
import sys
import os
import time


def fetch():
  done = 1.28
  i = 1
   
  for page in range(1,78):
   
      

        url = 'https://www.dealerrater.com/dealer/Fontana-Nissan-dealer-reviews-30400/page%i' % (
                        page)
 
        source_code = requests.get(url)

        plain_text = source_code.text.encode('utf-8')

        if not os.path.exists("dealerraterData/Met-Data/"):
                os.makedirs("dealerraterData/Met-Data/")
        file = page
               
        with open("dealerraterData/Met-Data/%i.html" % file , "wb") as output_file:
                output_file.write(plain_text)

        if i == 78:
            done = 100

        sys.stdout.write("\r[%s%s] %d%% Completed" %
                             ('=' * i, ' ' * (78 - i), done))
        done = done + 1.28
        i += 1

        sys.stdout.flush()
        
if __name__ == "__main__":
    start = time.time()
    fetch()
    end = time.time()
    print('\nTime Taken : ', end - start, 'seconds')