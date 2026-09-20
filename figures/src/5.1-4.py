A=np.array([[1.2,0.4],[0.9,0.2],[1.5,0.7]])
w=np.array([2.0,-1.0,0.5])
vals=A.T@w
ax.bar(['Market factor','Quality factor'],vals,color=[ACCENT,WARM])
for i,v in enumerate(vals): ax.text(i,v+0.04,f'{v:.2f}',ha='center',fontsize=8)
ax.set_ylabel('portfolio factor exposure (USD million)')
ax.set_title('Weighted aggregation reveals factor concentration',fontsize=9,loc='left')
