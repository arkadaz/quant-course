from scipy.linalg import solve_banded
K,r,sig,T,dS,Smax,N=52.,.05,.3,.5,1.,150.,100
M=int(Smax/dS);S=np.arange(M+1)*dS;i=np.arange(M+1);dt=T/N
a=.5*(sig**2*i**2-r*i);b=-(sig**2*i**2+r);c=.5*(sig**2*i**2+r*i)
ab=np.zeros((3,M+1));ab[1,:]=1;ab[1,1:-1]=1-dt*b[1:-1];ab[0,2:]=-dt*c[1:-1];ab[2,:-2]=-dt*a[1:-1]
V=np.maximum(K-S,0);rows=[V.copy()];bnd=[K]
for n in range(N):
    rhs=V.copy();rhs[0]=K;rhs[-1]=0
    V=np.maximum(solve_banded((1,1),ab,rhs),K-S);rows.append(V.copy())
    ex=S[(V-(K-S))<1e-9];bnd.append(ex.max() if len(ex) else np.nan)
G=np.array(rows)[:,:101];tau=np.arange(N+1)*dt
im=ax.imshow(G,origin='lower',aspect='auto',extent=[0,100,0,T],cmap='viridis')
ax.plot(bnd,tau,color='white',lw=1.8,label='exercise boundary')
ax.axvline(52,color='white',ls='--',lw=1);ax.text(53,.47,'K = 52',color='white',fontsize=7.5)
ax.scatter([50],[.5],color=WARM,zorder=3,s=26);ax.annotate('S 50, 0.5 year: 4.78',xy=(50,.5),xytext=(58,.43),color='white',fontsize=7.5)
ax.set_xlabel('Stock price S (USD)');ax.set_ylabel('Time to expiry (years)')
ax.figure.colorbar(im,ax=ax,label='American put value (USD)')
ax.set_title('American put solved on the grid',loc='left');ax.legend(fontsize=7.5,loc='lower right');ax.grid(False)
