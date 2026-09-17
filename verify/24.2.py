import numpy as np
assets=1e7*.92;equity=assets-9e6;call=.05*assets-equity
assert np.isclose(equity,2e5) and np.isclose(call,260000) and np.isclose(1/.2,5)
print('24.2 checked',equity,call)
