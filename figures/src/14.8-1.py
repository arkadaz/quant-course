
r=0.01*np.array([1.2,-1.0,.7,-2.2,1.8,-1.5,.4,-.9,2.1,-.6])
contrib=252/len(r)*r*r
ax.bar(np.arange(1,len(r)+1),contrib,color=np.where(r>=0,GOOD,BAD))
ax.set_xlabel('Observation');ax.set_ylabel('Contribution to annual variance')
ax.set_xticks(np.arange(1,11))
