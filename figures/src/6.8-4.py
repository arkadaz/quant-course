S=np.array([[0.0004,0.00008,0.00012],[0.00008,0.0009,0.00018],[0.00012,0.00018,0.0006]])*1e8
w=np.array([0.4,0.3,0.3]);C=np.outer(w,w)*S;total=C.sum()
ax.imshow(C,cmap='Oranges')
ax.set_xticks([0,1,2],['SPY','AAPL','JPM']);ax.set_yticks([0,1,2],['SPY','AAPL','JPM'])
for i in range(3):
    for j in range(3):
        colour='white' if C[i,j]>=5000 else INK
        ax.text(j,i,f'{C[i,j]:,.0f}',ha='center',va='center',color=colour)
ax.set_title(f'Weighted covariance contributions; total = {total:,.0f} bp²',fontsize=9,loc='left')
