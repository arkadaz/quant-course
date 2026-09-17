rng=np.random.default_rng(641);n=700;x=np.linspace(0,1,n+1);w=np.r_[0,np.cumsum(rng.normal(0,np.sqrt(1/n),n))];s=.35;v=.82;ws=np.interp(s,x,w);wv=np.interp(v,x,w)
ax.plot(x,w,color=ACCENT,lw=1.6);ax.axvspan(0,s,color=WARM,alpha=.16,label='shared history');ax.axvspan(s,v,color=GOOD,alpha=.12,label='future increment')
ax.scatter([s,v],[ws,wv],color=[WARM,GOOD],s=42,zorder=4);ax.text(s,ws+.12,'$W_s$',ha='center');ax.text(v,wv+.12,'$W_{t+s}$',ha='center')
ax.set_xlabel('Time');ax.set_ylabel('$W$');ax.set_title('Covariance comes from the shared interval',loc='left');ax.legend(loc='lower left')
