# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:24:05 2020

@author: prateek
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
    fourD1 =[]
    fiveD= []
    sixD = []
    
    for page in range(0,20):
        file = open('Data/Met-Data/%i.html'% page, 'rb')

        plain_text = file.read()

        soup = BeautifulSoup(plain_text, "lxml")
        D_count =0
        flag =1 
        R_count=0
        
        for div in soup.findAll('p', {'itemprop': 'description'}):
            c = div.get_text()
            zeroD.append(c)
            D_count += 1
    
        
        for div in soup.findAll('meta', {'itemprop': 'ratingValue'}):
            c = div.get('content')
            
            if flag ==1:
                flag += 1
                continue
            elif R_count== D_count:
                continue
            else:
                R_count += 1
                oneD.append(c)
                
        for div in soup.findAll('meta', {'itemprop': 'datePublished'}):
            c = div.get('content')
            twoD.append(c)
        
        for div in soup.findAll('meta', {'itemprop': 'author'}):
            c = div.get('content')
            threeD.append(c)   
    yield threeD,oneD,twoD,zeroD
     

if __name__ == "__main__":
    start = timer()
         
    duration = timer() - start
    print(duration)
    final=met_data()
    workbook = xlsxwriter.Workbook('Data/MyData.xlsx') 
    worksheet = workbook.add_worksheet("My sheet")         
    row = 0
    col = 0
   
   
    for zeroD in (final): 
        for reviewTitle in zeroD:
            for last in reviewTitle:
                worksheet.write(row, col + 1, last) 
                row += 1
            col += 1
            row = 0
       
    workbook.close()
  
    duration = timer() - start
    print(duration)
