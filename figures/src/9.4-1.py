ax.set_xlim(-0.2,4.2);ax.set_ylim(-0.2,3.2);ax.axis('off')
nodes=[(0,1.5,'1R 1G','1'),(1.7,2.5,'2R 1G','1/2'),(1.7,0.5,'1R 2G','1/2'),(3.6,3.0,'3R 1G','1/3'),(3.6,1.5,'2R 2G','1/3'),(3.6,0.0,'1R 3G','1/3')]
edges=[(0,1),(0,2),(1,3),(1,4),(2,4),(2,5)]
for a,b in edges:ax.plot([nodes[a][0],nodes[b][0]],[nodes[a][1],nodes[b][1]],color=MUTED,lw=1.2)
for x,y,label,p in nodes:ax.scatter([x],[y],s=620,color='white',edgecolor=ACCENT,zorder=3);ax.text(x,y+0.08,label,ha='center',fontsize=8,zorder=4);ax.text(x,y-0.14,p,ha='center',fontsize=7,color=WARM,zorder=4)
ax.text(0,3.05,'Start',ha='center');ax.text(1.7,3.05,'After 1 draw',ha='center');ax.text(3.6,3.18,'After 2 draws',ha='center')
