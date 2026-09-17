lam=np.linspace(0,.06,121);r=.045;c=.05;T=5;N=100;recs=[.2,.4,.6]
for R in recs:
 p=np.array([sum(N*c*np.exp(-(r+x)*i) for i in range(1,6))+N*np.exp(-(r+x)*T)+N*R*x/(r+x)*(1-np.exp(-(r+x)*T)) if x>0 else sum(N*c*np.exp(-r*i) for i in range(1,6))+N*np.exp(-r*T) for x in lam]);ax.plot(lam*100,p,label=f'Recovery {R*100:.0f}%')
ax.set_xlabel('Hazard rate (% per year)');ax.set_ylabel('Bond price per par 100');ax.set_title('Hazard and recovery jointly determine price');ax.legend()
