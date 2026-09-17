t=np.linspace(0,5,100)
parent=20*t
marketable=12*t
passive=8*t
ax.plot(t,parent,color=ACCENT,lw=2,label='Parent: 20t')
ax.plot(t,marketable,color=GOOD,lw=2,label='A: 12t')
ax.plot(t,passive,color=WARM,lw=2,label='B: 8t')
ax.plot(t,marketable+passive,color=BAD,ls='--',lw=1.2,label='A + B')
ax.set_xlabel('time (minutes)')
ax.set_ylabel('expected cumulative orders')
ax.legend(loc='upper left',ncol=2)
ax.set_title('Child streams conserve the parent count over time',fontsize=9,loc='left')
