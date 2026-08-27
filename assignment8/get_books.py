#Task 1: Review robots.txt to Ensure Policy Compliance
""" 
1. Open [https://durhamcountylibrary.org/robots.txt]
2. Verify that the following steps are not in breach of policy. """

#Task 2: Understanding HTML and the DOM for the Durham Library Site
""" 
1. Open [https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart]
2. Open your browser developer tools to show the HTML elements.  For Chrome, this is shift-ctrl-J.
3. li - class - row cp-search-result-item
4.Title - h3 - class - cp-title
5. author - a - class - author-link
6. book year and format : div- cp-format-info, span - display-info-primary """

#Task 3: Write a Program to Extract this Data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

book_list = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
results = []

print(f"Number of search results found: {len(book_list)}")

for item in book_list:
    title_h3 = item.find_element(By.CSS_SELECTOR, "span.title-content")
    #print("Title", title_h3.text) 
    title = title_h3.text.strip()
    
    author_a = item.find_element(By.CSS_SELECTOR, "a.author-link")
    authors = author_a.text.strip().split(",")
    
    format_div = item.find_element(By.CSS_SELECTOR, "div.cp-format-info")
    format_span = format_div.find_element(By.CSS_SELECTOR, "span.display-info-primary")
    format_year = format_span.text.strip()
    
    if len(authors) > 1:
        author_name = authors[0] + ';' + authors[1]
        #print(author_name)
    else:
        author_name = authors[0].strip()
        
    results.append({"Title": title, "Author": author_name, "Format-Year": format_year})
    
book_df = pd.DataFrame(results)
print("Books List:")
print(book_df)
    
#Task 4: Write out the Data
#wrting book search results to csv file
book_df.to_csv("assignment8/get_books.csv", index=False)
        

#wrting book search results to json file
json_data = {"results": results}
with open("assignment8/get_books.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)
 
driver.quit()