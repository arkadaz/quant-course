names=['file demo','path 1','path 2','path 3','path 4']
vol=np.array([24.90,25.42,30.36,51.57,40.14])
pnl=np.array([55.394,46.625,-20.263,-122.867,-104.401])
step=np.array([48.063,46.106,-18.843,-122.519,-104.578])
x=np.linspace(20,55,50)
ax.plot(x,991.52*(0.30-x/100),color=MUTED,lw=1.4,ls=(0,(4,2)),label='vega rule: 991.5k x (30% - vol)')
ax.scatter(vol,pnl,s=46,color=ACCENT,zorder=3,label='hedge P&L in the file')
ax.scatter(vol,step,s=46,marker='x',color=WARM,zorder=4,label='sum over the 50 steps')
offs=[(-12,2,'right'),(12,-20,'left'),(10,4,'left'),(0,14,'center'),(0,-26,'center')]
for n,v,p,(dx,dy,ha) in zip(names,vol,pnl,offs):
    ax.annotate(f'{n}\n{p*1000:+,.0f}',(v,p),xytext=(dx,dy),textcoords='offset points',ha=ha,fontsize=7.2)
ax.axvline(30,color=INK,lw=.8,ls=':');ax.axhline(0,color=INK,lw=.8)
ax.text(30.4,92,'sold at 30%',fontsize=7.3)
ax.set_xlim(18,56);ax.set_ylim(-230,110)
ax.set_xlabel('Realised volatility of the path (%)');ax.set_ylabel('Hedging P&L on 100,000 calls (USD thousand)')
ax.set_title('Calmer than 30% wins, wilder loses; gamma decides how much',loc='left')
ax.legend(fontsize=7,loc='lower left');ax.grid(alpha=.2)
