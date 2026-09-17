Q=np.column_stack([np.ones(3)/np.sqrt(3),np.array([-1,0,1])/np.sqrt(2),np.array([1,-2,1])/np.sqrt(6)]);d=np.array([2000,5000,9000]);pnl=-(d@Q)*5/1000
ax.bar(['Level','Slope','Curvature'],pnl,color=[BAD,WARM,GOOD]);ax.axhline(0,color=MUTED);ax.set_ylabel('P&L for +5 bp score (USD thousand)')
