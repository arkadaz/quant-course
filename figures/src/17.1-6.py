m=['multivariate normal','Student-t, 12 d.o.f.','mixture 75% / 25%']
var=[1.67,2.36,1.93];es=[3.15,4.58,5.60]
x=np.arange(3);w=.36
ax.bar(x-w/2,var,w,color=ACCENT,label='95% VaR');ax.bar(x+w/2,es,w,color=BAD,label='95% CVaR')
for xi,a,b in zip(x,var,es):
    ax.text(xi-w/2,a+.08,f'{a:.2f}%',ha='center',fontsize=7.5);ax.text(xi+w/2,b+.08,f'{b:.2f}%',ha='center',fontsize=7.5)
ax.set_xticks(x);ax.set_xticklabels(m,fontsize=8);ax.set_ylim(0,6.6)
ax.set_ylabel('Loss of the Sharpe-optimal portfolio (%)')
ax.set_title('Same mean and covariance, three different tails',loc='left');ax.legend(fontsize=7.5,loc='upper left');ax.grid(axis='y',alpha=.2)
