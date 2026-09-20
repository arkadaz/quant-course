rng=np.random.default_rng(37)
n,T=600,251
B=np.zeros((n,3)); B[:,0]=1
B[:,1]=rng.normal(0,1,n).round(2)
B[:,2]=(rng.random(n)<0.18).astype(float)
se=rng.uniform(0.012,0.030,n)
r=B@np.array([0.0040,-0.0025,0.0060])+rng.standard_normal(n)*se
hist=rng.standard_normal((n,T))*se[:,None]
z=np.abs(np.log1p(hist))/np.median(np.abs(np.log1p(hist)),axis=1)[:,None]
ths=np.arange(2.0,9.01,0.25)
pct=np.array([(z>t).mean()*100 for t in ths])
floor=1/(n*T)*100*0.4
ax.semilogy(ths,np.maximum(pct,floor),color=ACCENT,lw=2.4)
ax.axvspan(5,10,color=GRID,alpha=.9,zorder=0)
for t,txt in ((3,'4.45% = 6,708 clean points edited'),(5,'0.11% = 163 points')):
    v=(z>t).mean()*100
    ax.plot([t],[v],'o',color=ACCENT,ms=5)
    ax.annotate(txt,xy=(t,v),xytext=(8,6),textcoords='offset points',fontsize=8,color=INK)
ax.annotate('nothing clean is touched\nfrom about 8 upward',xy=(8.2,floor),xytext=(5.4,0.0015),
            fontsize=8,color=MUTED,arrowprops=dict(arrowstyle='->',color=MUTED,lw=.9))
ax.annotate('what people use',xy=(6.6,3.0),ha='center',fontsize=8,color=MUTED)
ax.set_xlabel('threshold on the robust score')
ax.set_ylabel('share of clean stock-days flagged, percent (log scale)')
ax.set_title('Read the threshold off your own clean data',loc='left')
ax.set_xlim(2,9)
