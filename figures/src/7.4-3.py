b=np.linspace(-0.4,1.4,260)
var=0.0009-2*b*0.00024+b*b*0.0004;vol=np.sqrt(var)*100
ix=np.argmin(var)
ax.plot(b,vol,color=ACCENT,lw=2)
ax.scatter([b[ix]],[vol[ix]],color=BAD,label=f'optimal beta = {b[ix]:.2f}, vol = {vol[ix]:.2f}%')
ax.set_xlabel('SPX short notional per unit of QQQ');ax.set_ylabel('residual daily volatility (%)');ax.legend(loc='upper left',fontsize=8)
ax.set_title('Beta 0.60 minimizes residual variance',fontsize=9,loc='left')
