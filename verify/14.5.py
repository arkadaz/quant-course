import numpy as np
T1,T2,Tm=1/12,3/12,2/12
s1,s2=.30,.24
w1,w2=s1*s1*T1,s2*s2*T2
vf=(w2-w1)/(T2-T1);wf=w1+(Tm-T1)/(T2-T1)*(w2-w1);sm=np.sqrt(wf/Tm)
assert np.isclose(w1,.0075)
assert np.isclose(w2,.0144)
assert np.isclose(vf,.0414)
assert np.isclose(np.sqrt(vf),.20346989949375807)
assert np.isclose(wf,.01095)
assert np.isclose(sm,.2563201123595259)
assert np.isclose(.5*(s1+s2),.27)
assert np.isclose(.27-sm,.01367988764047412)
C=np.array([112.0,80.0,47.0])
assert np.isclose(C[0]-2*C[1]+C[2],-1.0)
assert np.all(np.diff(C)<=0)
