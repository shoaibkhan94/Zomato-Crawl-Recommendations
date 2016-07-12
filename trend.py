import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime
import operator
import os

y=input("Enter the year?")
cui=raw_input("Enter the cuisine: ")

id=[]
with open(r'clustersDivision_of_Restaurants_clu_wise.csv','rb') as c:
    f=csv.reader(c)
    for row in f:
        if int(row[2])==0 :#for all clusters
            id.append([row[3]])
#print id
#print len(id)

c.close()

id1=[]
date=[]
i=0
with open(r'Kolkata_Reviews_Data_Cleaned.csv','rb') as c:
    f=csv.reader(c)
    for row in f:
        if row[8].endswith(str(y)) :
            if row[6].find(cui)!=-1 :
                id1.append([row[4]])
                try:
                    date.append(datetime.datetime.strptime(row[8],"%d/%m/%Y"))
                except:
                    date.append(datetime.datetime.strptime(row[8],"%d-%m-%Y"))
                with open(r'temp.csv','ab') as c1:
                    f1=csv.writer(c1)
                    f1.writerow([row[4],row[7],int(date[i].month)])
                    i+=1

#print id1
print len(id1)

c.close()
c1.close()


thedata=[]
with open(r'temp.csv', 'rb') as f:
    readit = csv.reader(f)
    for row in readit:
        thedata.append([row[0],row[1],int(row[2])])
    thedata.sort(key=operator.itemgetter(2))
with open(r'temp.csv', 'wb') as f:
    writeit = csv.writer(f)
    writeit.writerows(thedata)


'''with open(r'temp.csv', 'rb') as f:
    readit = csv.reader(f)
    for row in readit:
        print row'''
                    

months=[1,2,3,4,5,6,7,8,9,10,11,12]
month_tot=[0,0,0,0,0,0,0,0,0,0,0,0]
month_freq=[0,0,0,0,0,0,0,0,0,0,0,0]
month_avg=[0,0,0,0,0,0,0,0,0,0,0,0]

tot=0
freq=0
i=0


with open(r'temp.csv','rb') as c1:
    f1=csv.reader(c1)
    for row in f1:
        month_tot[int(row[2])-1]+=float(row[1])
        month_freq[int(row[2])-1]+=1
    
print month_tot
print month_freq

i=0
while i<12:
    if month_freq[i]==0 :
        month_avg[i]=0.0
    else:
        month_avg[i]=round(month_tot[i]/month_freq[i],2)
    i+=1
print month_avg



plt.xlabel('Month')
plt.ylabel('Avg. Rating')
plt.title('AllClus'+cui+' '+str(y))
plt.axis([1,12,0,5])
plt.plot(months,month_avg)
plt.savefig('AllClus'+cui+'_'+str(y)+'.png')
os.remove('temp.csv')
plt.show()


