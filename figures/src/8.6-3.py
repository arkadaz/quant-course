vals=[.0265,.0265,.036];ax.bar(['SPY','AGG','QQQ'],vals,color=[GOOD,GOOD,BAD]);ax.axhline(.0265,color=WARM,ls='--',label='held-asset level')
ax.annotate('$u_3=0.0095$',xy=(2,.036),xytext=(1.25,.041),arrowprops=dict(arrowstyle='->',color=BAD),color=BAD);ax.set_ylabel('Marginal annual variance');ax.legend();ax.set_title('The excluded asset fails the marginal-risk test',loc='left')
