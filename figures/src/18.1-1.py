t=np.linspace(0,5,101);fv=100*(1.05**t)
ax.plot(t,fv,color=ACCENT,lw=2);ax.scatter([0,1],[100,105],color=BAD,zorder=3)
ax.set_xlabel('Horizon (years)');ax.set_ylabel('Future value (USD)');ax.set_title('USD 100 compounded at 5% per year',loc='left');ax.grid(alpha=.25)
