from scipy.linalg import solve_banded
K,r,sig,T,dS,Smax,N=52.,.05,.3,.5,.5,200.,400
M=int(Smax/dS);S=np.arange(M+1)*dS;i=np.arange(M+1);dt=T/N
a=.5*(sig**2*i**2-r*i);b=-(sig**2*i**2+r);c=.5*(sig**2*i**2+r*i)
ab=np.zeros((3,M+1));ab[1,:]=1;ab[1,1:-1]=1-dt*b[1:-1];ab[0,2:]=-dt*c[1:-1];ab[2,:-2]=-dt*a[1:-1]
V=np.maximum(K-S,0)
for n in range(N):
    rhs=V.copy();rhs[0]=K;rhs[-1]=0;V=np.maximum(solve_banded((1,1),ab,rhs),K-S)
d1=(np.log(np.maximum(S,1e-9)/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
E=K*np.exp(-r*T)*stats.norm.cdf(-d2)-S*stats.norm.cdf(-d1)
m=(S>=20)&(S<=80);sb=S[(V-(K-S))<1e-9].max()
ax.plot(S[m],np.maximum(K-S[m],0),color=BAD,lw=1.5,label='exercise now: max(52 - S, 0)')
ax.plot(S[m],V[m],color=ACCENT,lw=2.2,label='American put (grid)')
ax.plot(S[m],E[m],color=MUTED,lw=1.2,ls=(0,(4,3)),label='European put (Black-Scholes)')
ax.axvspan(20,sb,color=BAD,alpha=.10);ax.text(21,3,f'exercise now\nbelow {sb:.1f}',fontsize=7.5,color=BAD)
ax.scatter([50,50],[V[100],E[100]],color=INK,zorder=3,s=22)
ax.annotate(f'S 50: {V[100]:.2f} vs {E[100]:.2f}',xy=(50,V[100]),xytext=(54,9),fontsize=7.5)
ax.set_xlabel('Stock price S (USD)');ax.set_ylabel('Value with 0.5 year left (USD)')
ax.set_title('Early exercise: where the grid picks the payoff',loc='left');ax.legend(fontsize=7.3,loc='upper right');ax.grid(alpha=.2)
