//Arrival time =0
#include <bits/stdc++.h>
using namespace std;
int n;

struct SJFtest
{
	string process;
	int bstT;
};
vector<pair<string,int> >v;

void Sort(struct SJFtest v[])
{
	for (int i = 0; i < n; ++i)
	{
		for (int j = i ; j < n  ; ++j)
		{
			if (v[i].bstT > v[j].bstT)
				swap(v[i], v[j]);
		}
	}

}
string Space(int n)
{
	string s="";
	while(n--) s+=" ";
	return s;
}

void GanntChart(struct SJFtest algo[])
{
	v.push_back({"",0});
	int prevT;
	for (int i = 0; i <n; i++)
	{
		prevT=v[v.size()-1].second;
		v.push_back({algo[i].process,prevT+algo[i].bstT});
	} 
	//design ganntChart
	for (int i = 1; i < v.size(); ++i)
	{
		cout<<v[i].first<<Space(v[i].second-v[i-1].second);
	}
	cout<<"\n";
	for (int i = 1; i < v.size(); ++i)
	{
		cout<<v[i-1].second<<Space(v[i].second-v[i-1].second);
	}
	cout<<v[v.size()-1].second<<"\n";
}
//find average waiting time
void AWT()
{
	double avg=0;
	for(int i=0;i<v.size()-1;i++)
	{
		avg+=v[i].second;
	}
	cout<<"\nAverage waiting time : "<<avg/n<<"\n";
}
//find average turn arround time
void ATT()
{
	double avg=0;
	for(int i=0;i<n;i++)
	{
		avg+=v[i].second;
	}
	cout<<"\nAverage turn arround time : "<<avg/n<<"\n";
}
int main()
{
	freopen("../input.txt", "r", stdin);
	freopen("../output.txt", "w", stdout);

	cin >> n; //number of process
	//input :: process_name,burstTime
	struct SJFtest algo[n];
	for (int i = 0; i < n; i++)
	{
		cin>>algo[i].process;
		cin>>algo[i].bstT;
	}
	Sort(algo);
	//construct ganntChart
	GanntChart(algo);
	AWT();
	ATT();
	return 0;
}