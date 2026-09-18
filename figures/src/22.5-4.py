D,h,V0=95.0,0.15,97.0
for a,c in ((0.0,'0.5'),(0.25,ACCENT),(0.5,WARM),(1.0,BAD)):
    V=[V0]
    for _ in range(10):
        q=min(max((D-(1-h)*V[-1])/V[-1],0),1) if V[-1]>0 else 0;V.append(V[-1]*(1-a*q))
    ax.plot(range(11),V,marker='o',ms=3,color=c,lw=1.6,label=f'price impact alpha = {a:g}')
ax.axhline(D,color=INK,ls='--',lw=1);ax.text(7,97,'repo debt 95',fontsize=7)
ax.set_xlabel('Round of forced selling');ax.set_ylabel('Asset value V (USD M)')
ax.set_title('Selling pushes marks down, which forces more selling',loc='left');ax.legend(fontsize=7,loc='lower left');ax.grid(alpha=.2)
