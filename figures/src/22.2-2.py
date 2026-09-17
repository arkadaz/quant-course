m=np.arange(1,61);B0=100e6;r=.06/12;A=B0*r/(1-(1+r)**-360);out=[]
for k in [0,1,2]:
 b=B0;cf=[]
 for t in m:
  sp=A-r*b;bstar=b-sp;cpr=k*min(.002*t,.06);smm=1-(1-cpr)**(1/12);pp=smm*bstar;cf.append(sp+pp);b=bstar-pp
 out.append(np.array(cf)/1e6)
ax.plot(m,out[0],label='0 PSA',color=MUTED);ax.plot(m,out[1],label='100 PSA',color=ACCENT);ax.plot(m,out[2],label='200 PSA',color=BAD);ax.set_xlabel('Month');ax.set_ylabel('Principal cash flow (USD M)');ax.set_title('Prepayment pulls cash forward',loc='left');ax.legend();ax.grid(alpha=.25)
