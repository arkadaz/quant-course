S=np.array([[.04,.004],[.004,.01]]);wm=np.array([.6,.4]);lam=2.5;tau=.05;pi=lam*S@wm;P=np.array([[1.,-1.],[1.,-1.]]);q=np.array([.03,.03]);v=float((P[:1]@(tau*S)@P[:1].T)[0,0]);gaps=[]
for O in [v*np.eye(2),v*np.array([[1.,.9],[.9,1.]])]:
 post=pi+(tau*S)@P.T@np.linalg.solve(P@(tau*S)@P.T+O,q-P@pi);gaps.append(100*(post[0]-post[1]))
ax.bar(['Errors treated independent','Errors correlated 0.9'],gaps,color=[BAD,ACCENT]);ax.axhline(4.8,color=MUTED,ls='--');ax.set_ylabel('Posterior equity–Treasury gap (percentage points)')
