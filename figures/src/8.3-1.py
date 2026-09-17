t=np.linspace(-2,2,250);ax.plot(t,t**2,color=GOOD,label='positive curvature');ax.plot(t,-t**2,color=BAD,label='negative curvature');ax.plot(t,.25*t**2,color=WARM,ls='--',label='saddle up-direction')
ax.axhline(0,color=INK,lw=.8);ax.set_xlabel('Local direction');ax.set_ylabel('Objective change');ax.legend(fontsize=8);ax.set_title('Curvature classifies a stationary point',loc='left')
