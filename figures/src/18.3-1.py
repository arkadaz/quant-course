S0,u,R,K=100.,1.07,1.01,100.;d=1/u;q=(R-d)/(u-d)
S={(t,k):S0*u**k*d**(t-k) for t in range(4) for k in range(t+1)}
C={(3,k):max(S[(3,k)]-K,0) for k in range(4)}
for t in (2,1,0):
    for k in range(t+1): C[(t,k)]=(q*C[(t+1,k+1)]+(1-q)*C[(t+1,k)])/R
for t in range(3):
    for k in range(t+1):
        for kk in (k,k+1): ax.plot([t,t+1],[S[(t,k)],S[(t+1,kk)]],color=MUTED,lw=1,zorder=1)
ax.axhline(K,color=BAD,lw=.9,ls=(0,(4,3)))
for (t,k),s in S.items():
    ax.scatter([t],[s],s=34,color=ACCENT if C[(t,k)]>0 else MUTED,zorder=3)
    ax.annotate(f'{s:.2f}\ncall {C[(t,k)]:.2f}',xy=(t,s),xytext=(6,-2),textcoords='offset points',fontsize=7,va='center')
ax.text(3.05,K+1.2,'K = 100',fontsize=7.5,color=BAD)
ax.set_xticks(range(4));ax.set_xticklabels(['t = 0','t = 1','t = 2','t = 3'])
ax.set_xlim(-.2,3.7);ax.set_ylabel('Stock price (USD)')
ax.set_title('Source tree: u 1.07, R 1.01, call K 100 worth 6.57',loc='left');ax.grid(alpha=.2)
