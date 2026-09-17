a,b=0.5,1.5;phi=stats.norm.pdf;Phi=stats.norm.cdf
m1=2*(Phi(a)-0.5-a*phi(a))/(2*Phi(a)-1)
m2=2*((Phi(b)-b*phi(b))-(Phi(a)-a*phi(a)))/(2*(Phi(b)-Phi(a)))
m3=1+b*phi(b)/stats.norm.sf(b)
buckets=['|X|<0.5','0.5≤|X|<1.5','|X|≥1.5'];values=[m1,m2,m3]
ax.bar(buckets,values,color=[GOOD,ACCENT,BAD])
for i,v in enumerate(values): ax.text(i,v+0.08,f'{v:.3f}',ha='center',fontsize=8,color=INK)
ax.set_ylabel('E[Y | magnitude bucket]')
ax.set_title('Exact truncated-Normal moments reveal nonlinear tail exposure',fontsize=9,loc='left')
