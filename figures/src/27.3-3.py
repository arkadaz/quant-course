k=np.arange(2,201)
err=0.5*np.sqrt(2/k)*100
ax.loglog(k,err,color=ACCENT,lw=2.4)
ax.plot(40,0.5*np.sqrt(2/40)*100,'o',color=INK,ms=9)
ax.annotate('40 factors in one day\nor 40 days of one factor:\nboth give 11.2%',
            xy=(40,0.5*np.sqrt(2/40)*100),xytext=(52,26),fontsize=8.5,color=INK,
            arrowprops=dict(arrowstyle='->',color=INK,lw=.9))
ax.set_xlabel('number of independent observations\n(read it either way: factors today, or days of one factor)')
ax.set_ylabel('relative error of the volatility estimate (%)')
ax.set_title('The formula does not care which axis the data came from',loc='left')
