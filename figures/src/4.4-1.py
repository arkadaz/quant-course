from math import comb
fig=plt.gcf();ax.remove();a1,a2=fig.subplots(1,2);fig.subplots_adjust(wspace=.3)
k2=np.arange(3);polya2=np.full(3,1/3);coin2=np.array([comb(2,j) for j in k2])/4
w=.38
a1.bar(k2-w/2,polya2,w,color=ACCENT,label='urn with reinforcement');a1.bar(k2+w/2,coin2,w,color=WARM,label='fair coin, no reinforcement')
for x,v in zip(k2-w/2,polya2):a1.text(x,v+.01,'1/3',ha='center',fontsize=7)
for x,v,s in zip(k2+w/2,coin2,['1/4','1/2','1/4']):a1.text(x,v+.01,s,ha='center',fontsize=7)
a1.set_xticks(k2);a1.set_xticklabels(['1R 3G','2R 2G','3R 1G']);a1.set_ylim(0,.75);a1.set_ylabel('probability')
a1.set_title('After 2 draws (start 1R 1G)',loc='left',fontsize=8);a1.legend(fontsize=6,loc='upper left')
k10=np.arange(11);polya10=np.full(11,1/11);coin10=np.array([comb(10,j) for j in k10])/1024
a2.bar(k10-w/2,polya10,w,color=ACCENT);a2.bar(k10+w/2,coin10,w,color=WARM)
a2.set_xticks(k10);a2.set_xlabel('red balls drawn in 10 draws');a2.set_ylim(0,.3)
a2.set_title('After 10 draws: urn 1/11 each, coin 24.6% at 5',loc='left',fontsize=8)
