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
q100=pool(1.0);q250=pool(2.5);q50=pool(0.5)
n=len(q100);q250=np.r_[q250,np.zeros(n-len(q250))];S=np.minimum(q100,q250)
m=np.arange(1,n+1);k=240
ax.plot(m[:k]/12,q100[:k],color=ACCENT,lw=1.2,label='Collateral at 100 PSA')
ax.plot(m[:k]/12,q250[:k],color=WARM,lw=1.2,label='Collateral at 250 PSA')
ax.plot(m[:k]/12,q50[:k],color=BAD,lw=1.2,ls='--',label='Collateral at 50 PSA (slow)')
ax.plot(m[:k]/12,S[:k],color=GOOD,lw=2.4,label=f'PAC schedule = lower of the two ({S.sum():.2f})')
ax.set_xlabel('Years');ax.set_ylabel('Principal per month (USD M)')
ax.set_title('PAC schedule: what the pool can pay at both ends of the band',loc='left');ax.legend(fontsize=7,loc='upper right');ax.grid(alpha=.2)
