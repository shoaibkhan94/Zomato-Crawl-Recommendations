import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime
import operator
import os
import collections

z=input("Enter the cluster no. : ")
y=input("Enter the year?")
cui=raw_input("Enter the cuisine: ")
    

id=[]
with open(r'clustersDivision_of_Restaurants_clu_wise.csv','rb') as c:
    f=csv.reader(c)
    for row in f:
        if int(row[2])==z :#for cluster z
            id.append(int(row[3]))
#print id
print len(id)

c.close()
s=set(id)
id1=[]
date=[]
i=0
with open(r'Kolkata_Reviews_Data_Cleaned.csv','rb') as c:
    f=csv.reader(c)
    for row in f:
        #print row[4]
        if int(row[4]) in s:
            #print row[4]
            if row[8].endswith(str(y)) :
                if row[6].find(cui)!=-1 :
                    id1.append(row[4])
                    try:
                        date.append(datetime.datetime.strptime(row[8],"%d/%m/%Y"))
                    except:
                        date.append(datetime.datetime.strptime(row[8],"%d-%m-%Y"))
                    with open(r'temp.csv','ab') as c1:
                        f1=csv.writer(c1)
                        f1.writerow([row[4],row[7],int(date[i].month)])
                        i+=1
        else:
            continue
#print id1
print len(id1)

c.close()
c1.close()

id2=[]
id2=id1.sort()
counter=collections.Counter(id1)
#print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
#print(counter.values())
# [4, 4, 2, 1, 2]
#print(counter.keys())
# [1, 2, 3, 4, 5]
li=counter.most_common(5)
print(counter.most_common(5))
# [(1, 4), (2, 4), (3, 2)]
os.remove('temp.csv')

'''with open(r'Tomato_db_sorted.csv','rb') as x:
    fr=csv.reader(x)
    for rows in x:
        cells=rows.split(",")
        if cells[1] in li:
            print cells[0]'''
