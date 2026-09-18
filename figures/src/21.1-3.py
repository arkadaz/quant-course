from scipy.linalg import solve_banded
K,r,sig,T,dS,Smax=52.,.05,.3,.5,.5,200.
M=int(Smax/dS);S=np.arange(M+1)*dS;i=np.arange(M+1)
a=.5*(sig**2*i**2-r*i);b=-(sig**2*i**2+r);c=.5*(sig**2*i**2+r*i)
def put50(N,theta):
    dt=T/N;V=np.maximum(K-S,0)
    ab=np.zeros((3,M+1));ab[1,:]=1;ab[1,1:-1]=1-theta*dt*b[1:-1];ab[0,2:]=-theta*dt*c[1:-1];ab[2,:-2]=-theta*dt*a[1:-1]
    for n in range(N):
        rhs=V.copy();rhs[1:-1]=V[1:-1]+(1-theta)*dt*(a[1:-1]*V[:-2]+b[1:-1]*V[1:-1]+c[1:-1]*V[2:])
        rhs[0]=K*np.exp(-r*(n+1)*dt);rhs[-1]=0;V=solve_banded((1,1),ab,rhs)
    return V[100]
ref=put50(5000,.5);Ns=np.array([10,20,40,80,160,320])
e1=[abs(put50(n,1.)-ref) for n in Ns];e2=[abs(put50(n,.5)-ref) for n in Ns]
ax.loglog(Ns,e1,'o-',color=WARM,label='implicit Euler')
ax.loglog(Ns,e2,'s-',color=ACCENT,label='Crank-Nicolson')
ax.set_xlabel('Number of time steps over 0.5 year');ax.set_ylabel('Error at S = 50 (USD)')
ax.set_title('Halving the step halves one error and quarters the other',loc='left');ax.legend(fontsize=7.5);ax.grid(True,which='both',alpha=.3)
