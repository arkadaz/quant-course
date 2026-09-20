rng=np.random.default_rng(652);nmax=32768;inc=rng.normal(0,np.sqrt(1/nmax),nmax);w=np.r_[0,np.cumsum(inc)];ns=np.array([8,32,128,512,2048,8192,32768]);p1=[];p2=[];p3=[]
for n in ns:
    ix=np.linspace(0,nmax,n+1,dtype=int);d=np.diff(w[ix]);p1.append(np.sum(np.abs(d)));p2.append(np.sum(d*d));p3.append(np.sum(np.abs(d)**3))
ax.loglog(ns,p1,color=BAD,marker='o',ms=3,label='$p=1$: diverges');ax.loglog(ns,p2,color=ACCENT,marker='o',ms=3,label='$p=2$: tends to 1');ax.loglog(ns,p3,color=GOOD,marker='o',ms=3,label='$p=3$: tends to 0');ax.axhline(1,color=INK,ls='--',lw=1)
ax.set_xlabel('Number of intervals');ax.set_ylabel('Sum of absolute increments to power $p$');ax.set_title('Brownian p-variation changes regime at p=2',loc='left');ax.legend(loc='center left')
