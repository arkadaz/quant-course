rng=np.random.default_rng(37)
n,T=600,251
B=np.zeros((n,3)); B[:,0]=1
B[:,1]=rng.normal(0,1,n).round(2)
B[:,2]=(rng.random(n)<0.18).astype(float)
se=rng.uniform(0.012,0.030,n)
r=B@np.array([0.0040,-0.0025,0.0060])+rng.standard_normal(n)*se
W=np.diag(1/se**2)
fit=lambda x:np.linalg.solve(B.T@W@B,B.T@W@x)
base=fit(r)
def shocked(v):
    x=r.copy(); x[7]=v; return fit(x)
real,bad=shocked(-0.18),shocked(3.40)
lab=['market','momentum','industry']
xs=np.arange(3); w=0.26
ax.bar(xs-w,real*100,w,color=GOOD,label='with the real news  (-18%)')
ax.bar(xs,base*100,w,color=MUTED,label='a clean day')
ax.bar(xs+w,bad*100,w,color=BAD,label='with the bad price  (+340%)')
ax.axhline(0,color=INK,lw=.9)
for i in range(3):
    ax.annotate(f'{bad[i]*100:+.2f}',xy=(i+w,bad[i]*100),xytext=(0,-11 if bad[i]<0 else 4),
                textcoords='offset points',ha='center',fontsize=7.5,color=BAD)
    ax.annotate(f'{base[i]*100:+.2f}',xy=(i,base[i]*100),xytext=(0,4 if base[i]>0 else -11),
                textcoords='offset points',ha='center',fontsize=7.5,color=INK)
ax.annotate('one stock out of 600\nflips the whole day',xy=(1+w,-2.0),xytext=(1.45,-1.55),
            fontsize=8,color=BAD,arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.set_xticks(xs); ax.set_xticklabels(lab)
ax.set_ylabel('estimated factor return (percent)')
ax.set_title('One bad price moves the factors 22 times more than real news',loc='left')
ax.legend(frameon=False,fontsize=8,loc='lower left')
