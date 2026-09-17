import numpy as np
a=.5*.02*(.3**2*10**2-.05*10);b=1-.02*(.3**2*10**2+.05);c=.5*.02*(.3**2*10**2+.05*10)
assert np.allclose([a,b,c],[.085,.819,.095])
assert np.isclose(a*7.30+b*4.10+c*2.00,4.1684)
assert .02*(.3**2*80**2+.05)>1
print('21.1 checked')
