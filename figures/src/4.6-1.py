rng=np.random.default_rng(0)
S=np.array([[0.0004,0.00024],[0.00024,0.0009]])
pts=rng.multivariate_normal([0,0],S,500)
vals,vecs=np.linalg.eigh(S)
ax.scatter(pts[:,0]*100,pts[:,1]*100,s=8,alpha=0.25,color=ACCENT)
for val,vec,col in zip(vals,vecs.T,[WARM,BAD]):
    p=2*100*np.sqrt(val)*vec
    ax.plot([-p[0],p[0]],[-p[1],p[1]],color=col,lw=2)
ax.set_xlabel('SPX one-day return (%)');ax.set_ylabel('QQQ one-day return (%)')
ax.set_title('Eigenvectors reveal the principal covariance directions',fontsize=9,loc='left')
