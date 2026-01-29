class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        import heapq
        check={}
        last={}
        for i in range(len(cost)):
            if original[i] in check:
                check[original[i]].append([changed[i],cost[i]])
            else:
                check[original[i]] = [[changed[i],cost[i]]]   
        # print(check)
        def path(start,end):
            val="abcdefghijklmnopqrstuvwxyz"
            dist={i:float('inf') for i in val}
            dist[start]=0
            curr=[(start,0)]
            while curr:
                node,dis=heapq.heappop(curr)
                # print(node,dis)
                if dis>dist[node]:
                    continue
                if node in check:    
                    for n,d in check[node]:
                        new_dist=d+dis
                        if new_dist<dist[n]:
                            dist[n]=new_dist
                            heapq.heappush(curr,(n,new_dist)) 
            last[start]=dist
            return dist[end]
        cost=0    
        for i in range(len(source)):
            c=0
            if source[i]!=target[i]:
                if source[i] in last:
                    c=last[source[i]][target[i]]
                else:
                    c=path(source[i],target[i])
                if c==float('inf'):
                    return -1
                cost+=c
        # print(last)
        return cost        
                