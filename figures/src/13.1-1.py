ns=np.array([8,16,32,64,128,256,512,1024]);smooth=1/ns
rng=np.random.default_rng(1201);z=rng.normal(size=ns[-1]);brown=[]
for n in ns:
 d=z[:n]/np.sqrt(n);brown.append(np.sum(d*d))
ax.loglog(ns,smooth,color=GOOD,lw=2,label='smooth path');ax.loglog(ns,brown,color=ACCENT,lw=2,marker='o',label='Brownian sample');ax.axhline(1,color=BAD,ls='--',label='limit T = 1');ax.set_xlabel('Partition count n');ax.set_ylabel('Sum of squared increments');ax.set_title('Second-order terms survive on Brownian paths',loc='left');ax.legend(fontsize=8)
