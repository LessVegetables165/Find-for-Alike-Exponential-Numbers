from math import log
ans = []
treshold = 10**(-5)
k=1
fin = 0
max = 600
for x in range(2,60):
    for y in range(x,60):
        for a in range(1, max):
            for b in range(1, max):
                try:
                    p = (-(x**a)+k*(y**b))/y**b
                    if abs(p) <= treshold and x**a != y**b:
                        print("{}^{} = {}*{}^{} için benzerlik = {} ".format(x,a,k,y,b,p))
                except:
                    pass
    fin += 100/58
    print("%{} is done.".format(fin))
