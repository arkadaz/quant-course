x=np.array([1.,2.,3.]);y=np.array([1.5,2.0,2.5])
A0,A1=np.meshgrid(np.linspace(-1.2,2.4,241),np.linspace(-0.4,2.4,241))
J=((A0[...,None]+A1[...,None]*x-y)**2).sum(-1)/6
cs=ax.contour(A0,A1,J,levels=[0.02,0.1,0.3,0.7,1.5,3,6],colors='0.6',linewidths=0.8)
ax.clabel(cs,fontsize=6,fmt='%.2f')
def path(lr,n):
    a=np.zeros(2);P=[a.copy()]
    for _ in range(n):
        e=a[0]+a[1]*x-y;a=a-lr*np.array([e.mean(),(e*x).mean()]);P.append(a.copy())
    return np.array(P)
p1=path(0.1,2000);p2=path(0.5,3)
ax.plot(p1[:,0],p1[:,1],'-',color=ACCENT,lw=1.6,label='Learning rate 0.1: 2,000 steps reach (1.0, 0.5), dots every 100')
ax.plot(p1[::100,0],p1[::100,1],'o',color=ACCENT,ms=3)
ax.plot(p2[:2,0],p2[:2,1],'s--',color=WARM,ms=5,lw=1.4,label='Learning rate 0.5: first step overshoots')
ax.plot([1.0],[0.5],'*',color='0.2',ms=11,label='Least-squares answer (1.0, 0.5)')
ax.set_xlim(-1.2,2.4);ax.set_ylim(-0.4,2.4);ax.set_xlabel('Intercept a0');ax.set_ylabel('Slope a1')
ax.set_title('Gradient descent on a three-point loss surface',loc='left');ax.legend(fontsize=7,loc='upper left',framealpha=0.9)
