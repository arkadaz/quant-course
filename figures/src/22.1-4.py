B0=100000.;r=0.08125/12;N=360
A=B0*r/(1-(1+r)**-N)
t=np.arange(1,N+1);bal=B0*((1+r)**N-(1+r)**t)/((1+r)**N-1)
prin=B0-bal;paid=A*t;intr=paid-prin
ax.plot(t/12,paid/1000,color='0.45',lw=1.4,ls='--',label='Total paid')
ax.plot(t/12,intr/1000,color=ACCENT,lw=1.8,label='Interest paid so far')
ax.plot(t/12,prin/1000,color=GOOD,lw=1.8,label='Principal repaid so far')
ax.scatter([2,2],[intr[23]/1000,prin[23]/1000],color=INK,s=18,zorder=3)
ax.annotate('Year 2: interest 16,121\nprincipal 1,698',(2,intr[23]/1000),xytext=(0.8,120),fontsize=7,arrowprops=dict(arrowstyle='-',color='0.4',lw=.8))
k=int(np.argmax(prin>=B0/2))
ax.scatter([t[k]/12],[prin[k]/1000],color=INK,s=18,zorder=3)
ax.annotate(f'Half the loan repaid\nonly in year {t[k]/12:.1f}',(t[k]/12,prin[k]/1000),xytext=(23.2,12),fontsize=7,arrowprops=dict(arrowstyle='-',color='0.4',lw=.8))
ax.set_xlabel('Years since origination');ax.set_ylabel('Cumulative USD thousands')
ax.set_title('Early payments are almost all interest ($100,000, 8.125%, 30 years)',loc='left');ax.legend(fontsize=7,loc='upper left');ax.grid(alpha=.2)
