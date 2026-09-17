d=np.linspace(0,1,200);w=[]
for a in d:
 S=(1-a)*np.array([[.04,.019],[.019,.01]])+a*.025*np.eye(2);u=np.linalg.solve(S,np.ones(2));w.append(u[0]/u.sum())
ax.plot(d,np.array(w)*100);ax.axhline(0,color=MUTED);ax.set_xlabel('Shrinkage intensity');ax.set_ylabel('First-asset weight (%)')
