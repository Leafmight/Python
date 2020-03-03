import numpy as np
filename = './befkbhalderstatkode.csv'

dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
