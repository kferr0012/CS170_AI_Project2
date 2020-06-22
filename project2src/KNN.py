#Source=https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
# ^ used only for Nearest Neighbor
from math import sqrt
from helper_function_main import *
import copy

dummy_list=[]
type_list=type(dummy_list)


#Good
# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(1,len(row1)):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

#Get Neighbor function
def get_neighbors(train, test_row, num_neighbors):
	distances = []
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = []
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

#Make predictions function
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[0] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

#Implement Leave One Out Validation
#Iterate through the rows and Check the accuracy
#Returns [correct_count,incorrect_count]
def leave_one_out_validation(dataframe):
    #Check type of dataframe
    #The KNN code expects data to be in list of lists format

    #Convert Dataframe to list of list
    if type(dataframe)==type_list:
        list_df=copy.copy(dataframe)
    else:
        list_df=copy.copy(convert_df_to_list_of_lists(dataframe))

    correct_count=0
    incorrect_count=0
    output_list=[]
    backup_data = copy.copy(list_df)

    for row in list_df:
        #Remove and Predict Class
        excluded_row=copy.copy(row)
        new_list_df=remove_list_from_list_of_list(backup_data,excluded_row)
        prediction=predict_classification(new_list_df,excluded_row,1)

        #Check if prediction was correct or not
        if prediction==excluded_row[0]:
            correct_count+=1
        else:
            incorrect_count+=1

        #Reset the data
        backup_data=copy.copy(list_df)

    output_list.append(correct_count)
    output_list.append(incorrect_count)
    return output_list
