import re

file = open('w_data (5).dat', 'r') #Opens the file

file = file.read() #Reads the file

weather_num = re.findall(r"[-+]?\d*\.\d+|\d+", file) #Finds all the numbers in the list and appends to list
del weather_num[0:2]#Removes the 2002 and extra 1
day_number = 0 #Variable to store day number from 1st colomn
temp_spread = 100 #Variable to store difference between column 2 and 3
for num in range(0, 30): #30 Days needs a range of 30
    day_index = 0 #Index to find where the day_number is
    day_index += num*14
    if num >= 9: #Add one to ignore the 1st HDD Variable
        day_index +=1
    if num >= 14: #Add one to ignore the 2nd HDD Variable
        day_index +=1
    if num >= 15: #Add one to ignore the 3rd HDD Variable
        day_index +=1
    temp_diff = int(weather_num[day_index+1]) - int(weather_num[day_index+2]) #+1 Since max_temp is always right after day_number and +2 since min_temp is always two after day_number
    if temp_diff < temp_spread: #If theres a new min temp_spread I replace the old one with the new one and update the day_number variable
        temp_spread = temp_diff 
        day_number = weather_num[day_index]
print ("Day " + day_number + " Temp spread " + str(temp_spread))
