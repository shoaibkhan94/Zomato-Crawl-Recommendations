import os
import csv

cui=raw_input("Enter the cuisine: ")
id=[]
id1=[]
with open(r'ratio_file_sortedM.csv','rb') as c:
    f=csv.reader(c)
    for row in f:
        if row[1]==cui:
            id.append(row[0])
            id1.append(float(row[2]))
        else:
            continue
print len(id)
print len(id1)
print id[0:10]
print id1[0:10]

i=0
j=0
id3=[None]*39350
k=0
with open(r'position.csv','rb') as c1:
    f1=csv.reader(c1)
    for row in f1:
        if row[0].startswith('I#'):
            i=0
            try:
                j=id.index(row[0])
            except:
                j=39351
            print k
            k+=1
            while i<39350:
                if i==j:
                    id3[i]=row[1]+','+row[2]
                    i+=1
                    break
                else:
                    i+=1


print len(id3)
print id3[0:100]

i=0
id4=[]
while i<39350:
    id4.append([id[i]+','+str(id1[i])+','+id3[i]+','+str((i*10)/39350)])
    i+=1
file_name=cui+'intersection_plot.csv'
with open(file_name,'ab') as f1:
    writeitt = csv.writer(f1)
    writeitt.writerows(id4)
