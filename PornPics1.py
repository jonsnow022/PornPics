# A program that takes image links of pornpics gallery and downloads them.
# It won't download gallery's that pornpics redirects to other websites
# only images that are on the pornpics website
# This is my first program that does something "useful" even tho it's porn
# Always wanted a tool like this for my "homework" folder ;)
# I know some of this code (or all) its terrible code but hey it works

import requests
from bs4 import BeautifulSoup
import os

def banner():

	# Checking to see if OS is Windows or linux
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")

	print('''
	______                      ______  _             
	| ___ \                     | ___ \(_)            
	| |_/ /  ___   _ __  _ __   | |_/ / _   ___  ___  
	|  __/  / _ \ | '__|| '_ \  |  __/ | | / __|/ __| 
	| |    | (_) || |   | | | | | |    | || (__ \__ \ 
	\_|     \___/ |_|   |_| |_| \_|    |_| \___||___/ \n
	''')


banner()
# list to store links
links = []
split = "-" * 58 # to look a bit cleaner

def create_dir(dir_name):
	# Checking if dir exists if not making one
	if not(os.path.isdir(dir_name)):
		os.makedirs(dir_name)

def get_links(link, links):

	# Getting the html and putting it on a bs object
	req = requests.get(link).text
	soup = BeautifulSoup(req, 'lxml')

	# Finding the specific links (with href) and appending them into a list
	for href_links in soup.find_all(class_="rel-link", href=True):
		links.append(href_links['href'])


def gallery_picker():
	# A list to store all the gallery links
	store_gallery_links = []

	while True:
		gallery_link = input("Enter PornPics link: ")
		store_gallery_links.append(gallery_link)
		# if 99 is pressed break the loop and pop the 99 bc it causes errors requets module as it isn't a link
		if gallery_link == "99":
			store_gallery_links.pop(-1)
			break

	# Getting the image links of individual gallery's
	for gallery_link in store_gallery_links:
		get_links(gallery_link, links)



def download_images(dir_name, links):

	print(split)
	print("Got the links, Downloading images")
	print(split)
	# Changing to the created dir
	os.chdir(dir_name)

	# looping through the links and slicking the names of images and downloading them
	img_count = 1

	for link in links:
		full_name = link[-12:]
		# wb for writing bytes
		with open(full_name, 'wb') as img:
		# Getting the request of the image and writing it
			img_req = requests.get(link).content
			img.write(img_req)

			print(f"Downloading image: {img_count}")
			img_count += 1

# The End
# Now just just the main screen and calling functions

def main():

	print(split)
	print("Choose The Mode You Want")
	print(split)
	print("1.Normal Mode (One Gallery)")
	print("2.Gallery Picker (Multiple Gallery's)")
	print(split)

	mode = input("Mode: ")

	if mode == "1":
		banner()

		print(split)
		print("Normal Mode")
		print(split)

		# calling functions and giving them arguements
		dir_name = input("Enter Pornstar name: ")
		create_dir(dir_name)

		link = input("Enter PornPics link: ")
		get_links(link, links)
		download_images(dir_name,links)
	elif mode == "2":
		banner()
		print(split)
		print("Gallery Picker Mode (Press 99 When You Are Done)")
		print(split)

		dir_name = input("Enter Pornstar name: ")
		create_dir(dir_name)

		# links are inputed in a loop
		gallery_picker()
		download_images(dir_name, links)
	else:
		print(f"Error: Mode {mode} doesn't exist")


# and finally main
main()
