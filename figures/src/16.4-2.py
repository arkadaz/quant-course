k=np.arange(0,41);w=.09*.89**k
ax.plot(k,w,color=ACCENT,lw=2,marker='o',ms=3,label='GARCH weight 0.09 × 0.89^k')
ax.step(np.arange(0,41),np.where(np.arange(0,41)<20,.05,0),where='post',color=WARM,lw=2,label='20-day window weight 1/20')
ax.axvline(np.log(.5)/np.log(.89),color=BAD,ls=':',label='GARCH weight halves after 5.95 days')
ax.set_xlabel('days since the squared return entered');ax.set_ylabel('weight in today\'s variance')
ax.set_title('GARCH forgets a shock smoothly; a rolling window drops it on day 21',loc='left');ax.legend(fontsize=7)
