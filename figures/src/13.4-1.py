
ST=np.linspace(3500,6500,301);K=5000.;cp=np.maximum(ST-K,0)-np.maximum(K-ST,0)
ax.plot(ST,cp,color=ACCENT,lw=3,label='Call minus put');ax.plot(ST,ST-K,'--',color=WARM,label='Forward payoff')
ax.axhline(0,color=INK,lw=1);ax.set_xlabel('SPX at expiry');ax.set_ylabel('Payoff (points)');ax.legend()
