Q=np.column_stack([np.ones(3)/np.sqrt(3),np.array([-1,0,1])/np.sqrt(2),np.array([1,-2,1])/np.sqrt(6)])
for i,n in enumerate(['Level','Slope','Curvature']):ax.plot([2,5,10],Q[:,i],marker='o',label=n)
ax.axhline(0,color=MUTED);ax.set_xlabel('UST maturity (years)');ax.set_ylabel('Loading (unitless)');ax.legend()
