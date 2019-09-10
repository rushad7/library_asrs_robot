n = 10;                 % adjacency matrix dimentions

x = 1;                  % x --> source node
y = 98;              % y --> destination node    

s = [];
t = [];
w = [];

m4 = 2:1:(n-1);  
m5 = 1:1:(n-2);

for i = 1:n*n
    
    if i == 1                    % node 1
        s = [s,1,1];        
    
    elseif (1<i) & (i<n)        % nodes 2 through 5
        s = [s,i,i]; 
    
    elseif i == n                % node 6
        s = [s,i];
                
    elseif ismember(i,m4*n)       % nodes 12,18,24,30
        s = [s,i];
                    
    elseif ismember(i,((m5*n)+1))  % nodes 7,13,19,25 
        s = [s,i,i];
    
    elseif (n*(n-1)<i) & (i<n*n)  % nodes 32,33,34,35
        s = [s,i];
    
    elseif i == (n*(n-1)) + 1       % node 31
        s = [s,i];
    
    elseif i == n*n                 % node 36
        continue
    
    else                            % central nodes
        s = [s,i,i];
    end
    
end  

for i = 1:n*n
    
    if i == 1                    % node 1
        t = [t,2,i+n];        
    
    elseif (1<i) & (i<n)        % nodes 2 through 5
        t = [t,i+1,i+n]; 
    
    elseif i == n                % node 6
        t = [t,2*i];
                
    elseif ismember(i,m4*n)       % nodes 12,18,24,30
        t = [t,i+n];
                    
    elseif ismember(i,((m5*n)+1))  % nodes 7,13,19,25 
        t = [t,i+1,i+n];
    
    elseif (n*(n-1)<i) & (i<n*n)  % nodes 32,33,34,35
        t = [t,i+1];
    
    elseif i == ((n*(n-1)) + 1)       % node 31
        t = [t,i+1];
    
    elseif i == n*n                 % node 36
        continue
    
    else                            % central nodes
        t = [t,i+1,i+n];
    end
    
end    

for i = 1:length(t)
    
    if (t(i)-s(i)) == 1              
        w = [w,1];        
    
    elseif (t(i)-s(i)) == n  
        w = [w,0.5];
    end
    
end    

G = graph(s,t,w);
[shortest_path, num_of_edges] = shortestpath(G,x,y);
p = plot(G,'EdgeLabel',G.Edges.Weight,'LineWidth',2);
highlight(p,shortest_path,'EdgeColor','r','LineWidth',4)
hold on

% [shortest_path, num_of_edges] = shortestpath(G,1,45);
% p = plot(G,'EdgeLabel',G.Edges.Weight,'LineWidth',2);
% highlight(p,shortest_path,'EdgeColor','g','LineWidth',4)
% 
% [shortest_path, num_of_edges] = shortestpath(G,1,98);
% p = plot(G,'EdgeLabel',G.Edges.Weight,'LineWidth',2);
% highlight(p,shortest_path,'EdgeColor','black','LineWidth',4)


distance = 0;
for i = 1:length(shortest_path)-1
    if abs(shortest_path(i) - shortest_path(i+1)) == 1
        distance = distance + 1;
        
    elseif abs(shortest_path(i) - shortest_path(i+1)) == n
        distance = distance + 0.5;
    end
end

fprintf('Shortest distance between node %d and node %d is %.2f\n',x,y,distance)

