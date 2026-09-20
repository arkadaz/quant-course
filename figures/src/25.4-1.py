n=np.logspace(np.log10(12),np.log10(100000),200)
drift=np.full_like(n,100.0)
vol=0.5*np.sqrt(2/n)/ (0.5*np.sqrt(2/251)) *100*np.sqrt(251/251)
vol=0.5*np.sqrt(2/n)*100
ax.loglog(n,drift*0+ (0.16/0.16)*100,color=BAD,lw=2.4,label='relative error of expected return')
ax.loglog(n,vol*2,color=ACCENT,lw=2.4,label='relative error of variance')
ax.loglog(n,vol,color=GOOD,lw=2.4,ls='--',label='relative error of volatility')
for x,lab in [(251,'daily closes\n251 points'),(19578,'every 5 minutes\n19,578 points')]:
    ax.axvline(x,color=MUTED,ls=':',lw=1.1)
    ax.annotate(lab,xy=(x,180),fontsize=7,color=MUTED,ha='center')
ax.annotate('flat: more data buys nothing',xy=(3000,100),xytext=(400,38),fontsize=8,color=BAD,
            arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.annotate('4.46%',xy=(251,0.5*np.sqrt(2/251)*100),xytext=(8,8),textcoords='offset points',fontsize=7.5,color=GOOD)
ax.annotate('0.51%',xy=(19578,0.5*np.sqrt(2/19578)*100),xytext=(-34,-14),textcoords='offset points',fontsize=7.5,color=GOOD)
ax.set_xlabel('data points in one year');ax.set_ylabel('relative standard error (%)')
ax.set_title('Same data, same year: one line falls, the other never moves',loc='left')
ax.legend(fontsize=7,loc='lower left')
