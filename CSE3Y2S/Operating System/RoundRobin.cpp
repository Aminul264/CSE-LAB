#include<bits/stdc++.h>
using namespace std;

int n,q=4;
vector<pair<string,int> >v;
struct rr
{
  string process;
  int bst;
};

//waiting time = last completion time - burst time
void waitingTime(vector<rr>p)
{
  
  double avgw=0,avgt=0;
  for(int i=0;i<n;i++)
  {
    for(int j=v.size()-1;j>=0;j--)
    {
      if(p[i].process==v[j].first)
      {
           avgw+=v[j].second-p[i].bst;
           avgt+=p[i].bst;
           break;
      }
    }
  }
  cout<<"Average waiting time :"<<avgw/n<<endl;
  cout<<"Average turn around time : "<<(avgt+avgw)/n<<endl;//waiting+burst
 }
string Space(int n)
{
  string s="";
  while(n--){
    s+=" ";
  }
  return s;
}
void algo(vector<rr>p)
 {
  int complete=0,i=0,rem,prev;
  v.push_back({" ",0});
  while(complete!=n)
  {
    rem=p[i].bst;
    prev=v[v.size()-1].second;
    if(rem<=q && rem)
    {
      v.push_back({p[i].process,rem+prev});
      p[i].bst=0;
      complete++;
    }
    else if(rem)
    {
      v.push_back({p[i].process,q+prev});
      p[i].bst=p[i].bst-q;
    }
    i++;
    i%=n;
  }

  //process sequence 
  for(int i=0;i<v.size();i++)
  {
    cout<<v[i].first<<" ";
  }
  cout<<endl;
  //waiting time s
  for(int i=0;i<v.size();i++)
  {
    cout<<v[i].second<<" ";
  }
  cout<<endl;
}
int main()
{
  freopen("input.txt","r",stdin);
  cin>>n;
  vector<rr>p(n),copy(n);
  for(int i=0;i<n;i++)
  {
    cin>>p[i].process;
    cin>>p[i].bst;

  }
  algo(p);
  waitingTime(p);
}