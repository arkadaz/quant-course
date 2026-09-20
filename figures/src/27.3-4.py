T=60;tau=4
days=np.arange(T)
earn=[14,28,41]
fig=ax.figure;fig.delaxes(ax)
a1=fig.add_subplot(2,1,1)
cols=[ACCENT,WARM,GOOD]
for e,c,nm in zip(earn,cols,['stock A','stock B','stock C']):
    a1.plot(days,np.maximum(0,1-np.abs(days-e)/tau),color=c,lw=2.2,label=nm)
    a1.axvline(e,color=c,ls=':',lw=1)
a1.set_ylabel('tent value');a1.set_ylim(-0.05,1.15)
a1.set_title('One tent per stock, opened around its own announcement',loc='left',fontsize=9)
a1.legend(fontsize=6.5,loc='upper right',ncol=3)
a2=fig.add_subplot(2,1,2)
mult=2.2
for e,c,nm in zip(earn,cols,['stock A','stock B','stock C']):
    a=np.maximum(0,1-np.abs(days-e)/tau)
    a2.plot(days,np.sqrt((1-a)+a*mult),color=c,lw=2.2)
a2.axhline(1,color=INK,lw=1)
a2.annotate('every other day: exactly unchanged',xy=(52,1.0),xytext=(0,6),
            textcoords='offset points',fontsize=7.5,color=MUTED,ha='right')
a2.set_xlabel('trading day');a2.set_ylabel('idio volatility multiplier')
a2.set_ylim(0.9,1.6)
a2.set_title('So the other stocks are never touched',loc='left',fontsize=9)
