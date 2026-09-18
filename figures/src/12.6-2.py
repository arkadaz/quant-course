s=np.linspace(35,230,700);s0=100;sig=.28;T=1
for drift,col,label in [(.12,ACCENT,'physical P: 47.93% above 110'),(.02,WARM,'risk-neutral Q: 34.13% above 110')]:
 m=np.log(s0)+(drift-.5*sig**2)*T;ax.plot(s,stats.lognorm.pdf(s,s=sig,scale=np.exp(m)),color=col,lw=2,label=label)
ax.axvline(110,color=BAD,ls='--',label='USD 110 threshold');ax.set_xlabel('Terminal price after 1 year (USD/share)');ax.set_ylabel('Density');ax.set_title('Drift moves; volatility does not',loc='left');ax.legend(fontsize=8)
