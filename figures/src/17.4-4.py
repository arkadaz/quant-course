Q=np.column_stack([np.ones(3)/np.sqrt(3),np.array([-1,0,1])/np.sqrt(2),np.array([1,-2,1])/np.sqrt(6)]);base=np.array([4.2,4.1,4.0]);ten=[2,5,10]
ax.plot(ten,base,color=MUTED,ls='--',label='Assumed base')
for i,n in enumerate(['Level','Slope','Curvature']):ax.plot(ten,base+Q[:,i]*[9,3,1][i]/100,label=n)
ax.set_xlabel('UST maturity (years)');ax.set_ylabel('Yield (%)');ax.legend(fontsize=7)
