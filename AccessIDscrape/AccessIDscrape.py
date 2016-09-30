import pandas as pd
from bs4 import BeautifulSoup
import requests

import re
import csv


df = pd.read_csv('P1 Class Directory - User Info.csv')
df['FullName'] = df['FIRST NAME (PREFERRED)'] + '+' + df['LAST NAME (PREFERRED)']

FullName = df['FullName'].tolist()
accessID_dict = {'AccessID': 'Full Name'}

#Scrape Wayne directory for all names, save results in a dictionary of {ID: name}
for person in FullName:
    print(person)
    html = requests.get('https://wayne.edu/people/?type=people&q=' + person)
    soup = BeautifulSoup(html.text, "lxml")

    for elem in soup.find_all('a', href=re.compile('/people/(\w+)')):
        accessID = elem['href']
        accessID = accessID[8:14]
        print(accessID)
        accessID_dict[accessID] = person

print(accessID_dict)
#Save dict as csv
with open('unclean_ID_index.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['AccessID', 'Full Name'])
    w.writerows(accessID_dict.items())


#open it back up
df2 = pd.read_csv('unclean_ID_index.csv')

keyword = re.compile(r'Doctor of Pharmacy')


#Clean out the people who aren't in PharmD program
#This is a bug when a name returns search hits for more than one person in the pharm program... oops
for ID in df2.ix[:, 0]:
    html = requests.get('https://wayne.edu/people/' + ID)
    soup = BeautifulSoup(html.text, "lxml")
    print(ID)

    soup_2_string = str(soup)
    if keyword.search(soup_2_string) is None:
        print('Not a PharmD student')
        df2 = df2[df2.ix[:, 0].str.contains(ID) == False]

    if keyword.search(soup_2_string) is not None:
        print('PharmD student found')


#need to insert indexes


df2.ix[:, 1] = df2.ix[:, 1].str.replace('+', ' ')

print(df2)
df2[['First Name','Last Name']] = df2['Full Name'].loc[df2['Full Name'].str.split().str.len() == 2].str.split(expand=True)

df2 = df2.drop('Full Name', 1)


#flip columns
columns = df2.columns.tolist()
columns = columns[2:] + columns[1:2] + columns[0:1]

df2 = df2[columns]
df2 = df2.sort_values('Last Name')

print(df2)

df2.to_csv('final_ID_list.csv', index=False)

