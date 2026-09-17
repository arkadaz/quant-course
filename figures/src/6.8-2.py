w=np.linspace(0,1,400);var1,var2,cov=0.0004,0.0009,0.00012
var=w*w*var1+(1-w)**2*var2+2*w*(1-w)*cov
ix=np.argmin(var);var_bp2=var*1e8
ax.plot(w,var_bp2,color=ACCENT,lw=2)
ax.scatter([w[ix]],[var_bp2[ix]],color=BAD,zorder=3,label=f'minimum w = {w[ix]:.2f}')
ax.set_xlabel('weight in SPY');ax.set_ylabel('portfolio variance (bp²)')
ax.legend(loc='upper right');ax.set_title('Quadratic risk along a two-asset mix',fontsize=9,loc='left')
