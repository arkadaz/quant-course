ds=np.linspace(0,1,101);ks=[]
for a in ds:ks.append(np.linalg.cond((1-a)*np.array([[.04,.019],[.019,.01]])+a*.025*np.eye(2)))
ax.plot(ds,ks);ax.set_xlabel('Shrinkage intensity');ax.set_ylabel('Condition number');ax.set_yscale('log')
