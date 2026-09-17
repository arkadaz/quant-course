s=np.linspace(60,500,700);s0=200;sig=.30;T=1
for drift,col,label in [(.10,ACCENT,'physical P'),(.04,WARM,'risk-neutral Q')]:
 m=np.log(s0)+(drift-.5*sig**2)*T;ax.plot(s,stats.lognorm.pdf(s,s=sig,scale=np.exp(m)),color=col,lw=2,label=label)
ax.axvline(220,color=BAD,ls='--',label='USD 220 threshold');ax.set_xlabel('AAPL terminal price (USD/share)');ax.set_ylabel('Density');ax.set_title('Drift moves; volatility does not',loc='left');ax.legend(fontsize=8)
