import numpy as np
pair=1e4*(.8-.12-.015*10-.005*10)-3500
net=19e6*.0018-1e5*.095
assert np.isclose(pair,1300) and np.isclose(net,24700)
print('24.1 checked',pair,net)
