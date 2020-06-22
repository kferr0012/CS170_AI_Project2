from KNN import *
from backward_elimination import *
from forward_selection import *
from helper_function_main import *
import time
import matplotlib.pyplot as plt


#This file is used to build graphs for the code report

#Load Data
file_name1='cs_170_small45.txt'
file_name2='cs_170_large45.txt'
file_name3='kevin_dataset_small.txt'
file_name4='kevin_dataset_large.txt'

data1=pd.read_csv(file_name1,sep="  ",header=None,engine='python')
data2=pd.read_csv(file_name2,sep="  ",header=None,engine='python')
data3=pd.read_csv(file_name3,sep="  ",header=None,engine='python')
data4=pd.read_csv(file_name4,sep="  ",header=None,engine='python')

#Grab Dimensions
num_col1=len(data1.columns)
num_row1=len(data1.index)
num_cell1=(num_col1-1)*num_row1
print('Cells1: ' + str(num_cell1))

num_col2=len(data2.columns)
num_row2=len(data2.index)
num_cell2=(num_col2-1)*num_row2
print('Cells2: ' + str(num_cell2))

num_col3=len(data3.columns)
num_row3=len(data3.index)
num_cell3=(num_col3-1)*num_row3
print('Cells3: ' + str(num_cell3))

num_col4=len(data4.columns)
num_row4=len(data4.index)
num_cell4=(num_col4-1)*num_row4
print('Cells4: ' + str(num_cell4))



#Convert every cell into float
for idx in range(1,num_col1):
    data1.loc[:,idx] = pd.to_numeric(data1.loc[:,idx],errors='coerce')
for idx in range(1,num_col2):
    data2.loc[:,idx] = pd.to_numeric(data2.loc[:,idx],errors='coerce')
for idx in range(1,num_col3):
    data3.loc[:,idx] = pd.to_numeric(data3.loc[:,idx],errors='coerce')
for idx in range(1,num_col4):
    data4.loc[:,idx] = pd.to_numeric(data4.loc[:,idx],errors='coerce')


#Normalize the data
for idx in range(1,num_col1):
    #Find Column Mean
    col_mean = pd.Series.mean(data1.loc[:,idx])

    #Find Column Std
    col_std = pd.Series.std(data1.loc[:,idx])

    #Replace with normalized data
    for i in range(0,num_row1):
        val = data1.loc[i,idx]
        normalized_value = (val-col_mean)/col_std
        data1.loc[i,idx] = normalized_value
for idx in range(1,num_col2):
    #Find Column Mean
    col_mean = pd.Series.mean(data2.loc[:,idx])

    #Find Column Std
    col_std = pd.Series.std(data2.loc[:,idx])

    #Replace with normalized data
    for i in range(0,num_row2):
        val = data2.loc[i,idx]
        normalized_value = (val-col_mean)/col_std
        data2.loc[i,idx] = normalized_value
for idx in range(1,num_col3):
    #Find Column Mean
    col_mean = pd.Series.mean(data3.loc[:,idx])

    #Find Column Std
    col_std = pd.Series.std(data3.loc[:,idx])

    #Replace with normalized data
    for i in range(0,num_row3):
        val = data3.loc[i,idx]
        normalized_value = (val-col_mean)/col_std
        data3.loc[i,idx] = normalized_value
for idx in range(1,num_col4):
    #Find Column Mean
    col_mean = pd.Series.mean(data4.loc[:,idx])

    #Find Column Std
    col_std = pd.Series.std(data4.loc[:,idx])

    #Replace with normalized data
    for i in range(0,num_row4):
        val = data4.loc[i,idx]
        normalized_value = (val-col_mean)/col_std
        data4.loc[i,idx] = normalized_value


#Run algorithms and record time

#Collecting data for cs_170_small45.txt Forward Selection
x1=[]   #num_cell
y1=[]   #times
for i in range(5):
    x1.append(num_cell1)
    start_time=time.time()
    forward_selection_algorithm(data1,num_col1)
    end_time=time.time()
    y1.append(end_time-start_time)


#Collecting data for cs_170_small45.txt Backward Elimination
x2=[]   #num_cell
y2=[]   #times
for i in range(5):
    x2.append(num_cell1)
    start_time=time.time()
    backward_elimination_algorithm(data1,num_col1)
    end_time=time.time()
    y2.append(end_time-start_time)

#Collecting data for cs_170_large45.txt Forward Selection
x3=[]   #num_cell
y3=[]   #times
for i in range(5):
    x3.append(num_cell2)
    start_time=time.time()
    forward_selection_algorithm(data2,num_col2)
    end_time=time.time()
    y3.append(end_time-start_time)

#Collecting data for cs_170_large45.txt Backward Elimination
x4=[]   #num_cell
y4=[]   #times
for i in range(5):
    x4.append(num_cell2)
    start_time=time.time()
    backward_elimination_algorithm(data2,num_col2)
    end_time=time.time()
    y4.append(end_time-start_time)

#Collecting data for kevin_dataset_small.txt Forward Elimination
x5=[]
y5=[]
for i in range(5):
    x5.append(num_cell3)
    start_time=time.time()
    forward_selection_algorithm(data3,num_col3)
    end_time=time.time()
    y5.append(end_time-start_time)

#Collecting data for kevin_dataset_small.txt Backward Elimination
x6=[]
y6=[]
for i in range(5):
    x6.append(num_cell3)
    start_time=time.time()
    backward_elimination_algorithm(data3,num_col3)
    end_time=time.time()
    y6.append(end_time-start_time)


#Collecting data for kevin_dataset_large.txt Forward Selection
x7=[]
y7=[]
for i in range(5):
    x7.append(num_cell4)
    start_time=time.time()
    forward_selection_algorithm(data4,num_col4)
    end_time=time.time()
    y7.append(end_time-start_time)

#Collecting data for kevin_dataset_large.txt Forward Selection
x8=[]
y8=[]
for i in range(5):
    x8.append(num_cell4)
    start_time=time.time()
    backward_elimination_algorithm(data4,num_col4)
    end_time=time.time()
    y8.append(end_time-start_time)








#Display Graph
plt.scatter(x1,y1,label='Forward Selection',color='blue',marker='*',s=30)
plt.scatter(x2,y2,label='Backward Elimination',color='red',marker='*',s=30)
plt.scatter(x3,y3,label='Forward Selection',color='blue',marker='*',s=30)
plt.scatter(x4,y4,label='Backward Elimination',color='red',marker='*',s=30)
plt.scatter(x5,y5,label='Forward Selection',color='blue',marker='*',s=30)
plt.scatter(x6,y6,label='Backward Elimination',color='red',marker='*',s=30)
plt.scatter(x7,y7,label='Forward Selection',color='blue',marker='*',s=30)
plt.scatter(x8,y8,label='Backward Elimination',color='red',marker='*',s=30)
plt.xlabel('Number of Cells')
plt.ylabel('Time in Seconds')
plt.legend()
plt.show()
