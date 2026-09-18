f=lambda w: 3*w**4-4*w**3-36*w**2; fp=lambda w: 12*w**3-12*w**2-72*w
w=np.linspace(-3.0,4.0,500); ax.plot(w,f(w),color=MUTED,lw=1.6)
for w0,c,lab in [(-1.0,WARM,'run a: start -1'),(1.0,GOOD,'run b: start +1')]:
    path=[w0]
    for _ in range(12): path.append(path[-1]-0.005*fp(path[-1]))
    path=np.array(path); ax.plot(path,f(path),'o-',color=c,ms=4,lw=1.2,label=lab)
    ax.annotate(f'profit {-f(path[-1]):.0f}M',xy=(path[-1],f(path[-1])),xytext=(path[-1]-0.6 if w0>0 else path[-1]-0.4,f(path[-1])-38),color=c,fontsize=9)
ax.axvline(0,color=MUTED,ls='--',lw=1); ax.text(0.08,40,'ridge w = 0',color=MUTED,fontsize=9)
ax.set_xlabel('Signal weight, $w$'); ax.set_ylabel('Backtest loss (USD million)'); ax.set_ylim(-235,80)
ax.legend(loc='upper left'); ax.set_title('Same code, same data: the start picks the valley',loc='left')
