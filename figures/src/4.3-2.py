A=np.array([[1.0,0.8,0.6],[0.3,0.5,0.2],[0.1,0.2,0.4]])
w=np.array([2,-1,1])
y=A@w
ax.bar(['Market','Quality','Rates'],y,color=[ACCENT,GOOD,WARM])
ax.axhline(0,color=MUTED,lw=0.8)
for i,v in enumerate(y): ax.text(i,v+(0.08 if v>=0 else -0.12),f'{v:.1f}',ha='center',va='bottom' if v>=0 else 'top')
ax.set_ylim(0,2.25)
ax.set_ylabel('factor exposure (USD million)')
ax.set_title('One row dot product per factor output',fontsize=9,loc='left')
