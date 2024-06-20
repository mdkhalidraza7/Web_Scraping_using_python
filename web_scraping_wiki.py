#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import os
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import pos_tag
from textstat import flesch_reading_ease, syllable_count
from nltk import punkt


# In[2]:


# Loading the XLSX file into a pandas DataFrame
xlsx_file = r'D:\khalid\myproject\web scraping\wikiweb.xlsx'
df = pd.read_excel(xlsx_file)
display(df)

# Specifing the class names for article text found under inpection or URL
article_class = "mw-body-content" 
article_classb = "mw-body-content"


# In[3]:


# Function to extract title and article text under the specified class from a URL
def extract_article(url, idd):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.text if soup.title else "No title found"
        
        specified_div = soup.find('div', class_=article_class)
        specified_divb = soup.find('div', class_=article_classb)
        
        if specified_div:
            p_tags = specified_div.find_all('p')
            article_text = '\n'.join([p.get_text() for p in p_tags])
        elif specified_divb:
            p_tags = specified_divb.find_all("p")
            article_text = '\n'.join([p.get_text() for p in p_tags])
        else:
            print(f"No content found for URL: {url}")
            return
        #saving each extracted url data as text file
        filename = f"{idd}.txt"
        filepath = os.path.join(r"D:\khalid\myproject\web scraping\wikiweb_texts", filename)
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(title + '\n\n')
            file.write(article_text)
            print(f"Saved article to {filename}")
         


# In[4]:


# Creating a directory to save text files 
os.makedirs(r"D:\khalid\myproject\web scraping\wikiweb_texts", exist_ok=True)


# In[5]:


# Iterating through the URLs and extract title and article text
for index, row in df.iterrows():
    url = row['URL']  
    idd = row['URL_ID']
    extract_article(url, idd)


# In[ ]:





# In[ ]:




