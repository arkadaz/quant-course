fig = ax.figure
ax.set_position([0.06, 0.08, 0.9, 0.84])
axes = [fig.add_axes([0.06+(j%3)*0.30, 0.54-(j//3)*0.42, 0.25, 0.30]) for j in range(6)]
x = np.linspace(-3,3,200)
axes[0].plot(x,stats.norm.pdf(x),color=ACCENT);axes[0].set_title("Normal",fontsize=8)
y=np.linspace(0.01,5,200);axes[1].plot(y,stats.lognorm.pdf(y,s=0.5),color=GOOD);axes[1].set_title("Lognormal",fontsize=8)
axes[2].plot(x,stats.t.pdf(x/np.sqrt(1/3),3)/np.sqrt(1/3),color=BAD);axes[2].set_title("Student-t",fontsize=8)
r=np.arange(0,12);axes[3].stem(r,stats.poisson.pmf(r,3),linefmt="C0-",markerfmt="C0o",basefmt=" " );axes[3].set_title("Poisson",fontsize=8)
r=np.arange(0,11);axes[4].stem(r,stats.binom.pmf(r,10,0.5),linefmt="C1-",markerfmt="C1o",basefmt=" " );axes[4].set_title("Binomial",fontsize=8)
y=np.linspace(0,5,200);axes[5].plot(y,stats.expon.pdf(y),color=WARM);axes[5].set_title("Exponential",fontsize=8)
for a in axes: a.tick_params(labelsize=6)
