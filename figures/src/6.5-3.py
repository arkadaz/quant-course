a=np.linspace(-2,2,100)
mean=75*a+40
ax.plot(a,mean,color=ACCENT,lw=2)
ax.axhline(0,color=MUTED,lw=0.8);ax.axvline(0,color=MUTED,lw=0.8)
ax.set_xlabel('AAPL position coefficient a');ax.set_ylabel('expected combined P&L (USD/day)')
ax.set_title('Expected values add under any dependence structure',fontsize=9,loc='left')
