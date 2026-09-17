S=np.array([[.04,.004],[.004,.01]]);wm=np.array([.6,.4]);lam=2.5;tau=.05
pi=lam*S@wm;P=np.array([[1.,-1.]]);q=np.array([.03]);v=float((P@(tau*S)@P.T)[0,0]);omega=v
post=pi+(tau*S)@P.T@np.linalg.solve(P@(tau*S)@P.T+np.array([[omega]]),q-P@pi)
w=np.linalg.solve(lam*S,post)
rat=np.logspace(-2,2,100);ws=[]
for k in rat:
 m=pi+(tau*S)@P.T@np.linalg.solve(P@(tau*S)@P.T+np.array([[k*v]]),q-P@pi);ws.append(np.linalg.solve(lam*S,m)[0])
ax.semilogx(rat,100*np.array(ws));ax.axhline(60,color=MUTED,ls='--');ax.set_xlabel('View variance / prior gap variance');ax.set_ylabel('Equity weight (%)')
