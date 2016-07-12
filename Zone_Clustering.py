import csv
import numpy as np
import random
import math
import pylab as pl

fp1 = open("Tomato_db_sorted.csv", "rb")
fp2 = open("Tomato_db_sorted_Lat_Long.csv", "wb")

text = csv.reader(fp1, delimiter=',')
writer=csv.writer(fp2,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
for row in text:
    a=[row[6],row[7]]
    a.sort()
    writer.writerow(a)
fp1.close()
fp2.close()
