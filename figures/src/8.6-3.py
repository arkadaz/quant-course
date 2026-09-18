vals=[.0191579,.0191579,.0283684];ax.bar(['Stocks','Bonds','Tech'],vals,color=[GOOD,GOOD,BAD]);ax.axhline(.0191579,color=WARM,ls='--',label='held-asset level 2$\\sigma_p^2$')
ax.annotate('$u_3=0.00921$',xy=(2,.0283684),xytext=(1.2,.0305),arrowprops=dict(arrowstyle='->',color=BAD),color=BAD)
ax.set_ylim(0,.034);ax.set_ylabel('Marginal annual variance $2(Vx)_i$');ax.legend(loc='upper left');ax.set_title('The excluded asset fails the marginal-risk test',loc='left')
