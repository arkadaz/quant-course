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
ax.stackplot(m/12,pay.T,labels=['A (194.5)','B (36.0)','C (96.5)','D (73.0)'],colors=[ACCENT,GOOD,WARM,'#7C3AED'],alpha=.85)
ax.set_xlabel('Years');ax.set_ylabel('Principal paid per month (USD M)')
ax.set_title('Course workbook, 100 PSA: all principal goes to one tranche at a time',loc='left');ax.legend(fontsize=7,loc='upper right');ax.grid(alpha=.2)
