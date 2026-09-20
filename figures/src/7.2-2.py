A=np.array([[1.2,0.4],[0.9,0.2],[1.5,0.7]])
B=A.T
ax.imshow(B,cmap='Oranges',vmin=0,vmax=1.6)
ax.set_xticks([0,1,2],['AAPL','MSFT','SPY'])
ax.set_yticks([0,1],['Market','Quality'])
for i in range(2):
    for j in range(3): ax.text(j,i,f'{B[i,j]:.1f}',ha='center',va='center',color=INK,weight='bold')
ax.set_title('Aᵀ: factors by rows, assets by columns',fontsize=9,loc='left')
