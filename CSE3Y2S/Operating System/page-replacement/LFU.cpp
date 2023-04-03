#include<bits/stdc++.h>
using namespace std;

int n,frame_size=3;

int mp[100]={0};


void solve()
{
    
    cin>>n;
    cin>>frame_size;

    vector<int>frame(n);

    for(int i=0;i<n;i++)
    {
        cin>>frame[i];
    }
    vector<int>q;

    int cnt=0;
    for(int i=0;i<n;i++)
    {
        if(mp[frame[i]]==0)
        {
            cnt++;
            cout<<"mis "<<frame[i]<<" "<<endl;
            if(q.size()<frame_size)
            {
                q.push_back(frame[i]);
                mp[frame[i]]++;

            }
            else
            {
                //find the least frequencies page
               // pair<int,int>leastFR;
               // leastFR={q.front(),mp[q.front()]};

               int leastCnt=mp[q[0]];
               int index=0;

                for(int k=0;k<q.size();k++)
                {
                    if(leastCnt<mp[q[k]])
                    {
                        leastCnt=mp[q[k]];
                        index=k;
                    }
                }
                //remove from q
                mp[q[index]]--;
                //q[index]=frame[i];
                q.erase(q.begin()+index);
                q.push_back(frame[i]);
                mp[frame[i]]++;

            }
        }
    }

    cout<<"\nPage fault : "<<cnt<<endl;

}
int main()
{
    freopen("lfu.txt","r",stdin);
   solve();
}
