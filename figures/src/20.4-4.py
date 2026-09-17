exp=np.array([.5,1,2,3]);strikes=np.array([4,4.5,5,5.5,6]);Z=np.zeros((len(exp),len(strikes)));N=10e6;F=.052;vol=.012
for i,T in enumerate(exp):
 up=F+vol*np.sqrt(T);dn=max(F-vol*np.sqrt(T),0);A=2.0*np.exp(-.045*T);Z[i]=.5*N*A*(np.maximum(up-strikes/100,0)+np.maximum(dn-strikes/100,0))/1000
heatmap(ax,Z,[f'{x:g}y' for x in exp],[f'{k:g}%' for k in strikes],title='Payer swaption value on a one-step lattice (USD thousands)',fmt='.0f')
