A=min(12.,10.);B=min(12.-A,15.);C=12.-A-B
assert (A,B,C)==(10.,2.,0.)
assert A+B+C==12.
assert 10-A==0 and 15-B==13
print('22.3 checked',A,B,C)
