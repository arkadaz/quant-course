rng=np.random.default_rng(3)
T=300;shock=120
base=0.0035
vol=np.where(np.arange(T)<shock,base,base+2*base*np.exp(-(np.arange(T)-shock)/70))
vol[:shock]=base
corr=np.where(np.arange(T)<shock,0.30,0.30+0.15*(1-np.exp(-(np.arange(T)-shock)/12)))
corr[:shock]=0.30
fig=ax.figure;fig.delaxes(ax)
a1=fig.add_subplot(2,1,1)
a1.plot(vol*100,color=ACCENT,lw=2.4)
a1.axvline(shock,color=MUTED,ls=':',lw=1.4)
a1.annotate('trouble starts',xy=(shock,base*100),xytext=(6,4),textcoords='offset points',fontsize=7.5,color=MUTED)
a1.annotate('three times higher in two weeks',xy=(shock+10,vol[shock+10]*100),xytext=(150,0.95),
            fontsize=8,color=ACCENT,arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.9))
a1.set_ylabel('factor volatility (% per day)')
a1.set_title('Volatility sprints: it needs a short half-life',loc='left',fontsize=9)
a2=fig.add_subplot(2,1,2)
a2.plot(corr,color=GOOD,lw=2.4)
a2.axvline(shock,color=MUTED,ls=':',lw=1.4)
a2.annotate('0.30 to 0.45, then it stops',xy=(shock+40,corr[shock+40]),xytext=(160,0.34),
            fontsize=8,color=GOOD,arrowprops=dict(arrowstyle='->',color=GOOD,lw=.9))
a2.set_ylim(0.25,0.50)
a2.set_xlabel('trading day');a2.set_ylabel('average correlation')
a2.set_title('Correlation strolls: it needs a long one',loc='left',fontsize=9)
