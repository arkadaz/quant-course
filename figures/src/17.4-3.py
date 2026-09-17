Q=np.column_stack([np.ones(3)/np.sqrt(3),np.array([-1,0,1])/np.sqrt(2),np.array([1,-2,1])/np.sqrt(6)]);d=np.array([2000,5000,9000]);e=np.array([-14000,5000,9000]);x=np.arange(3)
ax.bar(x-.18,d@Q/1000,width=.36,label='Before');ax.bar(x+.18,e@Q/1000,width=.36,label='After');ax.set_xticks(x,['Level','Slope','Curvature']);ax.set_ylabel('Sensitivity (USD thousand per score bp)');ax.legend()
