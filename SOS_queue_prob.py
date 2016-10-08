#I was waiting in line at the secretary of state. The staff call out the last 4 digits of your phone number when it is your turn.
#There are currently 40 people in line. 
#What is the probability that, when a number is called, two or more people will have the same number?
#Assuming that each number has an equal probability.
#This runs a monte carlo simulation because I am lazy and my computer is not.


import random

def rollnumber(times_to_roll):
   list = []
   for x in range(0,times_to_roll):
       list.append(random.randint(0,9999))
   return list

#wrong
def check_same_number(list):
    truth = len(list) != len(set(list))
    return truth

#correct
def check_for_copy_of_first(list):
    first = list[0]
    truth = first in list[1:]
    return truth


truth_list = []

while True:
    roll = rollnumber(40)
    same_num = check_for_copy_of_first(roll)
    truth_list.append(same_num)
    print(sum(truth_list)/len(truth_list))



#I was wrong, the first function was the prob that any 2 ppl
#in the queue had the same number when a number is called

#I really want to know what the prob is that
#when a number is called, two or more people have THAT number.
#Then you can calculate based on the number of people they see
#in time period x, what the prob is of a conflict whithin
#period x
