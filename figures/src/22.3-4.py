def pool(psa=1.0,B=400.0,wac=0.08125,season=3,N=360):
    r=wac/12;out=[]
    for t in range(1,N-season+1):
        if B<=1e-12: break
        A=B*r/(1-(1+r)**-(N-season-t+1));P=A-B*r
        smm=1-(1-min(psa*0.002*(t+season),psa*0.06))**(1/12)
        pp=(B-P)*smm;out.append(P+pp);B-=P+pp
    return np.array(out)
def seq(Q,sizes=(194.5,36.0,96.5,73.0)):
    b=list(sizes);pay=np.zeros((len(Q),len(b)));bal=np.zeros((len(Q),len(b)))
    for t,q in enumerate(Q):
        for i in range(len(b)):
            x=min(q,b[i]);pay[t,i]=x;b[i]-=x;q-=x
        bal[t]=b
    return pay,bal
q100=pool(1.0);q250=pool(2.5);n=len(q100);S=np.minimum(q100,np.r_[q250,np.zeros(n-len(q250))])
def pac(Q):
    bp=S.sum();bs=400-bp;pp=[];ps=[]
    for t,q in enumerate(Q):
        st=S[t] if t<len(S) else 0
        a=min(q,st,bp) if bs>1e-12 else min(q,bp)
        bp-=a;q-=a;s=min(q,bs);bs-=s;q-=s
        if q>1e-12: x=min(q,bp);a+=x;bp-=x
        pp.append(a);ps.append(s)
    pp=np.array(pp);ps=np.array(ps);t=np.arange(1,len(Q)+1)
    return (t*pp).sum()/(12*pp.sum()),(t*ps).sum()/(12*ps.sum())
x=np.array([50,75,100,125,150,200,250,300,400]);v=np.array([pac(pool(s/100)) for s in x])
ax.axvspan(100,250,color=GOOD,alpha=.1,label='PAC band 100 to 250 PSA')
ax.plot(x,v[:,0],marker='o',color=GOOD,label='PAC (279.74)');ax.plot(x,v[:,1],marker='o',color=BAD,label='Support (120.26)')
ax.set_xlabel('Actual prepayment speed (PSA)');ax.set_ylabel('Average life (years)')
ax.set_title('Inside the band the PAC stays at 7.91 years; support absorbs the rest',loc='left');ax.legend(fontsize=7,loc='upper right');ax.grid(alpha=.2)
