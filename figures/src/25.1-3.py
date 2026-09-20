rng=np.random.default_rng(7)
sig=np.linspace(.02,.80,33)
T=251
sim=[]
for s in sig:
    x=rng.normal(0.0,s/np.sqrt(T),(12000,T))
    sim.append((np.expm1(x).sum(axis=1)).mean()-np.log(np.exp(x).prod(axis=1)).mean())
ax.plot(sig*100,np.array(sim)*100,color=ACCENT,lw=2.2,label='simulated gap over 251 days')
ax.plot(sig*100,.5*sig**2*100,color=BAD,lw=1.8,ls='--',label='sigma squared over 2')
for s,lab in [(.1584,'15.84% gives 1.26 pt'),(.30,'30% gives 4.5 pt'),(.60,'60% gives 18 pt')]:
    ax.plot(s*100,.5*s**2*100,'o',color=WARM,ms=5)
    ax.annotate(lab,xy=(s*100,.5*s**2*100),xytext=(9,-4),textcoords='offset points',fontsize=7,color=WARM)
ax.set_xlabel('annualised volatility (%)');ax.set_ylabel('gap, arithmetic minus compounded (points)')
ax.set_title('Volatility drag grows with the square of volatility',loc='left');ax.legend(fontsize=7,loc='upper left')
