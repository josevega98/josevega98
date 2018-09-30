f = open("data.txt")
data = f.read().strip()
f.close()
m = [[int(njjm) for njjm in line.strip().split()] for line in data.split('\n')]
print (m)
print (len(m))
print (len(m[0]))
print ("\n")
print("dato inicial de cada columna")
for x in range(0,len(m[0])):
    print ("     ",m[0][x])
theta =  [i for i in range(len(m[0])+1)]
for i in range(0,len(m[0])+1):
    theta[i]=0
alpha = 0.005
def grad(the,x,alpha):
    r2=[i for i in range(len(the))]
    for i in range(0,len(the)):
        r2[i]=the[i]
        
    for j in range(0,len(the)):
        var=[o for o in range(len(x[0])-1)]
        if j==0:
            the[j]=r2[j]-alpha*fcosto(x,r2)/len(x)
        else:
            print("Valores ")
            sjjmatemp=0.00
            for ii in range(len(x)):
                for jj in range(0,len(x[0])-1):
                    var[jj]=x[ii][jj]
                    print(var[jj])
                sjjmatemp=sjjmatemp + pow(h_proporcional(var,the)-x[ii][len(x[0])-1],1)*x[ii][j-1]
            the[j]=r2[j]-alpha*(sjjmatemp/len(x))
    print(the)
for i in range(1):
    grad(theta,m,alpha)
    
def h_proporcional(x,thet):
    r=0
    for i in range(0,len(m[0])):
        if i== 0:
            r = r + theta[i]
        else:
            r = r + x[i-1]*theta[i] + pow(x[i-1],2)*theta[i+1]
    return r
def fcosto(x,t):
    r=0.00
    for i in range(0,len(x)):
        var=[i for i in range(len(x[0])-1)]
        for j in range(0,len(x[0])-1):
            var[j]=x[i][j]
        r = r + pow(h_proporcional(var,t)-x[i][len(x[0])-1],2)
    r = r/(len(m)*2)
    return r