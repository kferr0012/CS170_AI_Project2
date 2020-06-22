import pandas as pd
import copy

#Good
def convert_df_to_list_of_lists(df):
    #Assumes a copy is being passed through
    output_list=df.values.tolist()
    return output_list

def remove_list_from_list_of_list(list_of_lists,target_list):
    #This function returns a new list of lists
    #excluding the target list
    #Assumes a copy is being passed through
    list_of_lists.remove(target_list)
    return list_of_lists


#Good
def compute_accuracy(given_list):
    return given_list[0]/(given_list[0]+given_list[1])

#Good
#Takes df as parameter and indices of rows to remove
def remove_columns_by_index(df,idx_list):
    #send indices to list and make them in descending order
    #assumes copy being passed through
    index_list=[]
    for value in idx_list:
        index_list.append(value)
    index_list.sort(reverse=True)

    for col in index_list:
        df=df.drop(col,axis=1)

    return df

#Good
#Input Dataframe and which column indexes to extract
def carve_df(df,index_subset_list):
    col_list=[]
    num_col=len(df.columns)

    for i in range(1,num_col):
        col_list.append(i)


    new_list=list(set(col_list)-set(index_subset_list))


    df_copy=copy.copy(df)
    df_copy=remove_columns_by_index(df_copy,new_list)
    return df_copy

def print_welcome_message():
    print("Welcome to Kevin Ferrer's Feature selection algorithm.")

def get_user_input():
    print('Type the number of the algorithm you want to run.\n')
    print('\t1) Forward Selection')
    print('\t2) Backward Elimination\n')
    input_value=input()
    return int(input_value)
