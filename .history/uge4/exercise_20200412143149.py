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
east = {}
west = {}
years = {1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0, 2001: 0, 2002: 0,
       2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0,
       2014: 0, 2015: 0}

def getPopPerSpecificHood(year, hood):
    deezMask = (dd[:,0] == year) & (dd[:,1] == hood)
    return np.sum(dd[deezMask][:,4])

def getSumPerSpecificHoods():
    lst = []

    for ykey, yvalue in years.items():
        for hkey, hvalue in specificHoods.items():
            if(hkey == 2):
                east[ykey] = getPopPerSpecificHood(ykey, hkey)
            else:
                west[ykey] = getPopPerSpecificHood(ykey, hkey)

    lst.append(east)
    lst.append(west)
    return lst

print("Exercise 7:\n",getSumPerSpecificHoods())


def displayPopulationOverTheYears():
    getSumPerSpecificHoods() # Sørger for data til listerne east og west
 
    yearsToDisp = []
    eastpopulation = []
    westpopulation = []
 
    for key, value in years.items():
        yearsToDisp.append(key)
 
    for key, value in east.items():
        eastpopulation.append(value)
   
    for key, value in west.items():
        westpopulation.append(value)
 
    # plt.figure()
 
    p1 = plt.plot(yearsToDisp, eastpopulation, linewidth=2, color='red')
    
    p2 = plt.plot(yearsToDisp, westpopulation, linewidth=2, color='green')
    plt.legend([p1, p2],['eastpop','westpop'],loc=1) 
    plt.title("Population over the years", fontsize=18)
    plt.xlabel("Year", fontsize=10)
    plt.xticks(yearsToDisp)
    plt.tick_params(axis='both', labelsize=10)
    plt.show()

displayPopulationOverTheYears()