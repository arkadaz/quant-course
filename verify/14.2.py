import numpy as np
mu, sigma = .03, .06
assert np.isclose(sigma/np.sqrt(4), .03)
assert np.isclose((mu/sigma)*np.sqrt(4), 1.0)
assert np.isclose((2/.5)**2, 16.0)
assert np.isclose((2/.25)**2, 64.0)
assert np.isclose(np.sqrt((1+.5)/(1-.5)), np.sqrt(3))
assert np.isclose(.25*np.sqrt(64), 2.0)
