T = np.linspace(0, 1.0, 80)
S0 = 5000
r = 0.05
fair = S0*np.exp(r*T)
market = fair + 40
term_structure(ax, T, {'Fair carry': fair, 'Quoted futures (illustrative)': market}, title='Fair forward rises with financing horizon', ylabel='Futures level (points)')
