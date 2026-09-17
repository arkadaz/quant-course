r=np.linspace(0,.12,121);pv=105/(1+r)
ax.plot(100*r,pv,color=WARM,lw=2);ax.scatter([5],[100],color=BAD,s=40,zorder=3)
ax.set_xlabel('Annual rate (%)');ax.set_ylabel('Present value (USD)');ax.set_title('PV of USD 105 due in one year',loc='left');ax.grid(alpha=.25)
