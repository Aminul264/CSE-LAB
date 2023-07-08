#include<bits/stdc++.h>
using namespace  std;

int n,r;

struct container
{
    int max[100];
    int alloc[100];
    int need[100];
    
    bool flag;

};

void  SafetyAlgo(vector<int>available, vector<container>p)
{
    //copy available to works
    vector<int>works(r);
    for(int i=0;i<n;i++)
        works[i]=available[i];
    
     vector<int>safeSequence;
     int completed=0;
     while(completed!=n)
     {
        bool visited=false;
        for(int i=0;i<n;i++)
        {
            if(p[i].flag==false)
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
                p[i].flag=true;
                visited=true;

                safeSequence.push_back(i);
               // cout<<i<<" ";

                //update available(works)

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
            return;
         }
    }

  //  print safe sequence 
    for(int i=0;i<safeSequence.size();i++)
    {
        cout<<"p"<<safeSequence[i]<<" ";
    }
    cout<<endl;
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
       p[i].flag=false;
    }

    //available
    vector<int>available(r);
    for(int j=0;j<r;j++)
    {
        cin>>available[j];
    }

    //calculation need
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<r;j++)
        {
            p[i].need[j]=p[i].max[j]-p[i].alloc[j];
            cout<<p[i].need[j]<<" ";
        }
        cout<<endl;
    }

    SafetyAlgo(available,p);

}