S=np.array([[0.0004,0.00024],[0.00024,0.0009]]);L=np.linalg.cholesky(S)*100
ax.imshow(L,cmap='Blues',vmin=0,vmax=3)
ax.set_xticks([0,1],['shock 1','shock 2']);ax.set_yticks([0,1],['SPX','QQQ'])
for i in range(2):
    for j in range(2): ax.text(j,i,f'{L[i,j]:.3f}%',ha='center',va='center',color=INK,weight='bold')
ax.set_title('Cholesky factor in daily percentage-point units',fontsize=9,loc='left')
