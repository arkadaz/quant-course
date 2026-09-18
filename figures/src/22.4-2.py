from scipy.stats import norm, binom
N=125;x=np.linspace(-9,9,6001);w=norm.pdf(x);w=w/w.sum()
def dist(q,rho):
    if rho==0: return binom.pmf(np.arange(N+1),N,q)
    qm=np.clip(norm.cdf((norm.ppf(q)-np.sqrt(rho)*x)/np.sqrt(1-rho)),1e-15,1-1e-15)
    return (binom.pmf(np.arange(N+1)[:,None],N,qm[None,:])*w).sum(1)
l=np.arange(0,21);p0=dist(0.02,0.0)[:21];p5=dist(0.02,0.5)[:21]
ax.bar(l-0.2,p0,0.4,color=ACCENT,label='rho = 0 (independent)')
ax.bar(l+0.2,p5,0.4,color=WARM,label='rho = 0.5')
for a in (3,6,9): ax.axvline(a+0.5,color='0.5',ls=':',lw=1)
ax.text(1.4,0.55,'equity',fontsize=7,ha='center');ax.text(4.5,0.55,'mezz',fontsize=7,ha='center');ax.text(7.5,0.55,'senior',fontsize=7,ha='center')
ax.set_xlabel('Number of defaults out of 125 (q = 2%, same mean 2.5)');ax.set_ylabel('Probability')
ax.set_title('Correlation piles probability at zero and in the far tail',loc='left');ax.legend(fontsize=7,loc='upper right');ax.grid(axis='y',alpha=.2)
