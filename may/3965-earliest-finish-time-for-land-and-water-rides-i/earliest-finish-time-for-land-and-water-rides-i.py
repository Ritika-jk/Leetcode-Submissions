class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        l=len(landStartTime);
        w=len(waterStartTime);
        res=float("inf");
        for i in range(l):
            for j in range(w):
                t=0;
                t+=landStartTime[i]+landDuration[i];
                if(waterStartTime[j]>t):
                    t=waterStartTime[j];
                t+=waterDuration[j];
                res=min(res,t);
                t=0;
                t+=waterStartTime[j]+waterDuration[j];
                if(landStartTime[i]>t):
                    t=landStartTime[i];
                t+=landDuration[i];
                res=min(res,t);
        return res
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        