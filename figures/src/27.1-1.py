ind=np.array([0,0,0,1,1,2,2,2])
B=np.zeros((8,5));B[:,0]=1;B[np.arange(8),1+ind]=1
B[:,4]=[1.2,-0.4,0.6,-1.4,0.9,-0.7,0.3,-0.5]
im=ax.imshow(B,cmap='RdBu_r',vmin=-1.6,vmax=1.6,aspect='auto')
for i in range(8):
    for j in range(5):
        ax.text(j,i,f'{B[i,j]:g}',ha='center',va='center',fontsize=7.5,
                color=INK if abs(B[i,j])<1.0 else 'white')
ax.set_xticks(range(5));ax.set_xticklabels(['market','tech','banks','energy','momentum'],fontsize=8)
ax.set_yticks(range(8));ax.set_yticklabels([f'stock {i+1}' for i in range(8)],fontsize=7.5)
ax.add_patch(plt.Rectangle((-0.5,-0.5),1,8,fill=False,edgecolor=BAD,lw=2.4))
ax.add_patch(plt.Rectangle((0.5,-0.5),3,8,fill=False,edgecolor=BAD,lw=2.4,ls='--'))
ax.annotate('add these three together',xy=(2,-0.85),fontsize=8,color=BAD,ha='center')
ax.annotate('and you get this one',xy=(0,8.05),fontsize=8,color=BAD,ha='center')
ax.set_title('Five columns, but only four of them are independent',loc='left')
