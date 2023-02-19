#include<bits/stdc++.h>
using namespace std;


int n,timeQuantum;
vector<pair<string,int> > v;

struct RoundRobin
{
	string process;
	int bstT;
};

string Space(int n)
{
	string s="";
	while(n--)
	{
		s+=" ";
	}
	return s;
}
void ganntChart(struct RoundRobin algo[])
{
	v.push_back({"",0});
	int complete=0,i=0;
	int remT,prevT;
	while(complete!=n)
	{
		remT=algo[i].bstT;
		prevT=v[v.size()-1].second;

		if(algo[i].bstT<timeQuantum && remT)
		{
			algo[i].bstT=0;
			v.push_back({algo[i].process,remT+prevT});
		}
		else if(remT)//active:burstime not zero
		{
			algo[i].bstT-=timeQuantum;
			v.push_back({algo[i].process,prevT+timeQuantum});
		}

		if(algo[i].bstT==0 && remT)
		{
			complete++;
		}
		i++;
		i%=n;
	}

	//design ganntChart
	for(int i=1;i<v.size();i++)
	{
		cout<<v[i].first<<Space(v[i].second-v[i-1].second);
	}
	cout<<"\n";
	for(int i=1;i<v.size();i++)
	{
		cout<<v[i-1].second<<Space(v[i].second-v[i-1].second);
	}
	cout<<v[v.size()-1].second<<"\n";
}

int findPrevSameprocess(int j)
{
	for(int i=j;i>=0;i--)
	{
		if(v[i].first==v[j].first)
		{
			return v[i].second;
		}
	}
	return 0;
}

void AWT(RoundRobin algo[],RoundRobin algo1[])
{
	double avg=0,avgtt;
	for(int i=0;i<n;i++)
	{
		for (int j = 1; j < v.size(); j++)
		{
			if(v[j].first==algo[i].process)
			{
				int w=findPrevSameprocess(j);
				avg+=(v[j-1].second-w);// starting time - prevoius compelition time
				cout<<avg<<" ";
			}
		}
		//calculate turn aroundTime :: burst Time+ waiting time
		avgtt+=(avg+algo1[i].bstT);
	}
	cout<<"\nAverage waiting time : "<<avg/n<<"\n";
	cout<<"Average turn around time : "<<avgtt/n<<"\n";
}
int main()
{
	freopen("../input.txt","r",stdin);
	freopen("../output.txt","w",stdout);

	//number of process,timeQuantum;
	cin>>n>>timeQuantum;
	struct RoundRobin algo[n],algo1[n];
	//input::process,burst time
	for (int i = 0; i < n; ++i)
	{
		cin>>algo[i].process;
		cin>>algo[i].bstT;
		//copy
		cin>>algo1[i].process;
		cin>>algo1[i].bstT;
	}
	ganntChart(algo);
	//calculat average waiting time
	AWT(algo,algo1);


}