x=np.linspace(-7,7,180);beta=0.60;muX=0.04;muY=0.03
forecast=muY+beta*(x-muX);cond_sd=np.sqrt(7.56)
ax.plot(x,forecast,color=ACCENT,lw=2)
ax.fill_between(x,forecast-cond_sd,forecast+cond_sd,color=ACCENT,alpha=0.18,label='conditional mean +/- 1 SD')
ax.axhline(muY,color=MUTED,lw=0.8);ax.axvline(muX,color=MUTED,lw=0.8)
ax.set_xlabel('observed SPX return (%)');ax.set_ylabel('conditional QQQ return (%)');ax.legend(loc='upper left',fontsize=8)
ax.set_title('The signal changes the forecast; residual risk remains',fontsize=9,loc='left')
