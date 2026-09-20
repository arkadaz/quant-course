x1=np.linspace(0,12,400);x2=12-x1;F=2*np.log1p(x1)+4*np.log1p(x2);xo=11/3
ax.plot(x1,F,color=ACCENT,lw=2);ax.scatter([xo],[2*np.log(14/3)+4*np.log(28/3)],color=GOOD,s=50,label='optimum')
ax.set_xlabel('Desk 1 capital (USD million)');ax.set_ylabel('Expected annual profit (USD million)');ax.legend();ax.set_title('The equality constraint turns the surface into one curve',loc='left')
