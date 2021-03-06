import numpy as np
filename = './befkbhalderstatkode.csv'

dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def pop(aar=dd[:,0], bydel=dd[:,1], alder=dd[:,2], statkode=dd[:,3]):
    hood_mask = (dd[:,0] == 2015) & (dd[:,1] == neighb[:,0])
    print(np.sum(dd[hood_mask][:4]))

pop()