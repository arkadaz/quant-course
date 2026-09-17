t=np.linspace(-2.2,2.2,300);ax.plot(t,.12*t-.08*t**2,color=GOOD,lw=2,label='$\\gamma>0$');ax.plot(t,.12*t+.08*t**2,color=BAD,lw=2,label='$\\gamma<0$')
ax.set_xlabel('Scaled risky position');ax.set_ylabel('Mean-variance objective');ax.legend();ax.set_title('Risk aversion supplies the needed concavity',loc='left')
