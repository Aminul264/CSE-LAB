#include<bits/stdc++.h>
using namespace std;

int n,r;
struct container
{
    int  max[10];
    int  alloc[10];
    int  need[10];

    bool finish;
};

bool  SafetyAlgorithm(vector<container>p,vector<int>available)
{
    vector<int>works(r);
    works=available;
    vector<int>safeSequence;

    int completed=0;
    while(completed!=n)
    {
        bool visited=false;
        for(int i=0;i<n;i++)
        {
            if(p[i].finish==false)
            {
                int all_r=0;
                for(int j=0;j<r;j++)
                {
                    if(p[i].need[j]<=works[j])
                    {
                        all_r++;
                    }
                    else break;
                }
                if(all_r==r)
                {
                   completed++;
                   p[i].finish=true;
                   visited=true;

                   safeSequence.push_back(i);


                   //update works
                   for(int k=0;k<r;k++)
                   {
                     works[k]+=p[i].alloc[k];
                   }
                }
            }
        }
        if(visited==false)
        {
            cout<<"DeadLock"<<endl;
            return 0;
        }
    }
    
    for(int i=0;i<safeSequence.size();i++)
    {
        cout<<"p"<<safeSequence[i]<<" ";
    }
    cout<<endl;
    return  true;


}

int update(int index,vector<int>request,vector<container>&p,vector<int>&available)
{
    int all_r=0;
    for(int j=0;j<r;j++)
    {
        if( (request[j]<=p[index].need[j] ) && (request[j]<=available[j]))
        {
            all_r++;
        }
    }

    if(all_r==r)
    {
        for(int j=0;j<r;j++)
        {
            p[index].alloc[j]+=request[j];
            p[index].need[j]-=request[j];
            available[j]-=request[j];
        }
    }
    else
    {
        cout<<"Invalid request\n";
        return 0;
    }
}
int main()
{
freopen("input.txt","r",stdin);
  cin>>n>>r;

  vector<container>p(n);
  for(int i=0;i<n;i++)
  {
    //alloc
    for(int j=0;j<r;j++)
    {
        cin>>p[i].alloc[j];
    }
    //max
    for(int j=0;j<r;j++)
    {
        cin>>p[i].max[j];
    }
    p[i].finish=false;
  }

    //available
    vector<int>available(r);
    for(int i=0;i<r;i++)
    {
        cin>>available[i];
    }

    //calculation need

   for(int i=0;i<n;i++)
   {
        for(int j=0;j<r;j++)
        {
           p[i].need[j]=p[i].max[j]-p[i].alloc[j]; 
        }
   }

   //given request
   int index;
   cin>>index;
   vector<int>request(r);
   for(int i=0;i<r;i++)
   {
     cin>>request[i];
   }
  if(!update(index,request,p,available) ) 
      return 0;

   if(SafetyAlgorithm(p,available))
   {
     cout<<"Requst Granted\n";
   }
   else cout<<"Request Denied\n";

}