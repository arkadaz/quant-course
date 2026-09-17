vals={(0,0):1.0,(1,0):.487654956,(1,1):.487654956,(2,0):.236621287,(2,1):.475620657,(2,2):.238999370};
for (n,j),v in vals.items():
 y=n-2*j;ax.plot(n,y,'o',color=GOOD,ms=8);ax.text(n,y+.2,f'{v:.6f}',ha='center',fontsize=8)
for n in range(2):
 for j in range(n+1):
  y=n-2*j
  for jj in (j,j+1): ax.plot([n,n+1],[y,(n+1)-2*jj],color=MUTED,lw=1)
ax.set_xticks([0,1,2],['0','0.5','1.0']);ax.set_yticks([]);ax.set_xlabel('Time (years)');ax.set_title('State prices include probability and discounting');ax.grid(False)
