Lm=np.array([1,2,3,6,12])/12;St=np.array([2,3,5,7,10,15,30])
mk={'Dec 14, 2017':(np.array([1.49078,1.52997,1.60042,1.76769,2.04263]),np.array([2.0130,2.1025,2.1950,2.2585,2.3457,2.4447,2.5055]),(1.38060,0.02406,0.01451),ACCENT),
    'Oct 11, 2018':(np.array([2.27950,2.33075,2.43631,2.63525,2.95425]),np.array([3.0408,3.1054,3.1332,3.1562,3.1990,3.2437,3.2270]),(2.81944,0.03218,0.02133),WARM)}
def P(T,k,th,r0,s=0.01):
    B=(1-np.exp(-k*T))/k;A=(th-s*s/(2*k*k))*(B-T)-s*s*B*B/(4*k);return np.exp(A-B*r0)
for lab,(L,S,x,c) in mk.items():
    Tm=np.exp(np.linspace(np.log(1/12),np.log(1),40));Ts=np.array([2,3,5,7,10,15,20,25,30])
    ax.plot(Tm,100*(1/P(Tm,*x)-1)/Tm,color=c,lw=1.6)
    sw=[100*(1-P(T,*x))/(0.5*P(np.arange(0.5,T+1e-9,0.5),*x).sum()) for T in Ts]
    ax.plot(Ts,sw,color=c,lw=1.6,ls='--')
    ax.scatter(Lm,L,color=c,marker='o',s=22,zorder=3,label=f'{lab}: LIBOR (dots) and swaps (squares)')
    ax.scatter(St,S,color=c,marker='s',s=22,zorder=3)
ax.set_xscale('log');ax.set_xticks([1/12,0.25,1,2,5,10,30]);ax.set_xticklabels(['1M','3M','1Y','2Y','5Y','10Y','30Y'])
ax.set_xlabel('Maturity (log scale)');ax.set_ylabel('Rate (%)')
ax.set_title('Vasicek with sigma fixed at 1%: close, but it cannot bend at 12M or 30Y',loc='left');ax.legend(fontsize=7,loc='lower right');ax.grid(alpha=.2)
