from scipy.stats import norm, binom
N=125;x=np.linspace(-9,9,6001);w=norm.pdf(x);w=w/w.sum();lv=np.arange(N+1)
def dist(q,rho):
    if rho==0: return binom.pmf(lv,N,q)
    qm=np.clip(norm.cdf((norm.ppf(q)-np.sqrt(rho)*x)/np.sqrt(1-rho)),1e-15,1-1e-15)
    return (binom.pmf(lv[:,None],N,qm[None,:])*w).sum(1)
rh=np.r_[0,np.linspace(0.02,0.98,25)];E=[]
for r in rh:
    p=dist(0.02,r);E.append([(np.clip(lv-a,0,b-a)*p).sum() for a,b in ((0,3),(3,6),(6,9),(6,125))])
E=np.array(E)
for k,(lab,c) in enumerate(zip(['Equity 0-3','Mezzanine 3-6','Senior 6-9','Super senior 6-125'],[ACCENT,BAD,GOOD,WARM])):
    ax.plot(rh,E[:,k],color=c,lw=1.8,label=lab)
ax.set_xlabel('Asset correlation rho');ax.set_ylabel('Expected loss (units, q = 2%)')
ax.set_title('Same portfolio mean 2.5: correlation moves loss from equity to super senior',loc='left');ax.legend(fontsize=7,loc='center right');ax.grid(alpha=.2)
