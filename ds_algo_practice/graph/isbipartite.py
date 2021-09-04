
#https://leetcode.com/problems/is-graph-bipartite/

class Solution(object):
            
    def dfs(self,v,color,graph,visited):
      
        for i in graph[v]:
            if visited[i]==False:
                if color[v]=='red':
                    color[i] ='black'
                else:
                    color[i]='red'
                
                visited[i]=True
                self.dfs(i,color,graph,visited)
            if color[i]==color[v]:
                return False
        return True
        
    
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = ['white']*len(graph)
        visited = [False]*len(graph)
        flag=True
        for i in range(len(graph)):
            if len(graph[i])>0:
                flag = self.dfs(i,color,graph,visited)
                if flag==False:
                    break
        return flag
            
