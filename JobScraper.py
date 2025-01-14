import requests
from bs4 import BeautifulSoup
import csv

#this script will pull jobs from linkedin maching my search
url = 'https://www.linkedin.com/search/results/all/?keywords=devops%20developer&origin=GLOBAL_SEARCH_HEADER&sid=G4e'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
