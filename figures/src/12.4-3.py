rng=np.random.default_rng(7);k=.8;th=.03;r0=.015;T=5;n=5*252;dt=T/n;t=np.linspace(0,T,n+1)
def paths(sc,m):
    r=np.full((m,n+1),r0)
    z=rng.standard_normal((m,n))
    for i in range(n):
        x=np.maximum(r[:,i],0);r[:,i+1]=np.maximum(r[:,i]+k*(th-x)*dt+sc*np.sqrt(x*dt)*z[:,i],0)
    return r
lo=paths(.10,2000);hi=paths(.25,2000)
f_lo=(lo.min(1)<=1e-9).mean();f_hi=(hi.min(1)<=1e-9).mean()
for j in range(3):ax.plot(t,lo[j]*100,color=GOOD,lw=1,alpha=.9,label='σ_C = 0.10 (ratio 4.8)' if j==0 else None)
for j in range(3):ax.plot(t,hi[j]*100,color=BAD,lw=1,alpha=.8,label='σ_C = 0.25 (ratio 0.77)' if j==0 else None)
ax.axhline(0,color=INK,lw=.8);ax.set_xlabel('Years');ax.set_ylabel('Short rate (%)')
ax.set_title(f'Paths touching zero within 5 years: {f_lo:.1%} vs {f_hi:.1%}',loc='left');ax.legend(fontsize=8,loc='upper right')
print('touch', f_lo, f_hi)
