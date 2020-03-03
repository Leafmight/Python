import numpy as np
filename = './befkbhalderstatkode.csv'
import matplotlib.pyplot as plt
from collections import OrderedDict

dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}


def getPopPerHood(hood):
    deezMask = (dd[:,0] == 2015) & (dd[:,1] == hood)
    return np.sum(dd[deezMask][:,4])
def getList():
    lst = {}
    for key, value in neighb.items():
        lst.update({value: getPopPerHood(key)})
    return lst

print("Exercise 3:\n", getList())

def displayPlotOfHoodsPop():
    lst = getList()
    hoodsSorted = OrderedDict(sorted(lst.items(), key=lambda x: x[1]))
    cityAreas = []
    sumOfPeople = []
    for key, value in hoodsSorted.items():
        cityAreas.append(key)
        sumOfPeople.append(value)

    plt.bar(cityAreas, sumOfPeople, width=0.5, linewidth=0, align='center')
    title = 'Population in various areas in cph'
    plt.title(title, fontsize=12)
    plt.xticks(cityAreas, rotation=65)
    plt.tick_params(axis='both', labelsize=8)

    plt.show()

displayPlotOfHoodsPop()


def getOldPeople():
    deezMask = (dd[:,0] == 2015) & (dd[:,2] <= 65) 
    return np.sum(dd[deezMask][:,4])

print('Exercise 5',getOldPeople())
nordicCountryCodes = {5104: 'Finland', 5106: 'Island', 5110: 'Norge', 5120: 'Sverige'}

def getSumOfOldNordicPeople():
    lst = {}
    for key, value in nordicCountryCodes.items():
        lst.update({value: getOldNordicPeople(key)})
    return lst  

def getOldNordicPeople(countrycode):
    deezMask = (dd[:,0] == 2015) & (dd[:,2] <= 65) & (dd[:,3] == countrycode)
    return np.sum(dd[deezMask][:,4])

print("Exercise 6:\n", getSumOfOldNordicPeople())

specificHoods = {2: 'Østerbro', 4: 'Vesterbro/Kgs.'}
