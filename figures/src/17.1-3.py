h=np.arange(1,21);v=20e6*(.011*np.sqrt(h)*stats.norm.ppf(.99)-h*.0002)
ax.plot(h,v/1e6,label='Independent additive returns');ax.plot(h,h*v[0]/1e6,ls='--',label='Linear scaling');ax.set_xlabel('Horizon (trading days)');ax.set_ylabel('VaR 99% (USD million)');ax.legend()
