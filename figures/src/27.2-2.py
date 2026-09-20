rng=np.random.default_rng(5)
m,T=40,126
v=np.linspace(1.10,0.15,m)/100
C=np.eye(m)*0.75+0.25*np.ones((m,m));O=np.outer(v,v)*C
L=np.linalg.cholesky(O)
rel=lambda X: np.linalg.norm(X-O,'fro')/np.linalg.norm(O,'fro')
rhos=np.linspace(0,0.6,31)
E=np.zeros(len(rhos));K=np.zeros(len(rhos))
R=120
for _ in range(R):
    f=L@rng.standard_normal((m,T));emp=f@f.T/T
    tgt=np.trace(emp)/m*np.eye(m)
    for i,p in enumerate(rhos):
        S=(1-p)*emp+p*tgt
        E[i]+=rel(S);K[i]+=np.linalg.cond(S)
E/=R;K/=R
ax.plot(rhos,E,color=ACCENT,lw=2.4,label='distance from the truth (left)')
i0=int(np.argmin(E))
ax.plot(rhos[i0],E[i0],'o',color=INK,ms=8)
ax.annotate(f'best at {rhos[i0]:.2f}',xy=(rhos[i0],E[i0]),xytext=(8,10),
            textcoords='offset points',fontsize=8)
ax.axvspan(0.15,0.25,color=GRID,alpha=.8,zorder=0)
ax.annotate('what people actually use',xy=(0.20,0.262),fontsize=7.5,color=MUTED,ha='center')
ax.set_xlabel('shrinkage toward a flat diagonal');ax.set_ylabel('distance from the truth')
ax2=ax.twinx()
ax2.semilogy(rhos,K,color=BAD,lw=2.0,ls='--',label='condition number (right)')
ax2.set_ylabel('condition number',color=BAD)
ax2.tick_params(axis='y',colors=BAD)
ax.set_title('Accuracy peaks at 0.09; stability keeps improving past it',loc='left')
ax.legend(fontsize=7,loc='upper center');ax2.legend(fontsize=7,loc='upper right')
