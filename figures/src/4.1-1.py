A=np.array([[1.2,0.4],[0.9,0.2],[1.5,0.7]])
ax.imshow(A,cmap='Blues',vmin=0,vmax=1.6)
ax.set_xticks([0,1],['Market factor','Quality factor'])
ax.set_yticks([0,1,2],['AAPL','MSFT','JPM'])
for i in range(3):
    for j in range(2): ax.text(j,i,f'{A[i,j]:.1f}',ha='center',va='center',color=INK,weight='bold')
ax.set_xlabel('columns: factors')
ax.set_ylabel('rows: assets')
ax.set_title('A is a table of unitless asset-to-factor loadings',fontsize=9,loc='left')
