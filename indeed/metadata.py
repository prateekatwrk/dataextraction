# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:26:28 2019

@author: Prateek
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:40:22 2019

@author: Prateek
"""

import requests
import sys
import os
import time


def fetch():
  done = .56
  i = 1 
    
  for page in range(1,3560,20):
    	
        url = 'https://www.indeed.com/cmp/Toyota/reviews?start=%i' % (
                        page)
 
        source_code = requests.get(url)

        plain_text = source_code.text.encode('utf-8')

        if not os.path.exists("Data/Met-Data/"):
                os.makedirs("Data/Met-Data/")
        pageno =page/20
        with open("Data/Met-Data/%i.html" % pageno , "wb") as output_file:
                output_file.write(plain_text)

        if i == 178:
            done = 100

        sys.stdout.write("\r[%s%s] %d%% Completed" %
                             ('=' * i, ' ' * (178 - i), done))
        done = done + .56
        i += 1

        sys.stdout.flush()



if __name__ == "__main__":
    start = time.time()
    fetch()
    end = time.time()
    print('\nTime Taken : ', end - start, 'seconds')
