def gain(kappa,a=1.0):
    te,tn=1.0,kappa
    A=(a*a-1)*tn**2+te**2
    s2=0.5*(A+np.sqrt(A*A+4*tn**2*te**2))
    return s2/(s2+tn**2)
kk=np.logspace(-1,2,400)
for a,col,lab in ((1.00,ACCENT,'no mean reversion (a = 1.00)'),
                  (0.95,WARM,'a = 0.95'),
                  (0.90,GOOD,'a = 0.90'),
                  (0.80,BAD,'a = 0.80')):
    ax.loglog(kk,[gain(x,a) for x in kk],color=col,lw=2.0,label=lab)
k0=16.1589
ax.plot(k0,gain(k0),'o',color=INK,ms=7)
ax.annotate('kappa = 16.16 gives K = 0.06,\nwhich is lambda = 0.94',xy=(k0,gain(k0)),xytext=(1.3,0.012),
            fontsize=8,color=INK,arrowprops=dict(arrowstyle='->',color=INK,lw=.9))
ax.set_xlabel('noise divided by true change, per day');ax.set_ylabel('weight given to the new observation')
ax.set_title('Mean reversion makes you look further back, not less far',loc='left')
ax.legend(fontsize=7,loc='lower left')
