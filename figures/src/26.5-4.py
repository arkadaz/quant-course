mom=np.array([1.10,0.34,-0.54,-1.26,-1.89,0.02,-0.81,-0.87,-0.22,-0.05,-2.28,0.93])
x2=np.array([-0.96,1.69,0.15,-1.13,-0.06,0.03,0.07,-0.44,0.75,0.82,-2.09,0.07])
y=np.array([0.3333,2.0410,-0.7030,-0.5626,-1.6580,-0.3936,-0.5334,-0.2921,1.6614,1.0138,-3.0054,1.0906])/100
X1=np.column_stack([np.ones(12),mom]);X=np.column_stack([X1,x2])
full=np.linalg.lstsq(X,y,rcond=None)[0]
g1=np.linalg.lstsq(X1,y,rcond=None)[0];e1=y-X1@g1
H=X1@np.linalg.inv(X1.T@X1)@X1.T;x2t=(np.eye(12)-H)@x2
g2=(x2t@e1)/(x2t@x2t);e2=e1-x2t*g2
g3=(x2t@y)/(x2t@x2t);r3=y-x2t*g3
bad=(x2@e1)/(x2@x2)
labs=['all at once','stages,\ndone right','stages, but on\nraw returns','stages, skipping\nthe middle step']
coef=[full[2],g2,g3,bad]
res=[np.linalg.norm(y-X@full),np.linalg.norm(e2),np.linalg.norm(r3),np.linalg.norm(e1-x2*bad)]
fig=ax.figure;fig.delaxes(ax)
a1=fig.add_subplot(1,2,1)
cols=[ACCENT,GOOD,WARM,BAD]
a1.bar(range(4),np.array(coef)*100,color=cols,width=.6)
a1.axhline(full[2]*100,color=INK,ls=':',lw=1.2)
for i,c in enumerate(coef):
    a1.annotate(f'{c*100:.4f}',xy=(i,c*100),xytext=(0,5),textcoords='offset points',
                fontsize=8,ha='center')
a1.set_xticks(range(4));a1.set_xticklabels(labs,fontsize=6.5)
a1.set_ylabel('coefficient on the new column (%)')
a1.set_ylim(0,0.95)
a1.set_title('Three of four get the number right',loc='left',fontsize=9)
a2=fig.add_subplot(1,2,2)
a2.bar(range(4),res,color=cols,width=.6)
for i,c in enumerate(res):
    a2.annotate(f'{c:.4f}',xy=(i,c),xytext=(0,5),textcoords='offset points',fontsize=8,ha='center')
a2.set_xticks(range(4));a2.set_xticklabels(labs,fontsize=6.5)
a2.set_ylabel('size of the leftover (idiosyncratic) part')
a2.set_ylim(0,0.055)
a2.set_title('Only two get the leftover right',loc='left',fontsize=9)
