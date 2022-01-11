import itertools
import numpy as np

n = 10  # number of years
initialprob = list(range(0, 101, round(100 / (n - 1))))  # initialize the probability for each year
yearlyprobabilitylist = [x / 100 for x in
                         initialprob]  # divide by 100 to get actual probabilities since range is only for integers
yearlyprobabilitylist[0] += 0.05
yearlyprobabilitylist[len(yearlyprobabilitylist) - 1] -= 0.05
print(yearlyprobabilitylist)
lst = list(
    itertools.product([0, 1], repeat=n))  # create all permutations of break and non-break for the given no. years
#print(lst)

probabilitylist = []  # create a blank probability list - this is a list for the probability of each scenario
breakdownsno = []  # this creates a blank list that will correspond to the number of breakdowns of each scenario
# for example, 0, 0, 1, will add a 1 to this list, while 1, 1, 1, will add a 3 to this list
for element in lst:  # for loop to go through each scenario
    newlist = []  # creates a new list that will hold the probability of each individual outcome within the scenario
    # so for the scenario 0, 0, 1, this will create a list with the probability of "no break", "no break", and "break"
    breakdownsno.append(sum(element))  # adds the number of breakdowns to the breakdownsno list
    breakdownssofar = 0  # tracks breakdowns so far
    for x in element:  # for each outcome within a scenario
        age = 0  # used to track the index of each element within each scenario
        if (x == 1):  # if the outcome is a breakdown
            newlist.append(yearlyprobabilitylist[age])  # finds the probability of breakdown corresponding to index
            age = 0
        else:
            newlist.append(
                1 - yearlyprobabilitylist[age])  # finds 1-probability of breakdown corresponding to index
            age += 1  # increases counter because moving on to the next index
    probability = np.prod(np.array(newlist))  # multiplies all probabilities of each outcome within each scenario
    probabilitylist.append(probability)  # adds that probability to the container

products = [a * b for a, b in zip(breakdownsno, probabilitylist)]  # uses a elementwise multiplication of the two lists
# (probability * number of breakdowns), which creates a weighted average probability of each element
print(products)
breakdowns = sum(products)  # sums weighted average to get to the number of expected breakdowns
print("The homeowner can expect", round(breakdowns,2), "breakdowns over ", n, "years")

probdic = {}  # creates a dictionary
for key, val in zip(breakdownsno, probabilitylist):
    probdic[key] = probdic.get(key, 0) + val
print("The distribution of breakdowns is as follows", probdic)
