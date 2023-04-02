#include<bits/stdc++.h>
using namespace std;

int n,frame_size=3;

int mp[100]={0};

int Find_position(vector<int>&q, vector<int>&frame,int k)
{
    vector<int> v;
    for(int i=0;i<q.size();i++)
    {
        for(int j=k;j>=0;j--)
        {
            //first frame er je valuer  sathe match korbe
            if(q[i]==frame[j])
            {
                v.push_back(j);
                break;
            }
        }
    }
    sort(v.begin(),v.end());

    return v[0];


}
void solve()
{

    cin>>n;
    cin>>frame_size;

    vector<int>frame(n);
    //int mp[n+n]={0};

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
                mp[frame[i]]=1;

            }
            else
            {
                //find the least value's  position
                int f=Find_position(q,frame,i);
                mp[frame[f]]=0;
             
               //finding::q te kon  value ta  remove kora hobe 
                for(int k=0;k<frame_size;k++)
                {
                    if(frame[f]==q[k])
                    {
                        q[k]=frame[i];
                        mp[q[k]]=1;//new je value update kora holo seta mp te set kore rakha holo,,used
                        break;
                    }
                }

            }
        }
    }

    cout<<"\nPage fault : "<<cnt<<endl;

}
int main()
{
    freopen("lru.txt","r",stdin);
   solve();
}
