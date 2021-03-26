#!/usr/bin/python3

#imports
import argparse
from webbrowser import open as openvideo
from urllib.request import urlopen as openpage
from re import findall as findvideos

#setup the parser object
parser = argparse.ArgumentParser()
parser.add_argument('search_term', help='Enter the term to search')
parser.add_argument('-n','--number', type=int, default=1, help='Open the nth video')

#parse arguments and assign to variables
args=parser.parse_args()
search_term = args.search_term.replace(" ","+")
n = args.number

#open the search page
page = openpage("https://www.youtube.com/results?search_query=" + search_term)

#get a list of video IDs
videoIDs = findvideos(r"watch\?v=(\S{11})", page.read().decode())

#get ID of video that needs to be watched
video_to_watch = "https://www.youtube.com/watch?v=" + videoIDs[n-1]

#open in browser
openvideo(video_to_watch)

'''
Mini project 1:
Python can be used to make CLIs (command line interfaces). Let's start simple. Make a CLI program in python that accepts a string, 
searches youtube for that string, and opens the first result in a browser.

For example, you should be able to run the program as "python ytsearch.py numberphile" 
and it searches youtube for "numberphile" and opens the first one in the list

Bonus points for:
- A help page that is printed with python ytsearch.py -h 
- Being able to run the code as ytsearch.py numberphile or ytsearch numberphile
- An optional argument n that allows choosing which result to open. 
  Eg. something like python ytsearch -n 4 numberphile should open the 4th video that appears when searching "numberphile"
'''
