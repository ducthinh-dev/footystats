import requests
from urllib.parse import urlencode
import pandas as pd

class googleSearcher():
    def __init__(self):
        self.url = 'https://www.googleapis.com/customsearch/v1?'
        self.key = 'AIzaSyCbJp4viv2OZNdvBKPEQGsywZAsHzANyY4'
        self.cx = '345e90d52ee3f4337'

    def searchKeyword(self, keyword='sample', siteSearch=None):
        params = {
            'key': self.key,
            'cx': self.cx,
            'q': keyword
        }
        if siteSearch:
            params['siteSearch'] = siteSearch
        url = self.url + urlencode(params)
        results = requests.get(url=url).json()['items']
        return results


        