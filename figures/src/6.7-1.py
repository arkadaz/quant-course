S=np.array([[0.0004,0.00008,0.00012],[0.00008,0.0009,0.00018],[0.00012,0.00018,0.0006]])
S_bp2=S*1e8
ax.imshow(S_bp2,cmap='RdBu_r',vmin=0,vmax=100000)
labels=['Technology','Energy','Financials']
ax.set_xticks(range(3),labels);ax.set_yticks(range(3),labels)
for i in range(3):
    for j in range(3):
        colour='white' if S_bp2[i,j]<25000 or S_bp2[i,j]>75000 else INK
        ax.text(j,i,f'{S_bp2[i,j]:,.0f}',ha='center',va='center',color=colour)
ax.set_title('Daily-return covariance matrix (bp²)',fontsize=9,loc='left')
