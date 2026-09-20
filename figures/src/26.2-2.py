n=np.logspace(1.7,4.4,300)
mu,sig=0.020,0.35
ax.semilogx(n,np.sqrt(n)*mu/sig,color=ACCENT,lw=2.4,label='bet on alpha orthogonal')
ax.axhline(0.030/0.080,color=WARM,lw=2.4,label='bet on momentum (0.375, always)')
for N in (100,500,2000,8000):
    ax.plot(N,np.sqrt(N)*mu/sig,'o',color=INK,ms=5)
    ax.annotate(f'{np.sqrt(N)*mu/sig:.2f}',xy=(N,np.sqrt(N)*mu/sig),xytext=(4,7),
                textcoords='offset points',fontsize=7.5,color=INK)
ax.annotate('four times the universe,\ntwice the Sharpe',xy=(2000,2.556),xytext=(120,3.6),fontsize=8,color=ACCENT,
            arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.9))
ax.annotate('buying more stocks does not\nmake one bet into many',xy=(6000,0.375),xytext=(1500,0.75),fontsize=8,color=WARM,
            arrowprops=dict(arrowstyle='->',color=WARM,lw=.9))
ax.set_xlabel('stocks in the universe');ax.set_ylabel('Sharpe Ratio per year')
ax.set_ylim(0,5.6)
ax.set_title('Two kinds of alpha, priced by how they scale',loc='left')
ax.legend(fontsize=7,loc='upper left')
