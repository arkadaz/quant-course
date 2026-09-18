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
Q=pool();pay,bal=seq(Q);m=np.arange(1,len(Q)+1)
t=m[:,None];w=(t*pay).sum(0)/(12*pay.sum(0))
for i,(n,c) in enumerate(zip('ABCD',[ACCENT,GOOD,WARM,'#7C3AED'])):
    ax.plot(m/12,bal[:,i],color=c,lw=1.8,label=f'{n}: average life {w[i]:.2f} years')
    ax.axvline(w[i],color=c,ls=':',lw=1)
ax.set_xlabel('Years');ax.set_ylabel('Outstanding balance (USD M)')
ax.set_title('Same pool (average life 11.67), four very different maturities',loc='left');ax.legend(fontsize=7,loc='upper right');ax.grid(alpha=.2)
