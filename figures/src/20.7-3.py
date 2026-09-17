haz=np.linspace(.002,.06,100);r=.045;d=.25;n=20;t=np.arange(1,n+1)*d;D=np.exp(-r*t)
for R in [.2,.4,.6]:
 out=[]
 for la in haz:
  Q=np.exp(-la*np.arange(n+1)*d);dq=Q[:-1]-Q[1:];den=np.sum(d*D*Q[1:])+.5*d*np.sum(D*dq);out.append((1-R)*np.sum(D*dq)/den*1e4)
 ax.plot(haz*100,out,label=f'Recovery {R*100:.0f}%')
ax.set_xlabel('Hazard rate (% per year)');ax.set_ylabel('Five-year par spread (basis points)');ax.set_title('Recovery and hazard jointly set CDS spread');ax.legend()
