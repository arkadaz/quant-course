import numpy as np
from scipy.stats import norm
mu, sigma, n, days = 0.005, 2.0, 10_000, 250
assert np.isclose(n*mu, 50.0)
assert np.isclose(sigma*np.sqrt(n), 200.0)
assert np.isclose((mu/sigma)*np.sqrt(n), 0.25)
assert np.isclose(norm.cdf(-0.25), 0.4012936743)
assert np.isclose(n*mu*days, 12_500.0)
assert np.isclose(200*np.sqrt(days), 3162.2776602)
assert np.isclose(.25*np.sqrt(days), 3.9528470752)
assert np.isclose(10_000/(1+9999*.001), 909.1735612)
