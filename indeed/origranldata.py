# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:35:44 2019

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
    
    for page in range(0,50):
        file = open('Data/Met-Data/%i.html'% page, 'rb')

        plain_text = file.read()

        soup = BeautifulSoup(plain_text, "lxml")
        zeroD.append('!@#$%')
        oneD.append('!@#$%')
        twoD.append('!@#$%')
        threeD.append('!@#$%')
        fourD.append('!@#$%')
        fiveD.append('!@#$%')
        sixD.append('!@#$%')
        
        for div in soup.findAll('div', {'class': 'cmp-review-title'}):
            a = div.get_text()
            zeroD.append(a)
                
        for div in soup.findAll('span', {'class': 'cmp-reviewer-job-title'}):
                f = div.get_text()
                f = f.replace(' – \xa0', '')
                z = f.split('(')
                z[1] = z[1].replace(')', '')
                oneD.append(z[0]) 
                twoD.append(z[1])

        for div in soup.findAll('span', {'class': 'cmp-review-date-created'}):
            c = div.get_text()
            threeD.append(c)            
                            
        for div in soup.findAll('span', {'class': 'cmp-reviewer-job-location'}):
                d = div.get_text()
                fourD.append(d) 
            
        for div in soup.findAll('span', {'class': 'cmp-review-text'}):
                e = div.get_text()
                fiveD.append(e) 
    
        for div in soup.findAll('div', {'class': 'cmp-ratingNumber'}):
            b = div.get_text()
            sixD.append(b)
    
      
    yield sixD,zeroD,oneD,twoD,threeD,fourD,fiveD


if __name__ == "__main__":
   start = timer()
   final = met_data()
   
   
   workbook = xlsxwriter.Workbook('Toyota_indeed_data.xlsx') 
   worksheet = workbook.add_worksheet("My sheet")         
   row = 0
   col = 0
   
   
   for sixD,zeroD,oneD,twoD,threeD,fourD,fiveD in (final): 
       for rateing in sixD:
           #worksheet.write('rating')
           worksheet.write(row, col, rateing) 
           row += 1
       row = 0 
       for reviewTitle in zeroD:
           # worksheet.write('comment')
          
           worksheet.write(row, col + 1, reviewTitle) 
           row += 1
       row = 0

       for jobtitle in oneD:
           #worksheet.write('jobtitle')
           worksheet.write(row, col +2, jobtitle) 
           row += 1
       row = 0 
       for jobtitle2 in twoD:
           #worksheet.write('rating')
           worksheet.write(row, col +3, jobtitle2) 
           row += 1
       row = 0 
       
       for reviewdata in threeD:
           #worksheet.write('rating')
           worksheet.write(row, col +4, reviewdata) 
           row += 1
       row = 0 
       for reviewerjoblocation in fourD:
           #worksheet.write('rating')
           worksheet.write(row, col +5, reviewerjoblocation) 
           row += 1
       row = 0 
       for reviewtext in fiveD:
           #worksheet.write('rating')
           worksheet.write(row, col +6, reviewtext) 
           row += 1
       row = 0 
       
       
       
       
       
       
   workbook.close()   
   duration = timer() - start
   print(duration) 

     
     
     
     
     
     
     
     
     
     
     
     
     