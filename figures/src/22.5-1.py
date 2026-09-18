d=np.linspace(0,0.4,200)
for e0,c in ((0.05,BAD),(0.10,WARM),(0.20,ACCENT)):
    ax.plot(100*d,100*(1-e0)/(1-d),color=c,lw=1.8,label=f'Down payment {100*e0:.0f}%')
ax.axhline(100,color='0.4',ls='--',lw=1)
ax.scatter([20],[100*0.95/0.8],color=INK,s=20,zorder=3);ax.annotate('5% down, prices -20%: LTV 118.75%',(20,118.75),xytext=(21,135),fontsize=7,arrowprops=dict(arrowstyle='-',color='0.4',lw=.8))
ax.text(1,102,'LTV 100%: the house is worth exactly the loan',fontsize=7,color='0.3')
ax.set_xlabel('House price decline (%)');ax.set_ylabel('Loan-to-value (%)');ax.set_ylim(60,165)
ax.set_title('Negative equity starts as soon as the price fall exceeds the down payment',loc='left');ax.legend(fontsize=7,loc='upper left');ax.grid(alpha=.2)
