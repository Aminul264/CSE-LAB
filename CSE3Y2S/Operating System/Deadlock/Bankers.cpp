#include <bits/stdc++.h>
using namespace std;

int n,r;
struct process
{
    int max[10];
    int alloc[10];
    int need[10];

    int flag;

};
void solve()
{
    cout<<"Number of process : ";
    cin>>n;
    cout<<"\nNumber of resources : ";
    cin>>r;
    
    struct  process p[n];

    //input
    for (int i = 0; i < n; i++)
    {
        cout<<"Enter the details of p"<<i<<endl;

        cout<<"Enter Max need";
        for(int j=0;j<r;j++)
        {
            cin>>p[i].max[j];
        }

        cout<<"Enter allocation : ";
        for(int j=0;j<r;j++)
        {
            cin>>p[i].alloc[j];
        }

        p[i].flag=0;

    }
    cout<<endl;


    //calculation current need
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<r;j++)
        {
            p[i].need[j]=p[i].max[j]-p[i].alloc[j];
        }
    }
    
   //input for available
   cout<<"give available resources : ";
    int avail[r];
    for(int i=0;i<r;i++ )
    {
        cin>>avail[i];
    }


    int completed=0;
    int all_r=0;
    bool visited_once=false;

    vector<int>sequence;
    while(n!=completed)
    {
        visited_once=false;

        for(int i=0;i<n;i++)
        {   
           if(p[i].flag==0)
           {
                all_r=0;
                for(int j=0;j<r;j++)
                {
                    if(p[i].need[j]<=avail[j])
                    {
                        all_r++;
                    }
                    else break;
                }
                if(all_r==r)
                {
                    completed++;
                    visited_once=true;
                    p[i].flag=1;
                    
                    
                    sequence.push_back(i);


                    //avail+=allocation
                    for(int k=0;k<r;k++)
                    {
                        avail[k]+=p[i].alloc[k];
                    }
                }
           } 
        }
        if(visited_once==false)
        {
            cout<<"\nDeadlock ocurred"<<endl;
            return ;
        }
    }



    //print safe sequence 
    cout<<endl;
    for(int i=0;i<sequence.size();i++)
    {
        cout<<"p"<<sequence[i]<<" ";
    }
    cout<<endl;


}

int main()
{
   //freopen("bankers.txt","r",stdin);

  solve();


}
