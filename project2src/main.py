from helper_function_main import *
import pandas as pd
from KNN import *
from forward_selection import *
from backward_elimination import *


#Version Python3

#Welcome Message
print_welcome_message()

# Grab the file based on user input
file_name = input('Type in the name of the file you want to test: ')
# file_name='cs_170_small45.txt'

#Load Data
data = pd.read_csv(file_name,sep="  ",header=None,engine='python')

num_col = len(data.columns)
num_rows = len(data.index)

#Ask User for which Algorithm
answer=get_user_input()


print('\nThis dataset has '+str(num_col-1)+' features (not including the class attribute) with ' + str((num_col-1)*num_rows) +' instances.')

#Convert every cell into float
for idx in range(1,num_col):
    data.loc[:,idx] = pd.to_numeric(data.loc[:,idx],errors='coerce')

print('\nPlease wait while I normalize the data...   Done!\n')

#Normalize the data
for idx in range(1,num_col):
    #Find Column Mean
    col_mean = pd.Series.mean(data.loc[:,idx])

    #Find Column Std
    col_std = pd.Series.std(data.loc[:,idx])

    #Replace with normalized data
    for i in range(0,num_rows):
        val = data.loc[i,idx]
        normalized_value = (val-col_mean)/col_std
        data.loc[i,idx] = normalized_value

accuracy=compute_accuracy(leave_one_out_validation(data))
print('Running nearest neighbor with all '+str(num_col-1)+' features, using "leave-one-out" evaluation, I get an accuracy of '+str(accuracy*100)+'%\n')


if answer==1:

    forward_selection_algorithm(data,num_col)
elif answer==2:

    backward_elimination_algorithm(data,num_col)
elif answer==3:

    backward_elimination_algorithm(data,num_col)
    forward_selection_algorithm(data,num_col)
else:
    exit()
