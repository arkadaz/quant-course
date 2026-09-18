X,T=100.0,5;eta=10.0
def path(c):
    A=np.zeros((T-1,T-1));b=np.zeros(T-1)
    for k in range(T-1):
        A[k,k]=2*eta+c
        if k>0: A[k,k-1]=-eta
        if k<T-2: A[k,k+1]=-eta
    b[0]=eta*X
    return np.concatenate([[X],np.linalg.solve(A,b),[0]])
cs=np.concatenate([[0],np.logspace(-2,2,200)])
imp=[];rsk=[]
for c in cs:
    x=path(c);v=-np.diff(x);imp.append(eta*np.sum(v**2)/1000);rsk.append(np.sum(x[:-1]**2)/1000)
ax.plot(imp,rsk,color=ACCENT,lw=2,label='optimal schedules')
for c,col,lab in ((0,GOOD,'lambda sigma^2 = 0'),(1,WARM,'1e-6'),(3,BAD,'3e-6')):
    x=path(c);v=-np.diff(x);ax.scatter([eta*np.sum(v**2)/1000],[np.sum(x[:-1]**2)/1000],color=col,zorder=3,s=34,label=lab)
ax.scatter([30.0],[14.6],marker='x',color=INK,s=40,zorder=3,label='front 40,30,20,10,0k')
ax.set_xlabel('Impact cost (USD thousand)');ax.set_ylabel('Sum of inventory squared (10^9 shares^2)')
ax.set_title('Execution frontier of the page model',loc='left');ax.legend(fontsize=7.2);ax.grid(alpha=.2)
