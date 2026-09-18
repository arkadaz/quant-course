X,T=100.0,5
eta=1e-5*1e6
def path(c):
    A=np.zeros((T-1,T-1));b=np.zeros(T-1)
    for k in range(T-1):
        A[k,k]=2*eta+c
        if k>0: A[k,k-1]=-eta
        if k<T-2: A[k,k+1]=-eta
    b[0]=eta*X
    return np.concatenate([[X],np.linalg.solve(A,b),[0]])
d=np.arange(T+1)
for ls,col,lab in ((0,ACCENT,'0'),(1e-6,GOOD,'1e-6'),(3e-6,WARM,'3e-6'),(1e-5,BAD,'1e-5')):
    x=path(ls*1e6)
    ax.plot(d,x,'o-',color=col,lw=2,label=f'lambda sigma^2 = {lab}: day 1 sells {x[0]-x[1]:.1f}k')
ax.set_xlabel('Day');ax.set_ylabel('Shares still to sell (thousand)')
ax.set_title('Optimal schedules of the page model, 100,000 shares in 5 days',loc='left');ax.legend(fontsize=7.2);ax.grid(alpha=.2)
