import numpy as np
is_=(30000*.03+30000*.002)+(20000*.01+20000*.004)
etf=10000*(101.2-100-.2-.35)
borrow=20000*30*.36*(30/365);base=60000-borrow-1600
assert np.isclose(is_,1240) and np.isclose(etf,6500) and np.isclose(borrow,17753.4246575)
assert np.isclose(base,40646.5753425)
print('24.3 checked',is_,etf,base)
