rng=np.random.default_rng(2)
n,m,T=500,60,251
Bn=rng.normal(0,1,(n,m))
R=Bn@rng.normal(0,0.01,(m,T))+rng.normal(0,0.02,(n,T))
emp=R@R.T/T
null=np.linalg.svd(R.T)[2][T:]
w0=null[0]
true=Bn@(np.eye(m)*1e-4)@Bn.T+np.eye(n)*4e-4
fac_pred=np.sqrt(w0@true@w0)
vals=[max(np.sqrt(abs(w0@emp@w0)),1e-6)*100,fac_pred*100,fac_pred*100]
labs=['empirical covariance\nfrom 251 days','factor model','the truth']
bars=ax.bar(range(3),vals,color=[BAD,ACCENT,INK],width=.55)
for b,v in zip(bars,vals):
    ax.annotate('0.000%' if v<1e-3 else f'{v:.3f}%',xy=(b.get_x()+b.get_width()/2,v),
                xytext=(0,6),textcoords='offset points',fontsize=9,ha='center')
ax.annotate('an optimizer will pour unlimited\nmoney into this portfolio',
            xy=(0,vals[0]),xytext=(0.15,vals[1]*0.62),fontsize=8,color=BAD,
            arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.set_xticks(range(3));ax.set_xticklabels(labs,fontsize=8)
ax.set_ylabel('predicted daily volatility of one portfolio (%)')
ax.set_title('The same portfolio, scored by three different models',loc='left')
