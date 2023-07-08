#include<bits/stdc++.h>
using namespace std;

struct priority
{
    string process;
    int bstT;
    int prio; 
};

int n;
vector<int>v;

bool compare (struct priority a,struct priority b)
{
   return a.prio<b.prio;
}


string Space(int n)
{
    string s="";
    while(n--)
    {
        s+=" ";
    }
    return s;

}
void Average()
{
    double avg=0;
    for(int i=0;i<v.size()-1;i++)
    {
        avg+=v[i];
    }
    cout<<"Average waiting time: "<<avg<<endl;
    avg=0;
    for(int i=0;i<v.size();i++)
    {
        avg+=v[i];
    }
    cout<<"Average turnaround time: "<<avg<<endl;
}
void gantChart(vector<priority>p)
{
    
    int prev=0;
    v.push_back(0);
    for(int i=0;i<n;i++)
    {   
        if(i==0) prev=0;
        else prev = v[v.size()-1];
        v.push_back(p[i].bstT+prev);
    }


    for(int i=0;i<n;i++)
    {
        cout<<""<<p[i].process<<Space((v[i+1]-v[i]));
    }
    cout<<endl<<endl;
   //print  waiting time
    for(int i=0;i<v.size()-1;i++)
    {
      cout<<v[i]<<Space(v[i+1]-v[i]);
    }
    cout<<v[v.size()-1]<<endl;

}
int main()
{

    freopen("input.txt","r",stdin);
    cin>>n;
    vector<priority> p(n);

    for(int i=0;i<n;i++)
    {
      cin>>p[i].process;
      cin>>p[i].bstT;
      cin>>p[i].prio;
    }

    sort(p.begin(),p.end(),compare);
    // for(int i=0;i<n;i++)
    // {
    //     cout<<p[i].process<<" "<<p[i].bstT<<" "<<p[i].prio<<endl;
    // }

    gantChart(p);
    

    //average waiting time::and  turn Around time
     Average();

}
