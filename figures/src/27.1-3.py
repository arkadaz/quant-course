sig=np.array([1.8,2.2,1.5,2.6,2.0,2.4,1.7,2.1])
w=1/sig**2; w=w/w.sum()*8
x=np.arange(8)
ax.bar(x-0.19,np.ones(8),width=.36,color=GRID,edgecolor=MUTED,label='equal weights (OLS)')
ax.bar(x+0.19,w,width=.36,color=ACCENT,label='one over idio variance (WLS)')
for i in range(8):
    ax.annotate(f'{sig[i]:.1f}%',xy=(i,0),xytext=(0,-16),textcoords='offset points',
                fontsize=7,ha='center',color=MUTED)
lo,hi=int(np.argmin(sig)),int(np.argmax(sig))
ax.annotate(f'quietest gets {w[lo]/w[hi]:.2f}x\nthe weight of the loudest',
            xy=(lo+0.19,w[lo]),xytext=(3.4,1.62),fontsize=8,color=ACCENT,
            arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.9))
ax.set_xticks(x);ax.set_xticklabels([f'{i+1}' for i in range(8)])
ax.set_xlabel('stock (idio volatility below)');ax.set_ylabel('relative weight in the regression')
ax.set_ylim(0,1.95)
ax.set_title('A quiet stock says more about the factors than a wild one',loc='left')
ax.legend(fontsize=7,loc='upper left')
