rng=np.random.default_rng(29)
n,T=600,251
se=rng.uniform(0.012,0.032,n)
C=np.eye(n)
for i,j,r in [(0,1,.82),(2,3,.74),(4,5,.68)]: C[i,j]=C[j,i]=r
for a in range(10,15):
    for b in range(10,15):
        if a!=b: C[a,b]=.58
E=(np.linalg.cholesky(C+1e-10*np.eye(n))@rng.standard_normal((n,T)))*se[:,None]
emp=np.corrcoef(E); off=emp[~np.eye(n,dtype=bool)]
bins=np.linspace(-0.9,0.9,121)
ax.hist(off,bins=bins,color=ACCENT,alpha=.85,label='the 179,700 measured pairs')
x=np.linspace(-0.9,0.9,400)
pdf=np.exp(-x**2/(2*(1/np.sqrt(T))**2))/np.sqrt(2*np.pi)/(1/np.sqrt(T))
ax.plot(x,pdf*len(off)*(bins[1]-bins[0]),color=BAD,lw=2.0,ls='--',label='what pure noise would give')
ax.set_yscale('log');ax.set_ylim(0.5,3e4)
for v,lab in ((0.82,'0.82'),(0.74,'0.74'),(0.68,'0.68'),(0.58,'0.58')):
    ax.plot(v,1.3,'v',color=WARM,ms=8)
ax.annotate('the real structure lives out here',xy=(0.70,2.2),xytext=(0.12,220),fontsize=8,color=WARM,
            arrowprops=dict(arrowstyle='->',color=WARM,lw=.9))
ax.set_xlabel('residual correlation between two stocks');ax.set_ylabel('number of pairs (log scale)')
ax.set_title('The middle is all noise; only the far tail is information',loc='left')
ax.legend(fontsize=7,loc='upper left')
