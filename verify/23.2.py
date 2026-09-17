import numpy as np
qout=1e4*.98;value=qout*4.2-1e4*2.8-1e4*.1-qout*.05-28000*.05*.5
spark=90-(7*3+5);power=500*spark
assert np.isclose(value,10970) and np.isclose(power,32000) and np.isclose(500*(90-75),7500)
print('23.2 checked',value,power)
