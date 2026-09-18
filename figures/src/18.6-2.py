eq=np.array([20,20,20,20,20.]);fr=np.array([40,30,20,10,0.])
imp=lambda v:1e-5*np.sum((v*1000)**2)
risk=lambda v:np.sum((100-np.concatenate([[0],np.cumsum(v)[:-1]]))**2)*1e6
x=np.arange(2);w=.36
for i,(ls,col) in enumerate(((1e-6,GOOD),(3e-6,WARM))):
    tot=[imp(eq)+ls*risk(eq),imp(fr)+ls*risk(fr)]
    ax.bar(x+(i-.5)*w,tot,w,color=col,label=f'lambda sigma^2 = {ls:g}')
    for xi,t in zip(x+(i-.5)*w,tot): ax.text(xi,t+1500,f'{t:,.0f}',ha='center',fontsize=7.5)
ax.bar(x,[imp(eq),imp(fr)],.12,color=INK,label='impact part')
ax.set_xticks(x);ax.set_xticklabels(['equal 20k a day','front 40,30,20,10,0k'])
ax.set_ylabel('Score J (USD)');ax.set_ylim(0,112000)
ax.set_title('Who wins depends only on lambda sigma^2',loc='left');ax.legend(fontsize=7,loc='upper center',ncol=3);ax.grid(axis='y',alpha=.2)
