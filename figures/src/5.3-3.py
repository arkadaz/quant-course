A=np.array([[1.0,0.8,0.6],[0.3,0.5,0.2],[0.1,0.2,0.4]])
ax.imshow(A,cmap='RdBu_r',vmin=0,vmax=1)
ax.set_xticks([0,1,2],['AAPL','MSFT','JPM'])
ax.set_yticks([0,1,2],['Market','Quality','Rates'])
for i in range(3):
    for j in range(3): ax.text(j,i,f'{A[i,j]:.1f}',ha='center',va='center',color=INK)
ax.set_title('A: factor rows by asset columns',fontsize=9,loc='left')
