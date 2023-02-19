//arrival time zero
#include<bits/stdc++.h>
using namespace std;

int n;
vector<pair<string,int> > v;

struct Priority
{
	string process;
	int bstT;
	int priority;
};

void Sort(struct Priority algo[])
{
	for(int i=0;i<n;i++)
	{
		for(int j=i;j<n;j++)
		{
			if(algo[i].priority>algo[j].priority)
			{
				swap(algo[i],algo[j]);
			}
		}
	}
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
void ganntChart(struct Priority algo[])
{
	int prevT;
	v.push_back({"",0});
	for (int i = 0; i < n; ++i)
	{
		prevT=v[v.size()-1].second;
		v.push_back({algo[i].process,algo[i].bstT+prevT});

	}
	//design ganntChart
	for (int i = 1; i < v.size(); ++i)
	{
		cout<<v[i].first<<Space(v[i].second-v[i-1].second);
	}
	cout<<"\n\n";
	for(int i=1;i<v.size();i++)
	{
		cout<<v[i-1].second;
		string s =Space(v[i].second-v[i-1].second);
		s+=" ";
		cout<<s;
	}
}

void AWT()
{
	double avg=0;
	for(int i=0;i<v.size()-1;i++)
	{
		avg+=v[i].second;
	}
	cout<<"\nAverage waiting time  : "<<avg/n<<"\n";
}
void ATT()
{
	double avg=0;
	for(int i=0;i<v.size();i++)
	{
		avg+=v[i].second;
	}
	cout<<"\nAverage turn around time  : "<<avg/n<<"\n";
}
int main()
{
	//file input
	freopen("../input.txt", "r", stdin);
	freopen("../output.txt", "w", stdout);

	//number of process
	cin>>n;
	struct Priority algo[n];
	//input:: process,burstTime,priority order
	for (int i = 0; i < n; ++i)
	{
		cin>>algo[i].process;
		cin>>algo[i].bstT;
		cin>>algo[i].priority;
	}

	Sort(algo);
	ganntChart(algo);
	//calculate average waiting time
	AWT();
	//calculate average turn around time
	ATT();


}