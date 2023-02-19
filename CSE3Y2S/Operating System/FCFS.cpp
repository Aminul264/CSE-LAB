#include<bits/stdc++.h>
using namespace std;

int n;
std::vector<pair<string,int> > v;

struct FCFS
{
	string process;
	int bstT;
};


void ganntChart(struct FCFS algo[])
{
	int prevT;
	v.push_back({"",0});
	for (int i = 0; i < n; ++i)
	{
		prevT=v[v.size()-1].second;
		v.push_back({algo[i].process,algo[i].bstT+prevT});
	}
}
void AWT()
{
	double avg=0;
	for (int i = 0; i <v.size()-1; ++i)
	{
		avg+=v[i].second;
	}
	cout<<"\nAverage waiting time : "<<avg/n<<"\n";
}
void ATT()
{
	double avg=0;
	for (int i = 0; i <v.size(); ++i)
	{
		avg+=v[i].second;
	}
	cout<<"Average turn around time : "<<avg/n<<"\n";
}

string Space(int n)
{
	string s="";
	while(n--) s+=" ";
	return s;
}
int main()
{
	freopen("../input.txt","r",stdin);
	freopen("../output.txt","w",stdout);


	cin>>n;
	struct FCFS algo[n];
	for (int i = 0; i < n; ++i)
	{
		cin>>algo[i].process;
		cin>>algo[i].bstT;
	}
	ganntChart(algo);
	for(int i=0;i<n;i++)
	{
		cout<<algo[i].process<<Space(algo[i].bstT);

	}
	cout<<"\n";
	for(int i=1;i<v.size();i++)
	{
		cout<<v[i-1].second<<Space(v[i].second-v[i-1].second);;
	}
	cout<<v[v.size()-1].second;
	//calculate average waiting time
	AWT();
	//calculate average turn around time
	ATT();


}