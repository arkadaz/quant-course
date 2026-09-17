import numpy as np
mu, V = 8.0, 400.0
w = mu**2/(mu**2+V)
assert np.isclose(w, 64/464)
assert np.isclose(V*w*w+mu**2*(1-w)**2, 55.1724137931)
assert np.isclose(20/np.sqrt(504), .8908708064)
assert np.isclose(20/np.sqrt(196560), .0451109968)
assert np.isclose((20-1)/20, .95)
assert np.isclose(8-1.96*20, -31.2)
assert np.isclose(8+1.96*20, 47.2)
