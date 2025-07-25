class Solution {
public:
    int lastStoneWeight(vector<int>& stones) 
    {
        priority_queue<int> pq;   
        int n=stones.size(); 
        for(int i=0;i<n;i++)
        {
            pq.push(stones[i]);
        }
        while(pq.size()>1)
        {
            int f=pq.top();
            pq.pop();
            int s=pq.top();
            pq.pop();
            n-=2;//reduce size of pq by 2
            if(f-s>0)
            {
                pq.push((f-s));
                n++;//they werent equal so one stone leaves a part of it behind
            }
        }
        if(pq.size()==1)
        {
            return pq.top();
        }
        return 0;
    }
};
