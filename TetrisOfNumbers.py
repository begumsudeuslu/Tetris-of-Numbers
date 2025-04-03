import sys

#First step, we take input file and turns from txt to list.
def read_file(file_name):
    file_name= "input_as3.txt"
    all_list=[]
    with open(file_name, 'r') as f:
        for line in f:
            numbers=[int(num) for num in line.strip().split(" ")] 
            all_list.append(numbers)
    return all_list     #Return as list.


#If the list has empty row (or while during run this code, created empty row) this function remove that.
def del_empty_row(list):
   return [row for row in list if len(row)>0]


#If the list has empty column (or while during run this code, created empty column) this function remove that.
def del_empty_col(list):
    empty_cols= []
    for i in range(len(list[0])):
        flag = True
        for row in list:
            if row[i]!=" ":
                flag = False
                break
        if flag:
            empty_cols.append(i)
    
    for i in reversed(empty_cols):
        for row in list:
            del row[i]        
            
    return list


#This function check the input values of row and column.
"""If inputs are true, the codes run or function return True."""
def is_valid(i,j, list):
    return 0 <= i < len(list) and 0 <= j < len(list[0])


#This function change the numbers. and put sace instead of numbers. And this function do that for every contact numbers.
"""In this step we delete numbers which we have chosen and contact each other.
If chosen number and contact number equal, delete and put space instead of numbers.
And also this function return score as second. This score is sum of the all deleted number."""
def add_space(row, col, current_number, current_list,score):
    if current_list[row][col] == current_number:
        current_list[row][col] = " "
        score+= int(current_number)
        for pos_i, pos_j in [(-1, 0), (1, 0), (0, 1), (0,-1)]: 
            contact_number_i = row +  pos_i
            contact_number_j = col +  pos_j
                
            if is_valid(contact_number_i, contact_number_j, current_list):
                current_list, score= add_space(contact_number_i, contact_number_j, current_number, current_list, score)
                #This will continue for every contact numbers until not equal anymore.
                
    return current_list, score
                            
                            
#This function shifts the numbers in the column down.
"""Numbers and spaces in each column are appended to the empty list.
The numbers and spaces in this list are also appended sequentially to another new list.
First spaces are appended then numbers, because the numbers need to fall down. 
Final step is that we set the sorted list equal to columns."""
def drop_function(list):
    for j in range(len(list[0])):
        item_list= []  
        for i in range(len(list)):
            item_list.append(list[i][j])  #Firsly, we add all item in every column.
        
        number_list=[]
        for _ in range(item_list.count(" ")):   #Then add as many spaces as there are in the item_list.
            number_list.append(" ")
        
        for item in item_list:
            if item != " ":
                number_list.append(item)   #Finally, we add just the numbers, thus numbers stay last.
        
        for i in range(len(list)):
            list[i][j]=number_list[i]    #And replace the elements in the list.
    
    list = del_empty_row(list)   #Delete empty row.
    list = del_empty_col(list)   #Delete empty column.
            
    return list   #Again return changed list.


#Checks whether the game continues or not.
"""If there are at least two same numbers next to each other or under each other, the game continues.""" 
def game_over(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            current_number= list[i][j]
            if current_number!=" ":   #Go numbers not space.
                if j < len(list[0])-1 and current_number== list[i][j+1]:
                    return True
                if i < len(list)-1 and current_number==list[i+1][j]:
                    return True
    
    return False    #If you have no same numberes anymore, return false.


#This function print current list.
def print_list(list):
    list_str=[[str(num) for num in row] for row in list]
    arrange_list= '\n'.join([' '.join(row) for row in list_str])
    print(arrange_list)
    return arrange_list 

file_name= (sys.argv[1])      #We take a input txt from user.                   

current_list=read_file(file_name)   #Turn txt to list with this read_file function.

print_list(current_list)     #At the beginning print your input list.

total_score=0       #At the beginning your score is 0.

print(f"Score is {total_score}")    #And print your score also.

#Thanks to this loop, input is received from the user until the game ends.
"""This loop run until game_over function return False.
And we will continue and change the list until end of game."""
while game_over(current_list):
    
    #We take input.
    user_input= input("Please enter a row and a column number: ")
    input_list= [int(num) for num in user_input.strip().split(" ")]   
    x,y= input_list[0],input_list[1]
    
    #Check the input index. If indexes are True continue.
    if is_valid(x-1,y-1,current_list):
        score=0   #beginning score is 0
        current_number=current_list[x-1][y-1]
        
        #We turn to list and add space instead of numbers.
        changed_list, new_score= add_space(x-1, y-1,current_number ,current_list,score)
        
        #And change list again and drop the numbers.
        changed_list= drop_function(changed_list)
        
        #Also add score to total_score.
        total_score+=new_score
        
        #Print your changed list.
        print_list(changed_list)
        
        #Also print your total score.
        print(f"Your score is: {total_score}")
        
        #And update your list again.
        current_list= changed_list
    
    #If ypur input is wrong, print that and go to beginning of loop.    
    else:
        print("Please enter a correct size!")
        continue
   
#If exit from loop, print Game over.  
print("Game over")