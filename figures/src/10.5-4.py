rng=np.random.default_rng(653);nmax=32768;w=np.r_[0,np.cumsum(rng.normal(0,np.sqrt(1/nmax),nmax))];ns=np.array([8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]);qb=[];qs=[]
for n in ns:
    ix=np.linspace(0,nmax,n+1,dtype=int);d=np.diff(w[ix]);tt=np.linspace(0,1,n+1);qb.append(np.sum(d*d));qs.append(np.sum(np.diff(tt*tt)**2))
ax.semilogx(ns,qb,color=ACCENT,marker='o',ms=3,label='Brownian path');ax.semilogx(ns,qs,color=GOOD,marker='o',ms=3,label='smooth path $t^2$');ax.axhline(1,color=INK,ls='--',lw=1,label='Brownian limit = 1');ax.set_xlabel('Number of intervals');ax.set_ylabel('Quadratic sum');ax.set_title('Quadratic variation detects roughness',loc='left');ax.legend(loc='center right')
