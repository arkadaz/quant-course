import collections
rng=np.random.default_rng(29)
n,T=600,251
se=rng.uniform(0.012,0.032,n)
C=np.eye(n)
for i,j,r in [(0,1,.82),(2,3,.74),(4,5,.68)]: C[i,j]=C[j,i]=r
for a in range(10,15):
    for b in range(10,15):
        if a!=b: C[a,b]=.58
E=(np.linalg.cholesky(C+1e-10*np.eye(n))@rng.standard_normal((n,T)))*se[:,None]
emp=np.corrcoef(E)
def nstocks(th):
    keep=np.abs(emp)>th; np.fill_diagonal(keep,False)
    return int((keep.any(axis=1)).sum())
ths=np.linspace(0.12,0.85,80)
y=[nstocks(t) for t in ths]
ax.semilogy(ths,np.maximum(y,0.5),color=ACCENT,lw=2.4)
ax.axvspan(0.30,0.55,color=GRID,alpha=.9,zorder=0)
ax.annotate('the plateau: nothing changes\n13 pairs, 4 clusters, 11 stocks',xy=(0.425,14),
            xytext=(0.44,120),fontsize=8,color=INK,arrowprops=dict(arrowstyle='->',color=INK,lw=.9))
ax.axvline(2*np.sqrt(np.log(n)/T),color=BAD,ls='--',lw=1.8)
ax.annotate('the formula says 0.319',xy=(0.319,1.4),xytext=(6,0),textcoords='offset points',
            fontsize=7.5,color=BAD,rotation=90,va='bottom')
ax.annotate('noise floods in',xy=(0.17,nstocks(0.17)),xytext=(0.135,55),fontsize=8,color=MUTED)
ax.annotate('real pairs start dying',xy=(0.72,max(nstocks(0.72),0.6)),xytext=(0.60,2.6),
            fontsize=8,color=MUTED)
ax.set_xlabel('threshold on the residual correlation')
ax.set_ylabel('stocks left in some cluster (log scale)')
ax.set_title('Pick the threshold where the answer stops moving',loc='left')
