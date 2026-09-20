gam=np.linspace(1,4,120);A=104.395604;B=6.923077;Vinv=np.array([[27.472527,-16.483516],[-16.483516,109.890110]]);mu=np.array([.12,.06]);ws=[]
for g in gam:
 nu=(B-2*g)/A;ws.append((Vinv@(mu-nu*np.ones(2))/(2*g))[0])
ax.plot(gam,np.array(ws)*100,color=ACCENT,lw=2);ax.scatter([1,2,4],[ws[0]*100,50,ws[-1]*100],color=GOOD,s=35);ax.set_xlabel('Risk aversion');ax.set_ylabel('SPY weight (%)');ax.set_title('More risk aversion shifts capital toward AGG',loc='left')
