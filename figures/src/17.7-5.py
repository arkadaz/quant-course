nsep=np.array([[240,5],[5,0]]);nclu=np.array([[244,1],[1,4]])
def lrind(n):
 p=n.sum(axis=0)[1]/n.sum();p0=n[0,1]/n[0].sum();p1=n[1,1]/n[1].sum();ll0=n[:,1].sum()*np.log(p)+n[:,0].sum()*np.log(1-p);ll1=0.
 for i,pi in enumerate([p0,p1]):
  if n[i,0]:ll1+=n[i,0]*np.log(1-pi)
  if n[i,1]:ll1+=n[i,1]*np.log(pi)
 return 2*(ll1-ll0)
ax.bar(['Separated','Clustered'],[lrind(nsep),lrind(nclu)],color=[ACCENT,BAD]);ax.set_ylabel('Christoffersen independence statistic');ax.set_ylim(0,35)
