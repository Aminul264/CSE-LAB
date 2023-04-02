#include<bits/stdc++.h>
using namespace std;
int n,m;


void solve()
{
	 cin>>n>>m;
	 
    vector<int>process(n);
    vector<pair<int,int> > frame(n);
    int check[m]={0};
    

    for(int i=0;i<n;i++)
    {
        cin>>process[i];
    }
    for(int i=0;i<m;i++)
    {
        int x;
        cin>>x;
        frame[i]={x,i};

    }
    sort(frame.begin(),frame.end());
    for(int i=0;i<m;i++) cout<<frame[i].first<<" ";
    cout<<endl;

    bool flag=true;
    for(int i=0;i<n;i++)
    {
        flag=true;
        for(int j=m-1;j>=0;j--)
        {
            if(check[j]==0)
            {
                if(process[i]<=frame[j].first)
                {
                    check[j]=1;
                    flag=false;
                    cout<<i+1<<" ";
                    cout<<process[i]<<" ";
                    cout<<frame[j].second+1<<endl;
                    break;
                }
            }
        }

        if(flag)
        {
            cout<<i+1<<" ";
            cout<<process[i]<<" ";
            cout<<"Not allocated"<<endl;
        }
    }

}

int main( )
{

    cout<<"process no  ";
    cout<<"process size  ";
    cout<<"frame number  "<<endl;;
    solve();


}
