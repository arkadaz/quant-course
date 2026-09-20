k=np.arange(0,45)
lam,a1,b1=0.94,.09,.89
ax.plot(k,(1-lam)*lam**k,color=ACCENT,lw=2.2,marker='o',ms=3,label='EWMA, 0.06 x 0.94^k')
ax.plot(k,a1*b1**k,color=WARM,lw=2.2,marker='s',ms=3,label='GARCH, 0.09 x 0.89^k')
ax.step(k,np.where(k<20,0.05,0),where='post',color=BAD,lw=2.0,label='20-day window, 1/20 then nothing')
ax.axvline(-np.log(2)/np.log(lam),color=ACCENT,ls=':',lw=1.1)
ax.axvline(-np.log(2)/np.log(b1),color=WARM,ls=':',lw=1.1)
ax.annotate('half-life 11.2 d',xy=(11.2,0.052),fontsize=7,color=ACCENT,rotation=90,va='bottom',ha='right')
ax.annotate('half-life 5.9 d',xy=(5.95,0.052),fontsize=7,color=WARM,rotation=90,va='bottom',ha='right')
ax.annotate('the window drops it all at once',xy=(20,0.05),xytext=(23,0.062),fontsize=7.5,color=BAD,
            arrowprops=dict(arrowstyle='->',color=BAD,lw=.8))
ax.set_xlabel('days since the squared return happened');ax.set_ylabel("weight in today's variance")
ax.set_title('Two ways to forget, and one way to fall off a cliff',loc='left')
ax.legend(fontsize=7,loc='upper right')
