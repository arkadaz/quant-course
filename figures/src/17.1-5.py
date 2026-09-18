m=['normal formula','historical 1,000 days','Student-t(4), 100,000 paths']
var=[13.96,15.75,16.40];es=[15.99,19.60,22.10]
x=np.arange(3);w=.36
ax.bar(x-w/2,var,w,color=ACCENT,label='VaR 99%');ax.bar(x+w/2,es,w,color=BAD,label='ES 99%')
for xi,a,b in zip(x,var,es):
    ax.text(xi-w/2,a+.4,f'{a:.2f}',ha='center',fontsize=7.5);ax.text(xi+w/2,b+.4,f'{b:.2f}',ha='center',fontsize=7.5)
ax.set_xticks(x);ax.set_xticklabels(m,fontsize=7.8);ax.set_ylim(0,26)
ax.set_ylabel('One-day loss on 500M USD (USD million)')
ax.set_title('VaR moves 17% across methods, ES moves 38%',loc='left');ax.legend(fontsize=7.5,loc='upper left');ax.grid(axis='y',alpha=.2)
