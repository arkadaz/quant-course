labels=['0','50','100']
one=[97.0,0,3.0];two=[94.09,5.82,0.09]
x=np.arange(3);w=.36
ax.bar(x-w/2,one,w,color=ACCENT,label='100M in one bond: VaR 0, ES 60')
ax.bar(x+w/2,two,w,color=WARM,label='50M in each of two: VaR 50, ES 50.9')
for xi,a,b in zip(x,one,two):
    ax.text(xi-w/2,a+1.5,f'{a:.2f}%',ha='center',fontsize=7.2);ax.text(xi+w/2,b+1.5,f'{b:.2f}%',ha='center',fontsize=7.2)
ax.axhline(5,color=BAD,ls=':',lw=1);ax.text(0.42,7,'5% tail',color=BAD,fontsize=7.5)
ax.set_xticks(x);ax.set_xticklabels(labels);ax.set_ylim(0,110)
ax.set_xlabel('Loss (USD million), default probability 3% each');ax.set_ylabel('Probability (%)')
ax.set_title('Splitting the bet raises VaR but lowers ES',loc='left');ax.legend(fontsize=7,loc='upper right');ax.grid(axis='y',alpha=.2)
