#!/usr/bin/env python

# onlineResList - Makes an entry to the .txt doc.
#	takes link from the clipboard, <title> from the web page and comment from the clipboard.
#	Saves document in ~/Py directory, under the name 'online_resources.txt'
# Dodaje na spisak resursa za ucenje pajtona linkove sa naslovima
# Link ucitava iz klipborda, sa sajda skida <title>, a komentar uzima sa terminala

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
if len(sys.argv) >1:
	note =' '.join(sys.argv[1:])
	entry = f'{title}\n{note}\n{link}\n\n\n'
else:
	entry = f'{title}\n{link}\n\n\n'

# Creating an entry.
file = open('/Users/mladenimac/Py/online_resources.txt', 'a')
file.write(entry)
file.close()
print('\nEntry made.\n')