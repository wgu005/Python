import re

file = open('soccer.dat', 'r') #Opens the file

file = file.read() #Reads the file

soccer_num = re.findall(r"[-+]?\d*\.\d+|\d+", file) #Finds all the soccer_num in the list and appends to list
soccer_team = re.findall(r"[A-Za-z-_]+ ",file)
del soccer_team[0:7]
for x in range(0,20): #Remove everything but the team names
    letter_index = 0
    letter_index += x
    soccer_team.pop(letter_index+1)
team_num = 0
point_diff = 100000
for num in range(0, 20): #20 teams needs a range of 20
    team_index = 0
    team_index += num*8
    #print(soccer_num[team_index])
    temp_diff = abs(int(soccer_num[team_index+5]) - int(soccer_num[team_index+6]))
    if(temp_diff < point_diff): #Finding the smallest absolute difference in points
        point_diff = temp_diff
        team_num = soccer_num[team_index]

print("TeamName: " + soccer_team[int(team_num)-1] + " Smallest Difference: " + str(point_diff))