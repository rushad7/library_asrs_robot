n = 10                 # adjacency matrix dimentions
s = []
t = []
w = [1]
graph_mat = []

m4 = []
for i in range(2,n,1):
        m4.append(i)
m5 = []
for i in range(1,n-1,1):
        m5.append(i)
        
m4_upd = [x * n for x in m4]

m5_upd1 = [x * n for x in m5]
m5_upd2 = [x+1 for x in m5_upd1]

for i in range(1,n*n):
    
        if i == 1:                  # node 1
                for i in range(2):
                        s.append(1)
                
    
        elif 1<i<n:       # nodes 2 through 5
                for m in range(2):
                        s.append(i)
                        
        elif i == n:                # node 6
                s.append(i)
                 
        elif i in m4_upd:       # nodes 12,18,24,30
                s.append(i)
        
        elif i in m5_upd2:     # nodes 7,13,19,25 
                for m in range(2):
                        s.append(i)
                        
        elif (n*(n-1)) < i < (n*n):  # nodes 32,33,34,35
                s.append(i)
                
        elif i == (n*(n-1)) + 1 :      # node 31
                s.append(i)
                
        elif i == n*n:                 # node 36
                continue
                
        else :                           # central nodes
                for m in range(2):
                        s.append(i)

for i in range(1,n*n):
    
        if i == 1:                  # node 1
                t.append(1)
                t.append(i+n)
                
    
        elif 1<i<n:       # nodes 2 through 5
                t.append(i+1)
                t.append(i+n)
                        
        elif i == n:                # node 6
                t.append(2*i)
                 
        elif i in m4_upd:       # nodes 12,18,24,30
                t.append(i+n)
        
        elif i in m5_upd2:     # nodes 7,13,19,25 
                t.append(i+1)
                t.append(i+n)
                        
        elif (n*(n-1)) < i < (n*n):  # nodes 32,33,34,35
                t.append(i+1)
                
        elif i == (n*(n-1)) + 1 :      # node 31
                t.append(i+1)
                
        elif i == n*n:                 # node 36
                continue
                
        else :                           # central nodes
                t.append(i+1)
                t.append(i+n)


for i in range(len(s)):
        if t[i]-s[i] == 1:
                w.append(1)     #generate the nodes arbitrarily (1,0.5,1,0.5 and so on)

        elif t[i]-s[i] == n:
                w.append(0.5)
                

for i in range(len(s)):
    graph_mat.append((s[i],t[i],w[i]))

print(s)
print(t)
print(w)
print(graph_mat)
