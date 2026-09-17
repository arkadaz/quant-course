labels=['Calm','Stress']
means=[200,-500]
sds=[400,1000]
ax.errorbar(labels,means,yerr=sds,fmt='o',capsize=6,color=ACCENT,lw=2,ms=6)
ax.axhline(25,color=GOOD,ls='--',lw=1.2,label='Overall mean = $25/day')
ax.set_ylabel('conditional mean ± SD (USD/day)')
ax.legend(loc='lower left')
ax.set_title('Each regime has its own centre and spread',fontsize=9,loc='left')
