# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:38:54 2019

@author: Prateek
"""

import csv,os
import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd
from timeit import default_timer as timer
import xlsxwriter



def met_data():
    zeroD = []
    oneD = []
    twoD = []
    threeD = []
    fourD = []
    fiveD= []
    sixD = []
    
    for page in range(1,2):
        file = open('dealerraterData/Met-Data/%i.html'% page, 'rb')

        plain_text = file.read()

        soup = BeautifulSoup(plain_text, "lxml")
        zeroD.append('!@#$%')
        oneD.append('!@#$%')
        twoD.append('!@#$%')
        threeD.append('!@#$%')
        fourD.append('!@#$%')
        fiveD.append('!@#$%')
        sixD.append('!@#$%')
        
        for div in soup.findAll('div', {'class': 'td valign-bottom pad-left-md pad-top-none pad-bottom-none'}):
            a = div.get_text()
            a = a.replace('\n' , '')
            a = a.replace(']' , '')
            a = a.replace(' ' , '')
            a = a.split('\r')
            zeroD.append(a[2])
                
        
        
      
    yield zeroD


if __name__ == "__main__":
   start = timer()
   final = met_data()
   
   '''
   workbook = xlsxwriter.Workbook('dealerraterData.xlsx') 
   worksheet = workbook.add_worksheet("My sheet")         
   row = 0
   col = 0
   
   
   for zeroD in (final): 
       
       for reviewTitle in zeroD:
           # worksheet.write('comment')
          
           worksheet.write(row, col + 1, reviewTitle) 
           row += 1
       row = 0

       
   workbook.close()   
   '''
   for zeroD in (final):
       print(zeroD)
   duration = timer() - start
   print(duration) 

     
     
     
     
     
     
     
     
     
     
     
     
     