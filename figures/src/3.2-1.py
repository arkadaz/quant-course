u=np.array([2.0,0.7]); v=np.array([0.7,1.8])
for a in [-1,0,1]:
    for b in [-1,0,1]:
        p=a*u+b*v
        ax.plot(p[0],p[1],'o',color=ACCENT,alpha=0.55,ms=4)
ax.quiver(0,0,u[0],u[1],angles='xy',scale_units='xy',scale=1,color=GOOD,width=0.008)
ax.quiver(0,0,v[0],v[1],angles='xy',scale_units='xy',scale=1,color=WARM,width=0.008)
ax.text(u[0]+.08,u[1],'u',color=GOOD,fontsize=10)
ax.text(v[0]+.08,v[1],'v',color=WARM,fontsize=10)
ax.set_aspect('equal')
ax.set_xlim(-3.2,3.2); ax.set_ylim(-2.8,2.8)
ax.set_xlabel('Exposure axis 1'); ax.set_ylabel('Exposure axis 2')
ax.set_title('Independent vectors reach a two-dimensional span',loc='left')
