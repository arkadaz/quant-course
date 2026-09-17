S=np.array([[.04,.004],[.004,.01]]);wm=np.array([.6,.4]);lam=2.5;tau=.05
pi=lam*S@wm;P=np.array([[1.,-1.]]);q=np.array([.03]);v=float((P@(tau*S)@P.T)[0,0]);omega=v
post=pi+(tau*S)@P.T@np.linalg.solve(P@(tau*S)@P.T+np.array([[omega]]),q-P@pi)
w=np.linalg.solve(lam*S,post)
wlimit=np.linalg.solve(lam*S,pi+(tau*S)@P.T@np.linalg.solve(P@(tau*S)@P.T,q-P@pi));e=np.array([wm[0],wlimit[0],w[0]])*100;x=np.arange(3)
ax.bar(x,e,label='US equities');ax.bar(x,100-e,bottom=e,label='US Treasuries');ax.set_xticks(x,['Prior','Exact-view limit','Posterior']);ax.set_ylabel('Weight (%)');ax.legend(loc='lower right')
