#!/usr/bin/python3

import requests, time, json

from rich.json import JSON

from layout.table import Table
from layout.layout import Layout

from utils.date_time import DateTime

class Headers:

    @classmethod
    def is_json(cls, string):
        try:
            if json.loads(string):
                return True
                
            return False
        
        except ValueError as e:
            return False

    @classmethod
    def get_headers(cls, url, filter_data=None):
        start_time = time.time()

        response = requests.get(url)
        headers_dict = response.headers

        if filter_data:
            headers_dict = {k: v for k, v in headers_dict.items() if k.find(filter_data)}
        
        Table.header([
            ('Name', 'cyan', True),
            ('Value', 'white', False)
        ])

        for header_name, header_value in headers_dict.items():
            formatted_value = JSON(header_value) if cls.is_json(header_value) else header_value
            Table.row(header_name, formatted_value)

        Table.caption(f'Total of headers: {len(headers_dict)} - '
                      f'Time taken: {DateTime.calculate_interval(start_time)} seconds')
        
        Table.display()

    @classmethod
    def section(cls, url, filter_data):
        Layout.header_section('Headers')
        cls.get_headers(url, filter_data)
