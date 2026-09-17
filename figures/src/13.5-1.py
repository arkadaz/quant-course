
T=np.array([1,2,3])/12;iv=np.array([.30,np.sqrt(.01095/(2/12)),.24]);w=iv**2*T
ax.plot(T,100*iv,'o-',color=ACCENT,label='Implied vol (%)');ax2=ax.twinx();ax2.plot(T,w,'s--',color=WARM,label='Total variance')
ax.set_xlabel('Maturity (years)');ax.set_ylabel('Implied volatility (%)');ax2.set_ylabel('Total variance');ax.legend(loc='upper left');ax2.legend(loc='upper right')
