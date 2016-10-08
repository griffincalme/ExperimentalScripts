#I was waiting in line at the secretary of state. The staff call out the last 4 digits of your phone number when it is your turn.
#There are currently 40 people in line.
#What is the probability that, when a number is called, two or more people will have the same number?
#Assuming that each number has an equal probability.
#This runs a monte carlo simulation because I am lazy and my computer is not.


import random
import matplotlib.pyplot as plt
import time

start = time.clock()

def rollnumber(times_to_roll):
   list = []
   for x in range(0,times_to_roll):
       list.append(random.randint(0,9999))
   return list


def check_for_copy_of_first(list):
    first = list[0]
    truth = first in list[1:]
    return truth

truth_list = []
prob_list = []

for i in range(0,500000):
    roll = rollnumber(40)
    same_num = check_for_copy_of_first(roll)
    truth_list.append(same_num)
    prob = sum(truth_list)/len(truth_list)
    prob_list.append(prob)
    if i % 5000 == 0:
        print(' ')
        print(prob)
        print('iteration:' + str(i))

end = time.clock()
print('took ' + str(end) + ' seconds')

plt.xkcd()
plt.plot(prob_list)
plt.ylabel('Probability')
plt.xlabel('Trial')
plt.suptitle('Probability that two people will respond when the last 4 digits of a phone number are called')
plt.show()

