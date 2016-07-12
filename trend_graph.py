import matplotlib.pyplot as plt
import csv
import numpy as np


num_plots=10
m=[1,2,3,4,5,6,7,8,9,10,11,12]
#colormap = plt.cm.Set1
#plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.5, num_plots)])
z=0
labels=[]
plt.gca().set_color_cycle(['r','g','b','y','k'])
y=input("Enter the year?")
cui=raw_input("Enter the cuisine: ")

file_name='Cui_'+cui+'_'+str(y)+'.csv'
plt.xlabel('Month')
plt.ylabel('Avg. Rating')
titl=cui+'_'+str(y%100)
plt.title(titl,y=1.08)
with open(file_name,'rb') as c1:
        f1=csv.reader(c1)
        for row in f1:
                if z==5 :
                        plt.legend(labels, ncol=2, loc='upper left', 
           bbox_to_anchor=[0.5, 1.1], 
           columnspacing=1.0, labelspacing=0.0,
           handletextpad=0.0, handlelength=2.5,
           shadow=True)

                        plt.show()
                        plt.xlabel('Month')
                        plt.ylabel('Avg. Rating')
                        #titl=cui+'_'+str(y%100)
                        plt.title(titl,y=1.08)
                        plt.plot(m,row,lw=2,marker='.',mew=2.5)
                        #plt.text(x,y,'a')
                        labels=[]
                        labels.append(r'$Cluster %i$'%z)

                elif z==9 :
                        plt.plot(m,row,lw=2,marker='.',mew=2.5)
                        labels.append(r'$Cluster %i$'%z)
                        plt.legend(labels, ncol=2, loc='upper left', 
           bbox_to_anchor=[0.5, 1.1], 
           columnspacing=1.0, labelspacing=0.0,
           handletextpad=0.0, handlelength=2.5,
           shadow=True)

                        plt.show()
                        
                else :
                        plt.plot(m,row,lw=2,marker='.',mew=2.5)
                        labels.append(r'$Cluster %i$'%z)
                z+=1
'''plt.legend(labels, ncol=2, loc='upper left', 
           bbox_to_anchor=[0.5, 1.1], 
           columnspacing=1.0, labelspacing=0.0,
           handletextpad=0.0, handlelength=2.5,
           shadow=True)

plt.show()'''

