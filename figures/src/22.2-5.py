d=np.linspace(-0.03,0.04,300)
RI=0.28+0.14*np.arctan(-8.57+430*d)
ax.plot(100*d,100*RI,color=ACCENT,lw=2)
ax.axhline(100*(0.28+0.14*np.pi/2),color='0.6',ls=':',lw=1);ax.axhline(100*(0.28-0.14*np.pi/2),color='0.6',ls=':',lw=1)
for x in (0.0,0.02125):
    y=0.28+0.14*np.arctan(-8.57+430*x);ax.scatter([100*x],[100*y],color=INK,s=20,zorder=3)
    ax.annotate(f'{100*x:g}% gap: {100*y:.1f}%',(100*x,100*y),xytext=(100*x-2.6 if x>0 else 100*x+0.3,100*y+6),fontsize=7)
ax.set_xlabel('WAC minus 10-year rate (percentage points)');ax.set_ylabel('Refinancing multiplier (% CPR)')
ax.set_title('Richard and Roll: refinancing switches on once the gap passes about 2%',loc='left');ax.grid(alpha=.2);ax.set_ylim(0,55)
