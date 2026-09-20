labels=['Independent','Positive co-movement','Negative co-movement']
base=[2,2,2];cross=[0,1.4,-1.0]
ax.bar(labels,base,color=ACCENT,label='component variances')
ax.bar(labels,cross,bottom=base,color=[MUTED,BAD,GOOD],label='2ab covariance term')
ax.axhline(0,color=MUTED,lw=0.8);ax.set_ylabel('variance units')
ax.legend(loc='upper left');ax.set_title('The cross-term is the price of dependence',fontsize=9,loc='left')
