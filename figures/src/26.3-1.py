B=np.array([[1,1.2,1],[1,-0.4,1],[1,0.6,0],[1,-1.4,0]],float)
f=np.array([0.008,-0.005,0.003]);w=np.array([3.,-2.,4.,-5.])
sf=np.array([0.010,0.0035,0.0055])
Of=np.outer(sf,sf)*np.array([[1,-.20,.50],[-.20,1,-.10],[.50,-.10,1]])
b=B.T@w
U,S,_=np.linalg.svd(Of);C=np.diag(S**-0.5)@U.T
Bt=B@np.linalg.inv(C);ft=C@f;bt=Bt.T@w
old=b*f*1e3; new=bt*ft*1e3
fig=ax.figure;fig.delaxes(ax)
for k,(vals,title,names) in enumerate((
        (old,'as written: blame momentum',['market','momentum','tech']),
        (new,'after rotating: blame factor 3',['rotated 1','rotated 2','rotated 3']))):
    a2=fig.add_subplot(1,2,k+1)
    cols=[BAD if v<-30 else (MUTED if abs(v)<5 else WARM) for v in vals]
    a2.bar(range(3),vals,color=cols,width=.55)
    a2.bar([3],[vals.sum()],color=INK,width=.55)
    for i,v in enumerate(list(vals)+[vals.sum()]):
        a2.annotate(f'{v:+,.0f}',xy=(i,v),xytext=(0,-13 if v<0 else 5),
                    textcoords='offset points',fontsize=7.5,ha='center')
    a2.axhline(0,color=INK,lw=.9)
    a2.set_xticks(range(4));a2.set_xticklabels(names+['total'],fontsize=7,rotation=20,ha='right')
    a2.set_ylim(-78,18)
    if k==0: a2.set_ylabel('factor PnL (USD thousand)')
    a2.set_title(title,loc='left',fontsize=9)
