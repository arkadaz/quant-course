w=np.linspace(-3.2,4.0,500);f=3*w**4-4*w**3-36*w**2
ax.plot(w,f,color=ACCENT,lw=2);ax.scatter([-2,3],[-64,-189],c=[WARM,GOOD],s=48);ax.set_xlabel('Signal weight, $w$');ax.set_ylabel('Backtest loss (USD million)');ax.set_title('One smooth function can contain two valleys',loc='left')
