Q=np.array([.236621287,.475620657,.238999370]);r=np.array([.07,.05,.03]);disc=np.exp(-r*.5);ks=np.linspace(.03,.07,81);N=10e6;d=.5;cap=[];floor=[]
for k in ks:
 cap.append(np.sum(Q*disc*N*d*np.maximum(r-k,0)));floor.append(np.sum(Q*disc*N*d*np.maximum(k-r,0)))
ax.plot(ks*100,np.array(cap)/1000,label='Caplet',color=ACCENT);ax.plot(ks*100,np.array(floor)/1000,label='Floorlet',color=GOOD);ax.set_xlabel('Strike rate (%)');ax.set_ylabel('Present value (USD thousands)');ax.set_title('Strike transfers value between cap and floor');ax.legend()
