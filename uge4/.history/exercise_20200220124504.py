import numpy as np
filename = './befkbhalderstatkode.csv'

dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def pop(hood):
    hood_mask = (dd[:,0] == 2015) & (dd[:,1] == hood)
    return np.sum(dd[hood_mask][:4])

def getSumPerHood():
    lst = {}
    for key, value in neighb.items():
        lst.update({value: pop(key)})
    return lst

print("Exercise 2:\n", getSumPerHood())