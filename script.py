import requests
from bs4 import BeautifulSoup
import re
import os


def fix_all_html(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'index.html':
                file_path = os.path.join(root, file)
                fix_html(file_path)

def fix_html(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    a_tags = soup.find_all('a', href=True)

    for a in a_tags:
        href = a['href']
        if href[84:88] == '/tag':
            a['href'] = href[84:]

    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def main():
    fix_all_html(".")

if __name__ == '__main__':
    main()