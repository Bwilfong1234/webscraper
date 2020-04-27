#!/usr/bin/env python
# coding: utf-8

# In[51]:


import os
from bs4 import BeautifulSoup as bs
import requests
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from splinter import Browser
import time


# In[52]:


def scrape_info():


    url = 'https://mars.nasa.gov/news/'


    # In[53]:


    response = requests.get(url)


    # In[54]:


    soup = bs(response.text, 'html.parser')


    # In[55]:


    print(soup.prettify())


    # In[56]:


    results2=soup.find_all('div', class_='content_title')

    print(results2)


    # In[58]:


    Header=[]


    # In[57]:


    result=soup.find_all('div', class_='rollover_description_inner')
    # print(result)


    # In[59]:


    results2=soup.find_all('div', class_='content_title')
    # scrape the article header 
    for result in results2:
        try:
    
            header = result.a.text
            if (header):
                Header.append(header)
                print('-----------------')
                print(header)

        except AttributeError as e:
            print(e)
    time.sleep(1)       
            
    # browser.quit()        



    # In[68]:


    head=Header[0]


    # In[69]:


    head


    # In[62]:


    Newsartical=[]


    # In[63]:


    result34=soup.find_all('div', class_='rollover_description_inner')
    # scrape the article header 
    for result in result34:
        try:
    
            news_p = result.text
            if (news_p):
                print('-----------------')
                Newsartical.append(news_p)
                print(news_p)

        except AttributeError as e:
            print(e)
    time.sleep(1)       
            
    # browser.quit()


    # In[66]:


    snooz= Newsartical[0]


    # In[67]:


    snooz


    # In[14]:


    #  get_ipython().system('which chromedriver')


    # In[15]:


    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    # browser = Browser('chrome', **executable_path, headless=False)


    # In[16]:


    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    time.sleep(5)

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    time.sleep(5)
    browser.click_link_by_partial_text('FULL')
    time.sleep(5)
    for x in (2,2):
        html = browser.html
        soup = bs(html, 'html.parser')
        Divs = soup.find_all("div", class_='fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open')
        try:
            for image in Divs:
                featuredimg=image.img['src']
                print('page:', x, '-------------')
                print(image.img['src'])
                featuredimgurl= f"https://www.jpl.nasa.gov{featuredimg}"
        except AttributeError as e:
            print(e)

    time.sleep(3)       
            
    # browser.quit()


    # In[18]:


    featuredimgurl= f"https://www.jpl.nasa.gov{featuredimg}"


    # In[19]:





    # In[20]:


    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    # browser = Browser('chrome', **executable_path, headless=False)
    # time.sleep(5)

    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    time.sleep(5)
    for x in (1,1):
        html = browser.html
        soup = bs(html, 'html.parser')
        Divs2 = soup.findAll('span')
        wetertext=[]
        try:
            for whether in Divs2:
                wetertext.append(whether.text)
                print('page:', x, '-------------')
                print(whether.text)
        
        except AttributeError as e:
            print(e)
    time.sleep(3)       
            
    # browser.quit()


    # In[24]:


    wetertext
    check='InSight sol'
    res = [idx for idx in wetertext if idx.lower().startswith(check.lower())]
    Wether_report=res[0]
    Wether_report


    # In[25]:





    # In[26]:


    import pandas as pd


    # In[27]:


    url = 'https://space-facts.com/mars/'
    tables= pd.read_html(url)
    df = tables[1]
    df
    table=df.to_html( 
    classes='table table-striped' 
    ) 
    table.replace('\n', '')  
    
    # In[44]:


    hemisphere_image_ur=[]
    # bb=[]


    # In[46]:


    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    # browser = Browser('chrome', **executable_path, headless=False)
    # time.sleep(5)

    url5 ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus')
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    Divs12 = soup.find("div", class_='downloads')
    imglink1= Divs12.a['href']
    hemisphere_image_ur.append(imglink1)

    time.sleep(3)       
            
    # browser.quit()



    # In[ ]:


    # html = browser.html
    # soup = bs(html, 'html.parser')
    # Divs12 = soup.find("div", class_='downloads')
    # print(Divs12.a['href'])


    # In[ ]:





    # In[ ]:





    # In[47]:


    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    # browser = Browser('chrome', **executable_path, headless=False)
    # time.sleep(5)

    url5 ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    time.sleep(5)
    browser.click_link_by_partial_text('Valles')
   
    html = browser.html
    soup = bs(html, 'html.parser')
    Divs12 = soup.find("div", class_='downloads')
    imglink2= Divs12.a['href']
    hemisphere_image_ur.append(imglink2)
    time.sleep(3)       
            
    # browser.quit()


    # In[ ]:





    # In[48]:


    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    # browser = Browser('chrome', **executable_path, headless=False)
    # time.sleep(5)

    url5 ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli')
    html = browser.html
    soup = bs(html, 'html.parser')
    Divs12 = soup.find("div", class_='downloads')
    imglink3= Divs12.a['href']
    hemisphere_image_ur.append(imglink3)
    time.sleep(3)       
  

    # In[49]:


    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    # browser = Browser('chrome', **executable_path, headless=False)
    # time.sleep(5)

    url5 ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis')
    time.sleep(5)
    html = browser.html
    soup = bs(html, 'html.parser')
    Divs12 = soup.find("div", class_='downloads')
    imglink4= Divs12.a['href']
    hemisphere_image_ur.append(imglink4)

    time.sleep(3)       
            
    # browser.quit()

# 'Syrtis': 'Syrtis Major Hemisphere', f"'Schiaparelli': 'Schiaparelli Hemisphere', f"'Valles': 'Valles Marineris Hemisphere'

    # In[50]:


    hemisphere_image_ur
    Syrtiss=f"{hemisphere_image_ur[-1]}"
    #Syrtiss.append(f"{hemisphere_image_ur[-1]}")
    Schiaparelli=f"{hemisphere_image_ur[2]}"
   # Schiaparelli.appendf"{hemisphere_image_ur[2]}"
    Valles=f"{hemisphere_image_ur[1]}"
    #Valles.append(f"{hemisphere_image_ur[1]}")
    Cerberus=f"{hemisphere_image_ur[0]}"
   #Cerberus.append(f"{hemisphere_image_ur[0]}")

    # In[ ]:

    # scrape= (hemisphere_image_ur, Wether_report,snooz,head,featuredimgurl)

    costa_datas = {
            "Fetured": featuredimgurl,
            "Header": head,
            "bodys": snooz,
            "Wether_report": Wether_report,
            "Syrtis":Syrtiss,
            "Schiaparelli":Schiaparelli,
            "Valles":Valles,
            "Cerberus":Cerberus,
            "table":table
        }
    browser.quit()

    # Return results
    return costa_datas
