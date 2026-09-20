vals=np.array([[0,0],[0,1.0]]);ax.imshow(vals,cmap='Blues',vmin=0,vmax=1);ax.set_xticks([0,1],['$dt$','$dW$']);ax.set_yticks([0,1],['$dt$','$dW$']);labels=[['0','0'],['0','$dt$']]
for i in range(2):
 for j in range(2):ax.text(j,i,labels[i][j],ha='center',va='center',fontsize=16,weight='bold',color=INK)
ax.set_title('Only one second-order cell survives',loc='left')
