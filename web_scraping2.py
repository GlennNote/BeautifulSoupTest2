from bs4 import BeautifulSoup
import re

with open('index.html','r') as f: ##R stands for read
    doc =   BeautifulSoup(f, 'html.parser')

##tag = doc.find('option')
##tag['value'] = 'new value' ##access attribute value inside the tag and change it
##tag['color'] = 'blue' ##adding an attribute
##print(tag.attrs)
##print(tag)

##tag = doc.find_all(['p','div','li']) ##Searching for several tags within a document

    
##tag = doc.find(['option'], string='Undergraduate', value='Undergraduate')

##tag = doc.find_all(class_='btn-item') ##Searching for a class    

    
##tags = doc.find_all(string= re.compile('\$.*'), limit=1) ##limit number of results  
##for tag in tags:
##    print(tag.strip()) ##take care of whitespace


tags = doc.find_all('input', type='text')    
for tag in tags:
    tag['placeholder'] = 'I changed you!'

with open('changed.html', 'w') as file: ##w stands for write
    file.write(str(doc))