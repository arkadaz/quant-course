t=np.linspace(0,10,201);d=1/(1.05**t)
ax.plot(t,d,color=GOOD,lw=2);ax.axhline(1,color=MUTED,ls='--',lw=1)
ax.set_xlabel('Maturity (years)');ax.set_ylabel('Discount factor');ax.set_title('Flat 5% annual-effective assumption',loc='left');ax.grid(alpha=.25)
