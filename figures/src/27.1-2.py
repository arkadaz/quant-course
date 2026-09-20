ind=np.array([0,0,0,1,1,2,2,2])
B=np.zeros((8,5));B[:,0]=1;B[np.arange(8),1+ind]=1
B[:,4]=[1.2,-0.4,0.6,-1.4,0.9,-0.7,0.3,-0.5]
r=np.array([1.20,0.35,0.90,-0.60,0.25,-1.10,-0.40,-0.95])/100
sig=np.array([1.8,2.2,1.5,2.6,2.0,2.4,1.7,2.1]);W=np.diag(1/sig**2)
cap=np.array([300.,180,220,400,150,260,340,190])
Bd=np.delete(B,3,axis=1);fd=np.linalg.solve(Bd.T@W@Bd,Bd.T@W@r)
cw=np.array([cap[ind==g].sum() for g in range(3)]);cw=cw/cw.sum()
c=np.zeros(5);c[1:4]=cw
A=np.zeros((6,6));A[:5,:5]=B.T@W@B;A[:5,5]=c;A[5,:5]=c
rhs=np.zeros(6);rhs[:5]=B.T@W@r
fc=np.linalg.solve(A,rhs)[:5]
full_d=np.insert(fd,3,0.0)
fig=ax.figure;fig.delaxes(ax)
a1=fig.add_subplot(1,2,1)
x=np.arange(5)
a1.bar(x-0.19,full_d*100,width=.36,color=WARM,label='drop the energy column')
a1.bar(x+0.19,fc*100,width=.36,color=ACCENT,label='cap-weighted constraint')
a1.axhline(0,color=INK,lw=.9)
for i in range(4):
    a1.annotate('0.58',xy=(i,max(full_d[i],fc[i])*100),xytext=(0,6),textcoords='offset points',
                fontsize=6.5,ha='center',color=MUTED)
a1.annotate('identical',xy=(4,fc[4]*100),xytext=(0,8),textcoords='offset points',
            fontsize=7.5,ha='center',color=GOOD)
a1.set_xticks(x);a1.set_xticklabels(['market','tech','banks','energy','mom'],fontsize=7.5,rotation=20)
a1.set_ylabel('factor return today (%)')
a1.set_title('Different numbers',loc='left',fontsize=9)
a1.legend(fontsize=6.5,loc='lower left')
a2=fig.add_subplot(1,2,2)
a2.plot(range(1,9),(Bd@fd)*100,'o-',color=WARM,ms=9,lw=2,label='drop a column')
a2.plot(range(1,9),(B@fc)*100,'x',color=ACCENT,ms=9,mew=2.4,label='constraint')
a2.plot(range(1,9),r*100,'.',color=INK,ms=5,label='what actually happened')
a2.axhline(0,color=GRID,lw=1)
a2.set_xlabel('stock');a2.set_ylabel('predicted return (%)')
a2.set_title('Identical predictions',loc='left',fontsize=9)
a2.legend(fontsize=6.5,loc='lower left')
