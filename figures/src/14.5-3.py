
T=np.linspace(.08,1.0,220);good=.006+.035*T;bad=.010+.025*T-.030*T*T
ax.plot(T,good,color=ACCENT,label='Increasing total variance');ax.plot(T,bad,'--',color=BAD,label='Calendar violation');ax.axhline(0,color=INK,lw=1)
ax.set_xlabel('Maturity (years)');ax.set_ylabel('Total variance');ax.legend()
