q=np.linspace(0,.4,250);linear=.001*q;impact=.006*q**2;ax.plot(q*100,linear*1e4,color=ACCENT,lw=2,label='linear spread/fees');ax.plot(q*100,(linear+impact)*1e4,color=BAD,lw=2,label='plus quadratic impact')
ax.set_xlabel('Gross weight traded');ax.set_ylabel('Cost (bp of portfolio value)');ax.legend();ax.set_title('Impact bends the cost curve upward',loc='left')
