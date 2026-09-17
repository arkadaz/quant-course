mus=np.linspace(.10,.14,161);Vinv=np.array([[27.472527,-16.483516],[-16.483516,109.890110]]);A=104.395604;g=2;ww=[]
for m in mus:
 mu=np.array([m,.06]);B=np.ones(2)@Vinv@mu;nu=(B-2*g)/A;ww.append((Vinv@(mu-nu*np.ones(2))/(2*g))[0])
ax.plot(mus*100,np.array(ww)*100,color=BAD,lw=2);ax.scatter([12,13],[50,56.59],color=GOOD,s=42);ax.set_xlabel('Assumed SPY expected return (%)');ax.set_ylabel('Optimal SPY weight (%)');ax.set_title('Small mean errors create large weight changes',loc='left')
