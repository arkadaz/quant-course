h=np.array([0.00002,0.00004,0.00008,0.00016]);mu=75;sig=300
M=lambda z:np.exp(mu*z+0.5*sig*sig*z*z)
first=(M(h)-M(-h))/(2*h)
second=(M(h)-2*M(0)+M(-h))/(h*h)
ax.plot(h,first,color=ACCENT,marker='o',label='first derivative ≈ 75')
ax.plot(h,second,color=WARM,marker='o',label='second derivative ≈ 95,625')
ax.axhline(mu,color=ACCENT,ls='--',lw=0.8);ax.axhline(sig*sig+mu*mu,color=WARM,ls='--',lw=0.8)
ax.set_xscale('log');ax.set_xlabel('finite-difference step h');ax.set_ylabel('estimated moment');ax.legend(loc='center left')
ax.set_title('Finite-difference derivatives should recover moments',fontsize=9,loc='left')
