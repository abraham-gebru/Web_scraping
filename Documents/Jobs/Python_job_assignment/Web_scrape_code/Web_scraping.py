#!/usr/bin/env python
# coding: utf-8
#Author Abraham Gebru
# In[1]:


# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
from selenium import webdriver  
#from selenium.common.exceptions import NoSuchElementException  
#from selenium.webdriver.common.keys import Keys  


html_count =0
#The output file contains two columns with the content list and content description
rows = []
rows.append(['Content list', 'content description'])

    # In[10]:
    
#Web scraping function    
def webscrape():
    
    html_source = browser.page_source   
    #Create beautifulsoup object
    soup = BeautifulSoup(html_source,'html.parser')
    #find all the links from the html file
    link_output = soup.findAll('a')  
    
    #scraping from all desired links
    for input_value in range (len(link_output)):
        #select only links that contains 'ZACH' content
        if "view" in link_output[input_value].contents[0]: 
            print(link_output[input_value].contents[0])
            print("")
            urlpage=link_output[input_value].contents[0]
            # query the website and return the html to the variable 'page'
            page = urllib.request.urlopen(urlpage)
            # parse the html using beautiful soup and store in variable 'soup'
            soup = BeautifulSoup(page, 'html.parser')
            # find results within table
            licence_holder = soup.find('div', class_='box_content')
            licence_number = soup.find('div', class_='license_table box form')
            licence_info = soup.find('table', attrs={'class': 'box_content'})
            i=0
            for int_value in range(3):
                if int_value==0:
                    #extract license number
                    data = licence_number.find_all('h2')     
                    Col1 = 'License'
                    Col2 = data[0].getText()
                    rows.append([Col1, Col2])
                elif int_value==1:
                    #extract the license holder full name
                    results = licence_holder.find_all('tr')
                    for result in results:
                        # find all columns per result
                        data = result.find_all('td')
                        # check that columns have data 
                        if len(data) == 0 | len(data) == 1: 
                            continue
                        Col1 = 'Name'
                        Col2 = data[0].getText()
                        rows.append([Col1, Col2])
                else:
                    #extract license status, license type, multistate?, date issued, expiration date
                    results = licence_info.find_all('tr')
                    for result in results:
                        i=i+1;
                        data = result.find_all('td')
                        if len(data) == 0 | len(data) == 1: 
                            continue
                        Col1 = data[0].getText()
                        Col2 = data[1].getText()
                        rows.append([Col1, Col2])
                        if i==6:
                            break

                            #%%
#create an object of webdriver for firefox browser                        
browser =webdriver.Firefox(executable_path = '/home/abraham/Documents/Jobs/Python_job_assignment/geckodriver-v0.24.0-linux64/geckodriver')  
#use the first page locally saved html source code
browser.get('file:///home/abraham/Documents/Jobs/Python_job_assignment/webscrapfile.html')
webscrape()
#%%

#create an object of webdriver for firefox browser
browser =webdriver.Firefox(executable_path = '/home/abraham/Documents/Jobs/Python_job_assignment/geckodriver-v0.24.0-linux64/geckodriver')  
#use the second page locally saved html source code
browser.get('file:///home/abraham/Documents/Jobs/Python_job_assignment/webpage_source_four.html')
webscrape()
#%%
#create an object of webdriver for firefox browser
browser =webdriver.Firefox(executable_path = '/home/abraham/Documents/Jobs/Python_job_assignment/geckodriver-v0.24.0-linux64/geckodriver')  
#use the third page locally saved html source code
browser.get('file:///home/abraham/Documents/Jobs/Python_job_assignment/webpage_source_five.html')
webscrape()
#%%
print(rows)
# Create csv and write rows to output file
with open('web_scrape_zach.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)


# In[ ]:




