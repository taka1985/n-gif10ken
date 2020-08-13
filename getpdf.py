from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
import urllib.error
import urllib.request


base_url = 'https://n-gif10ken.com/'


def main():
    download_pdfs()


def download(url, path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
        with open(path, mode='wb') as local_file:
            local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def download_pdfs():
    pdf_url= base_url + 'materials/159540942046901.pdf'
    download(pdf_url, './dist/pdf/janru.pdf')


if __name__ == '__main__':
    main()
