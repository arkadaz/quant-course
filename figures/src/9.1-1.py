rng=np.random.default_rng(611)
n=900;t=np.linspace(0,1,n+1);w=np.r_[0,np.cumsum(rng.normal(0,np.sqrt(1/n),n))]
ax.plot(t,w,color=ACCENT,lw=1.5)
ax.axvspan(.12,.30,color=WARM,alpha=.18,label='non-overlapping window A')
ax.axvspan(.58,.82,color=GOOD,alpha=.15,label='non-overlapping window B')
for q in [.12,.30,.58,.82]: ax.scatter([q],[np.interp(q,t,w)],s=25,color=INK,zorder=4)
ax.set_xlabel('Time');ax.set_ylabel('$B_t$');ax.set_title('A continuous path with independent Normal increments',loc='left');ax.legend(loc='upper left',fontsize=7)
