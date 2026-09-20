t=[0,1,2]
wealth=[1.0,1.5,0.75]
naive=[1.0,1.5,1.0]
ax.plot(t,wealth,color=ACCENT,lw=2.4,marker='o',ms=6,label='money you actually have')
ax.plot(t,naive,color=BAD,lw=2.0,ls='--',marker='s',ms=5,label='what "+50% then -50% = 0" implies')
ax.axhline(1.0,color=GRID,lw=1)
for x,y,s in [(1,1.5,'1.50 USD'),(2,.75,'0.75 USD'),(2,1.0,'1.00 USD')]:
    ax.annotate(s,xy=(x,y),xytext=(-52 if x==2 else 8,6),textcoords='offset points',fontsize=8,
                color=ACCENT if s!='1.00 USD' else BAD)
ax.annotate('gap = 25 points',xy=(2,.875),xytext=(1.10,.55),fontsize=8,color=INK,
            arrowprops=dict(arrowstyle='<->',color=INK,lw=.9))
ax.text(0.06,0.60,'ln 1.5 + ln 0.5 = -0.2877\nexp(-0.2877) - 1 = -25%',fontsize=7.5,color=GOOD)
ax.set_xticks(t);ax.set_xticklabels(['start','after +50%','after -50%'])
ax.set_ylabel('wealth from 1 USD');ax.set_ylim(.45,1.78)
ax.set_title('Simple returns do not add; log returns do',loc='left');ax.legend(fontsize=7,loc='upper right')
