
//Arrival time =0
#include <bits/stdc++.h>
using namespace std;
int n;
vector<pair<string,int> >chart;

struct SRTF
{
    string proc;
    int ArT,bstT;
};
void Sort(struct SRTF v[])
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = i ; j < n  ; ++j)
        {
            if (v[i].ArT > v[j].ArT)
                swap(v[i], v[j]);
        }
    }

}
//sort remaiining burst time
void SortBst(struct SRTF v[])
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
//SJF
void SJF(struct SRTF algo[])
{
    int prevT;
    SortBst(algo);
    for (int i = 0; i <n; i++)
    {
        if(algo[i].bstT>0)
        {
            prevT=chart[chart.size()-1].second;
            chart.push_back({algo[i].proc,algo[i].bstT+prevT});
        }
    }
    for (int i = 0; i < chart.size(); ++i)
    {
        cout<<chart[i].first<<" ";
    }
    cout<<endl;
    for (int i = 0; i < chart.size(); ++i)
    {
        cout<<chart[i].second<<" ";
    }

    return;
}

void GanntChart(struct SRTF algo[])
{
    int currentT=0,complete=0,i=0;
    int minb=INT_MAX;
    int index;
    int prevT=0;
    int incomplte=0;
    bool check=false;

    chart.push_back({"",0});

    while(complete!=n)
    {
        index=-1;
        //find shortest arrival  time and minimum burst time
        for(int i=0; i<n; i++)
        {
            if(algo[i].ArT<=currentT && algo[i].bstT<=minb && algo[i].bstT>0)
            {
                index=i;
                minb=algo[i].bstT;
            }
        }
        if(index!=-1)
        {
            if(index+1==n) check=true;//maximum arrival time touch

            if(currentT==0)
            {
                if(algo[0].bstT< algo[1].ArT)
                {
                    chart.push_back({algo[0].proc,algo[0].bstT});
                    algo[0].bstT=0;

                }
                else
                {
                    int bst=algo[1].ArT;
                    chart.push_back({algo[0].proc,bst});
                    algo[0].bstT-=bst;

                }
                currentT=algo[1].ArT;

                continue;
            }

            prevT=chart[chart.size()-1].second;
            chart.push_back({algo[index].proc,1+prevT});
            currentT++;
            algo[index].bstT--;
            if(algo[index].bstT==0)
            {
                complete++;

            }
            //  for (int i = 0; i < chart.size(); ++i)
            // {
            //      cout<<chart[i].first<<" "<<chart[i].second<<endl;
            //  }
        }
        // else if(check)//maximum arrival time touch korche
        // {
        //      cout<<"sjf\n";
        //      SJF(algo);
        //      return;
        // }
        else
        {
            SJF(algo);
            return;
            //currentT++;
        }

    }

}

int main()
{
    //file input,output
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);


    cin >> n; //number of process
    struct SRTF algo[n];

    // input :: process,arrivalTime,burstTime
    for (int i = 0; i < n; i++)
    {
        cin>>algo[i].proc;
        cin>>algo[i].ArT;
        cin>>algo[i].bstT;
    }
    Sort(algo);
    for (int i = 0; i < n; ++i)
    {
        cout<<algo[i].proc<<" "<<algo[i].ArT<<" "<<algo[i].bstT<<"\n";
    }
    GanntChart(algo);



    return 0;
}
