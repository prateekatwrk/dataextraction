# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:59:57 2019

@author: prateek
"""

import requests
import sys
import os
import time


def fetch():
    done = 2.63
    i = 1
   
    url = 'https://www.sitejabber.com/reviews/allergybuyersclub.com'
    source_code = requests.get(url)

    plain_text = source_code.text.encode('utf-8')

    if not os.path.exists("../Data/Met-Data/"):
                os.makedirs("../Data/Met-Data/")

    with open("../Data/Met-Data/allergybuyersclub.html" , "wb") as output_file:
                output_file.write(plain_text)

    

if __name__ == "__main__":
    start = time.time()
    fetch()
    end = time.time()
    print('\nTime Taken : ', end - start, 'seconds')