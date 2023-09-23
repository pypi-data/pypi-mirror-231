#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


class CsvUtils:

    def __init__(self, csv_file_path=None):
        self.csv_file_path = csv_file_path

    def reader(self):
        """
        对csv进行读取操作，结果以list形式返回
        @return:
        """
        tem_list = []
        with open(self.csv_file_path, 'r', encoding='utf-8')as f:
            read = csv.reader(f)
            for i in read:
                tem_list.append(i)
        return tem_list

    def write_csv_by_list(self, headers, rows):
        """
        写入csv,列表形式
        @param headers: 列标题列表,example:['class', 'name', 'sex', 'height', 'year']
        @param rows: 行数据列表,example:[[1, 'xiaoming', 'male', 168, 23],[1, 'xiaohong', 'female', 162, 22]]
        @return:
        """
        try:
            with open(self.csv_file_path, 'w', encoding='utf-8', newline='')as f:
                write = csv.writer(f)
                write.writerow(headers)
                write.writerows(rows)
        except Exception as e:
            raise e

    def write_csv_by_dict(self, headers, rows):
        """
        写入csv,字典形式
        @param headers: 列表标题, eg. ['class', 'name', 'sex', 'height', 'year']
        @param rows:行数据列表,eg. [{'class': 1, 'name': 'xiaoming', 'sex': 'male', 'height': 168, 'year': 23}]
        @return:
        """
        try:
            with open(self.csv_file_path, 'w', encoding='utf-8', newline='') as f:
                write = csv.DictWriter(f, headers)
                write.writeheader()
                write.writerows(rows)
        except Exception as e:
            raise e
