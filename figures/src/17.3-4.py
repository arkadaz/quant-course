S=np.array([[.04,.004],[.004,.01]]);ms=np.linspace(.06,.10,100);ws=[]
for m in ms:
 u=np.linalg.solve(S,np.array([m,.04])-.02);ws.append(u[0]/u.sum())
ax.plot(ms*100,np.array(ws)*100);ax.set_xlabel('Assumed equity mean return (%)');ax.set_ylabel('Tangency equity weight (%)')
