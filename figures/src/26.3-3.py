B=np.array([[1,1.2,1],[1,-0.4,1],[1,0.6,0],[1,-1.4,0]],float)
f=np.array([0.008,-0.005,0.003]);w=np.array([3.,-2.,4.,-5.])
sf=np.array([0.010,0.0035,0.0055])
Of=np.outer(sf,sf)*np.array([[1,-.20,.50],[-.20,1,-.10],[.50,-.10,1]])
A=B[:,:2];H=np.linalg.inv(A.T@A)@A.T@B;g=H@f;Og=H@Of@H.T
fig=ax.figure;fig.delaxes(ax)
a1=fig.add_subplot(1,2,1)
x=np.arange(4)
a1.bar(x-0.19,(B@f)*100,width=.36,color=ACCENT,label='3 factors')
a1.bar(x+0.19,(A@g)*100,width=.36,color=WARM,label='2 factors (best fit)')
a1.axhline(0,color=INK,lw=.9)
a1.set_xticks(x);a1.set_xticklabels(['A','B','C','D'])
a1.set_ylabel('factor part of the return (%)')
a1.set_title('What the smaller model can still say',loc='left',fontsize=9)
a1.legend(fontsize=6.5,loc='upper right')
a2=fig.add_subplot(1,2,2)
b=B.T@w;bA=A.T@w
v=[np.sqrt(b@Of@b)*1e6,np.sqrt(bA@Og@bA)*1e6]
bars=a2.bar([0,1],v,color=[ACCENT,WARM],width=.5)
for bb,vv in zip(bars,v):
    a2.annotate(f'{vv:,.0f}',xy=(bb.get_x()+bb.get_width()/2,vv),xytext=(0,5),
                textcoords='offset points',fontsize=9,ha='center')
a2.annotate('+2.4%',xy=(1,v[1]),xytext=(0,26),textcoords='offset points',fontsize=9,ha='center',color=BAD)
a2.set_xticks([0,1]);a2.set_xticklabels(['3 factors','2 factors'])
a2.set_ylabel('factor risk of the portfolio (USD per day)')
a2.set_ylim(0,58000)
a2.set_title('And what it costs you',loc='left',fontsize=9)
