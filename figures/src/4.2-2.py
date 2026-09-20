u=np.array([1.,2.]); v=2*u
ax.quiver(0,0,u[0],u[1],angles='xy',scale_units='xy',scale=1,color=ACCENT,width=0.010,label='u')
ax.quiver(0,0,v[0],v[1],angles='xy',scale_units='xy',scale=1,color=BAD,width=0.010,label='v = 2u')
ax.plot([-1.2,2.5],[-2.4,5.0],color=MUTED,ls='--',lw=1)
ax.set_aspect('equal'); ax.set_xlim(-1.4,2.8); ax.set_ylim(-2.7,5.4)
ax.set_xlabel('Exposure axis 1'); ax.set_ylabel('Exposure axis 2')
ax.legend(loc='upper left')
ax.set_title('One direction, two position sizes',loc='left')
