import csv

cui=raw_input("Enter the cuisine: ")

id100=[]
#id1000=[]
#id10000=[]
file_name=cui+'intersection_plot.csv'
with open(file_name,'rb') as c:
    f=csv.reader(c)
    for row in f:
        if (float(row[1])*10>=1) & (float(row[1])*10<10.0):
            id100.append([row[0]+','+str(float(row[1])*10)+','+row[2]+','+row[3]+','+str(10)])
        elif (float(row[1])*100>=1) & (float(row[1])*100<10.0):
            id100.append([row[0]+','+str(float(row[1])*100)+','+row[2]+','+row[3]+','+str(100)])
        elif (float(row[1])*1000>=1) & (float(row[1])*10<1000.0):
            id100.append([row[0]+','+str(float(row[1])*1000)+','+row[2]+','+row[3]+','+str(1000)])
with open('final'+file_name,'ab') as f1:
            writeitt = csv.writer(f1)
            writeitt.writerows(id100)
