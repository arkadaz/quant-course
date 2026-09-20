theta=np.linspace(0,2*np.pi,200)
S=np.array([[0.0004,0.00024],[0.00024,0.0009]])
q=[]
for t in theta:
    x=np.array([np.cos(t),np.sin(t)]); q.append(x@S@x*1e8)
ax.plot(theta,q,color=GOOD,lw=2)
ax.axhline(0,color=BAD,ls='--',lw=1)
ax.set_xlabel('unit-vector direction angle (radians)');ax.set_ylabel('xᵀΣx ((basis points)²)')
ax.set_title('Positive definiteness means positive risk in every direction',fontsize=9,loc='left')
