#!/usr/bin/env python

# onlineResList - Makes an entry to the .txt doc.
#	takes link from the clipboard, <title> from the web page and comment from the clipboard.
#
# Depending on the keyword 'java' or 'python'saves document in predefined directory, under the name 'python_resources.txt' or 'java_resources.txt'
# Dodaje na spisak resursa za ucenje pajtona linkove sa naslovima
# Link ucitava iz klipborda, sa sajda skida <title>, a komentar uzima sa terminala


# Syntax: python onlineResList.py java TextOfTheNote

import os, sys, pyperclip, requests, bs4

# Getting the link, accsessing the web-page and getting the title.
link = pyperclip.paste()
try:
	res = requests.get(link)
	res.raise_for_status()
except:
	print(f'ERROR:\nLink \'{link}\' not valid\n')
try:	
	soup = bs4.BeautifulSoup(res.text, features = 'html.parser') 
	title = soup.find('title').text
except NameError: exit()
# Checking if there are any comments added.
if len(sys.argv) >2:
	note =' '.join(sys.argv[2:])
	entry = f'{title}\n{note}\n{link}\n\n\n'
else:
	entry = f'{title}\n{link}\n\n\n'

# Creating an entry.
if sys.argv[1] == 'python':
	with open('/Users/mladenimac/Py/python_resources.txt', 'a') as file:
		file.write(entry)
		file.close()
	print('\nEntry made to python resouce file.\n')
elif sys.argv[1] == 'java':
	with open('/Users/mladenimac/Java/Java_resources.txt', 'a') as file:
		file.write(entry)
		file.close()
	print('\nEntry made to java resource file.\n')
else:
	print('Cant determine the  document to edit./nType "java" or "python" keywords, without quotation marks.')