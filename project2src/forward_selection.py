from KNN import *

#This function takes data as a parameter
def forward_selection_algorithm(given_df,cols):
    best_accuracy=0
    best_combination=None #List of Features
    current_combination=[]
    current_accuracy=None
    local_max_accuracy=0
    local_max_combo=None
    frontier_combinations=[]
    next_combination=[]
    num_col = cols
    df_copy=copy.copy(given_df)

    #List of col indexes
    list_of_col_indexes=[]

    #First level of combinations
    for i in range(1,num_col):
        dummy_list=[]
        dummy_list.append(int(i))
        list_of_col_indexes.append(int(i))
        frontier_combinations.append(dummy_list)

    # print(frontier_combinations)
    # print(list_of_col_indexes)

    print('Beginning Search.\n')

    while len(current_combination)!=(num_col-1):
        #Compute the accuracy of each combination
        for combo in frontier_combinations:
            current_combination=combo
            df_copy=carve_df(df_copy,current_combination)
            accuracy=compute_accuracy(leave_one_out_validation(df_copy))
            df_copy=copy.copy(given_df)

            print('\t Using feature(s) ',end='')
            print(current_combination,end='')
            print(' accuracy is ' + str(accuracy*100) + '%')

            if accuracy > local_max_accuracy:
                local_max_accuracy=accuracy
                next_combination=current_combination

            if accuracy > best_accuracy:
                best_accuracy=accuracy
                best_combination=current_combination

        #Check if limit reached
        if len(current_combination)==(num_col-1):
            break

        if local_max_accuracy < best_accuracy:
            print('\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)')

        #Empty Out frontier and make new frontier
        frontier_combinations=[]
        copy_next_combo=copy.copy(next_combination)
        print('\nFeature set: ',end=' ')
        print(next_combination,end='')
        print(' was best, accuracy is ' + str(local_max_accuracy*100) + '%\n')

        for i in list_of_col_indexes:
            if i not in next_combination:
                copy_next_combo.append(i)
                frontier_combinations.append(copy_next_combo)
                copy_next_combo=copy.copy(next_combination)

        #Empty out local_max_combo and local_max_accuracy
        local_max_combo=None
        local_max_accuracy=0

    print('\nFinished Search!! The best feature subset is ',end='')
    print(best_combination,end='')
    print(', which has an accuracy of ' + str(best_accuracy*100)+'%\n')
