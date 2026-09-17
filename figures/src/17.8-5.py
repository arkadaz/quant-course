rng=np.random.default_rng(1788);true=np.array([[.04,.019],[.019,.01]])/252;raw=[];shr=[]
for x in rng.multivariate_normal(np.zeros(2),true,size=(120,24)):
 S=np.cov(x,rowvar=False,ddof=1);F=np.trace(S)/2*np.eye(2)
 for a,out in [(0,raw),(.5,shr)]:
  u=np.linalg.solve((1-a)*S+a*F,np.ones(2));out.append(100*u[0]/u.sum())
ax.boxplot([raw,shr],tick_labels=['Sample','50% shrunk'],showfliers=False);ax.axhline(50,color=MUTED,ls='--');ax.set_ylabel('First-asset minimum-variance weight (%)')
