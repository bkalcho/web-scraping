#!/usr/bin/env python
__author__ = 'kalcho'

import csv

csv_file = open("test.csv", "w+")
try:
    writer = csv.writer(csv_file)
    writer.writerow(("number", "number plus 2", "number times 2"))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csv_file.close()