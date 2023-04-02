#include<bits/stdc++.h>
using namespace std;

int n,frame_size=3;
void solve()
{
    cin>>n;
    vector<int>frame(n);
    int mp[n]={0};

    for(int i=0;i<n;i++)
    {
        cin>>frame[i];
    }
    queue<int>q;

    int cnt=0;
    for(int i=0;i<n;i++)
    {
        if(mp[frame[i]]==0)
        {
            cnt++;
            if(q.size()<frame_size)
            {
                q.push(frame[i]);
                mp[frame[i]]=1;
            }
            else
            {
                mp[q.front()]=0;
                q.pop();
                q.push(frame[i]);
                mp[frame[i]]=1;
            }
        }

    }

    cout<<"Page fault : "<<cnt<<endl;

}
int main()
{
   solve();
}
