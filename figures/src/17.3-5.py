rho=np.array([-.5,.2,.8]);w=[];sd=[]
for r in rho:
 S=np.array([[.04,r*.02],[r*.02,.01]]);u=np.linalg.solve(S,np.ones(2));a=u/u.sum();w.append(a[0]);sd.append(np.sqrt(a@S@a))
ax.bar(['-0.5','0.2','0.8'],100*np.array(sd),color=[GOOD,ACCENT,BAD]);ax.set_xlabel('Equity–Treasury correlation');ax.set_ylabel('Minimum-variance standard deviation (%)')
