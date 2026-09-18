S=np.array([[.04,.0018],[.0018,.0036]]);ms=np.linspace(.06,.12,100);ws=[]
for m in ms:
 u=np.linalg.solve(S,np.array([m,.035])-.02);ws.append(u[0]/u.sum())
ax.plot(ms*100,np.array(ws)*100);ax.set_xlabel('Assumed equity mean return (%)');ax.set_ylabel('Tangency equity weight (%)')
