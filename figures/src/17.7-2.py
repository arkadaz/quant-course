n=np.array([[244,1],[1,4]]);ax.imshow(n,cmap='Blues');ax.set_xticks([0,1],['Next: 0','Next: 1']);ax.set_yticks([0,1],['Previous: 0','Previous: 1']);ax.grid(False)
for i in range(2):
 for j in range(2):ax.text(j,i,str(n[i,j]),ha='center',va='center',color='white' if n[i,j]>100 else INK,fontsize=14)
