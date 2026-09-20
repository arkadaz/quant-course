import numpy as np
from scipy.stats import norm
M, alpha, T = 200, .05, 5
assert np.isclose(M*alpha,10)
assert np.isclose(1-(1-alpha)**M,.9999649473)
a_star=alpha/M
assert np.isclose(a_star,.00025)
z=norm.ppf(1-a_star/2)
assert np.isclose(z,3.6622599309)
assert np.isclose(z/np.sqrt(T),1.6378124313)
assert np.isclose(np.sqrt(2*np.log(M)/T),1.4557908320)
p=np.array([.0002,.0009,.0020,.0040]); thresholds=np.arange(1,5)*.10/M
assert np.array_equal(p<=thresholds,np.array([True,True,False,False]))
