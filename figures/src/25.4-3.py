rng=np.random.default_rng(21)
se,sn,M=0.0256,0.012,390
eps=se*rng.standard_normal(M)
m=np.concatenate([[0.0],np.cumsum(eps)])
p=m+sn*rng.standard_normal(M+1)
true=M*se**2
for q,col,lab in ((1,BAD,'every 1 minute'),(5,WARM,'every 5 minutes'),(30,GOOD,'every 30 minutes')):
    idx=np.arange(0,M+1,q)
    d=np.diff(p[idx])
    cum=np.cumsum(d**2)
    ax.plot(idx[1:],cum,color=col,lw=2.0,label=lab)
    ax.annotate(f'{cum[-1]:.2f}',xy=(idx[-1],cum[-1]),xytext=(6,-3),textcoords='offset points',fontsize=8,color=col)
ax.axhline(true,color=INK,ls='--',lw=1.6)
ax.annotate(f'the day\'s true variance, {true:.2f}',xy=(40,true),xytext=(0,7),
            textcoords='offset points',fontsize=8,color=INK)
ax.set_xlabel('minute of the trading day');ax.set_ylabel('sum of squared moves so far (USD squared)')
ax.set_title('One price path, three sampling rates, three different answers',loc='left')
ax.legend(fontsize=7,loc='upper left')
