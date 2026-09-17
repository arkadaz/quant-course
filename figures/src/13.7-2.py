
n=252;h=1/n;j=np.arange(n);z1=np.sqrt(2)*np.sin(2*np.pi*(j+.25)/17);z2=np.sqrt(2)*np.cos(2*np.pi*(j+.4)/29)
S=np.empty(n+1);v=np.empty(n+1);S[0]=100;v[0]=.09
for m in range(n):
 vp=max(v[m],0);v[m+1]=v[m]+2*(.04-vp)*h+.3*np.sqrt(vp*h)*(-.7*z1[m]+np.sqrt(1-.7**2)*z2[m]);S[m+1]=S[m]*np.exp((.03-.01-.5*vp)*h+np.sqrt(vp*h)*z1[m])
t=np.arange(n+1)*h;ax.plot(t,S/S[0],color=ACCENT,label='Spot / S0');ax.plot(t,np.maximum(v,0)/v[0],color=WARM,label='Variance / v0');ax.set_xlabel('Time (years)');ax.set_ylabel('Normalized state');ax.legend()
