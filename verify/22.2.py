import numpy as np
cpr=.06;smm=1-(1-cpr)**(1/12)
assert np.isclose(smm,.005143,atol=1e-6)
assert np.isclose(min(.002*30,.06),.06)
assert np.isclose(100*smm,0.5143,atol=.001)
print('22.2 checked',smm)
