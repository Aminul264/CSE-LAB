
//Arrival time =0
#include <bits/stdc++.h>
using namespace std;
int n,timeQuantum;
vector<pair<string,int> >v;//ganttChart

struct RoundRobin
{
	string process;
	int burstTime;
};

//construct ganntChart
void ganttChart(RoundRobin algo[])
{
	v.push_back({"",0});

	int complete=0,i=0,remTime,prevTime;
	while(complete!=n)
	{

			 remTime=algo[i].burstTime;
			 prevTime=v[v.size()-1].second;
             
			if(remTime<timeQuantum && remTime)
			{
				algo[i].burstTime=0;
				v.push_back({algo[i].process,prevTime+remTime});
			}

			else if(remTime)
			{
				algo[i].burstTime=remTime-timeQuantum;
				v.push_back({algo[i].process,timeQuantum+prevTime});
			}
			if(algo[i].burstTime==0 && remTime)
				complete++;
			i++;
			i%=n;
	}
}


//calculate average waiting time
int findPreviousSameProcess(int j)
{
	for(int i=j-1;i>=0;i--)
	{
		if(v[i].first==v[j].first)
			return (v[i].second);
	}
	return 0;
}
void AWT(RoundRobin algo[])
{
	double avg=0,avgtt;
	for(int i=0;i<n;i++)
	{
		for (int j = 1; j < v.size(); j++)
		{
			if(v[j].first==algo[i].process)
			{
				int w=findPreviousSameProcess(j);
				avg+=(v[j-1].second-w);// starting time - prevoius compelition time
				cout<<avg<<" ";
			}
		}
		//calculate turn aroundTime :: burst Time+ waiting time
		avgtt+=(avg+algo[i].burstTime);
	}
	cout<<"\nAverage waiting time : "<<avg/n<<"\n";
	cout<<"Average turn around time : "<<avgtt/n<<"\n";
}
int main()
{

	freopen("../input.txt", "r", stdin);
	freopen("../output.txt", "w", stdout);
    
    //number of process ,amount of quantum time
	cin>>n>>timeQuantum;
	RoundRobin algo[n];

	for (int i = 0; i < n; ++i)
	{
	
		//cin>>process>>burstTime;
		cin>>algo[i].process;//=process;
		cin>>algo[i].burstTime;//=burstTime;
	}
	ganttChart(algo);
    
    //v[i]=>:::i tomo process er compelition time
	for (int i = 0; i<v.size() ; i++)
	{
		cout<<v[i].first<<" "<<v[i].second<<"\n";
	}
    
	AWT(algo);
	//ATT();
	return 0;
}