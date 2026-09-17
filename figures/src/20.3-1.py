nodes={(0,0):5,(1,0):6,(1,1):4,(2,0):7,(2,1):5,(2,2):3};
for (n,j),v in nodes.items():
 y=n-2*j;ax.plot(n,y,'o',color=ACCENT,ms=8);ax.text(n,y+.18,f'{v:.0f}%',ha='center',fontsize=9)
for n in range(2):
 for j in range(n+1):
  y=n-2*j
  for jj in (j,j+1): ax.plot([n,n+1],[y,(n+1)-2*jj],color=MUTED,lw=1)
ax.set_xticks([0,1,2],['0','0.5','1.0']);ax.set_yticks([]);ax.set_xlabel('Time (years)');ax.set_title('Recombining short-rate lattice');ax.grid(False)
