import numpy as np
d15=(100-2.4*(.9755+.9505))/102.4
d2=(100-2.5*(.9755+.9505+d15))/102.5
f=-np.log(d15/.9505)/.5
assert np.isclose(d15,.931421875) and np.isclose(d2,.905916540,atol=1e-9)
assert np.isclose(f,.0405518,atol=1e-7) and np.isclose(1e7*d15,9314218.75)
print('20.1 checked',d15,d2,f)
