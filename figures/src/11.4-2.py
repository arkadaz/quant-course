y=np.linspace(0,220,401);uQ=np.maximum(0,1.2*y-180);uS=np.maximum(0,y-90);q=10.8*y-6*uQ-6*uS
ax.plot(y,q,color=ACCENT,lw=2)
ax.scatter([150],[1260],color=BAD,s=48,zorder=4,label='maximum: USD 1,260')
ax.axvline(150,color=WARM,ls='--',lw=1.2)
ax.set_xlabel('Beta multiplier, $y$');ax.set_ylabel('Dual function, $q(y)$ (USD)')
ax.legend(loc='lower right',fontsize=8);ax.set_title('Maximising the lower bound recovers the dual optimum',loc='left')
