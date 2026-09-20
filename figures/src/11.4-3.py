y=np.linspace(0,210,301);uQ=np.maximum(0,1.2*y-180);uS=np.maximum(0,y-90)
kQ=180-1.2*y+uQ;kS=90-y+uS
ax.plot(y,kQ,color=ACCENT,lw=2,label='QQQ coefficient')
ax.plot(y,kS,color=GOOD,lw=2,label='SPY coefficient')
ax.axhline(0,color=INK,lw=1);ax.axvline(150,color=WARM,ls='--',lw=1.2,label='$y=150$')
ax.set_xlabel('Beta multiplier, $y$');ax.set_ylabel('Decision coefficient (USD per USD million)')
ax.legend(loc='upper right',fontsize=8);ax.set_title('Dual feasibility keeps every decision slope non-negative',loc='left')
