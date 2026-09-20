lam,s_prev,shock=0.94,0.01,-0.04
w,a1,b1=1.8e-6,.09,.89
ve=(1-lam)*shock**2+lam*s_prev**2
vg=w+a1*shock**2+b1*s_prev**2
V=w/(1-a1-b1)
h=np.arange(0,91)
ewma=np.full_like(h,np.sqrt(ve)*100,dtype=float)
garch=np.sqrt(V+(a1+b1)**h*(vg-V))*100
ax.plot(h,ewma,color=ACCENT,lw=2.4,label='EWMA, lambda = 0.94')
ax.plot(h,garch,color=WARM,lw=2.4,label='GARCH(1,1)')
ax.axhline(np.sqrt(V)*100,color=BAD,ls='--',lw=1.6,label='GARCH long-run level, 0.949%')
ax.axhline(s_prev*100,color=GRID,lw=1.2)
ax.annotate('yesterday, both said 1.000%',xy=(60,1.0),xytext=(0,-14),textcoords='offset points',fontsize=7,color=MUTED)
ax.annotate('1.378%',xy=(0,np.sqrt(ve)*100),xytext=(4,8),textcoords='offset points',fontsize=8,color=ACCENT)
ax.annotate('1.523%',xy=(0,np.sqrt(vg)*100),xytext=(4,4),textcoords='offset points',fontsize=8,color=WARM)
ax.annotate('1.154% at day 60',xy=(60,garch[60]),xytext=(-6,-20),textcoords='offset points',fontsize=8,color=WARM,
            arrowprops=dict(arrowstyle='->',color=WARM,lw=.8))
ax.annotate('EWMA never comes home',xy=(45,np.sqrt(ve)*100),xytext=(30,1.70),fontsize=8,color=ACCENT,
            arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.8))
ax.set_xlabel('trading days after the -4% day');ax.set_ylabel('forecast volatility (% per day)')
ax.set_ylim(0.85,1.80)
ax.set_title('One offset in the formula, two completely different futures',loc='left')
ax.legend(fontsize=7,loc='upper right')
