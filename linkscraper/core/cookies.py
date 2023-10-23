#!/usr/bin/python3

import requests, time

from utils.utils import *

from layout.table import Table

def get_cookies(url, filter_data=None):
    start_time = time.time()
    response = requests.get(url)
    
    Table.header([
        ("Name", "cyan", True),
        ("Value", "white", False)
    ])
    
    cookie_dict = response.cookies.get_dict()
    
    if filter_data:
        cookie_dict = {k: v for k, v in cookie_dict.items() if find(k, filter_data)}

    for name, value in cookie_dict.items():
        Table.row(name, value)

    end_time = "{:.2f}".format(time.time() - start_time)
    Table.caption(f"Total of cookies on page: {len(cookie_dict)} - Time taken: {end_time} seconds")
    Table.display()
