starts=np.array([-3.,-1.,1.,4.]);ends=np.array([-2.,-2.,3.,3.]);yy=np.arange(4)
for i,(s,e) in enumerate(zip(starts,ends)): ax.annotate('',xy=(e,i),xytext=(s,i),arrowprops=dict(arrowstyle='->',lw=2,color=ACCENT if e<0 else GOOD))
ax.scatter(starts,yy,color=WARM,s=36,label='start');ax.scatter(ends,yy,color=GOOD,s=36,label='finish');ax.set_xlabel('Signal weight, $w$');ax.legend();ax.set_title('Local search follows its starting basin',loc='left')
