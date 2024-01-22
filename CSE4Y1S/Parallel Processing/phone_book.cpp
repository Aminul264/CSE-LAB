#include<bits/stdc++.h>
#include<mpi.h>
using namespace std;


void send_a_number(int number,int to){
    MPI_Send(&number,1, MPI_INT,to , 0 , MPI_COMM_WORLD);
}
int receive_a_number(int from){
    int len;
    MPI_Recv(&len, 1 , MPI_INT, from ,0 , MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    return len;
}
void send_a_string(string str,int len,int to){
    MPI_Send(&str[0],len, MPI_INT,to , 0 , MPI_COMM_WORLD);
}
string receive_a_string(int from,int len){

    char *str= new char[len];
    MPI_Recv(str, len , MPI_CHAR ,from , 0 , MPI_COMM_WORLD , MPI_STATUS_IGNORE);
    return string(str);
}

string generate_a_string(vector<string>list,int start,int end)
{
    string s="";
    for(int i=start;i<end;i++)
    {
        s+=list[i]+"\n";
    }
    return s;

}
vector<string> get_list(string str)
{
    stringstream ss(str);
    vector<string>ans;
    string word="";
    while(ss>>word)
    {
        ans.push_back(word);
    }
    return ans;
}
void check(string text,string phone,string pattern)
{
    int cnt=0;
    for(int i=0;i<text.size();i++)
    {
        if(text[i]==pattern[cnt]){
            cnt++;
            if(cnt==pattern.size()){
                cout<<text<<" "<<pattern<<endl;
                break;
            }
        }
    }
}
int main(int argc,char *argv[]){

    MPI_Init(&argc , &argv);
    int rank,num_of_process;
    MPI_Comm_size( MPI_COMM_WORLD ,&num_of_process);
    MPI_Comm_rank( MPI_COMM_WORLD ,&rank);




    if(rank==0)
    {
        cout<<argc<<endl<<endl;
        ifstream phonebook;
        string name,phone;
        vector<string>namelist,phonelist;

        for(int i=1;i<argc;i++)
        {
            cout<<argv[i]<<endl;
            phonebook.open(argv[i]);
            string name,phone;
            while(phonebook >>name>>phone)
            {
                namelist.push_back(name);
                phonelist.push_back(phone);
                cout<<name<<" "<<phone<<endl;
            }
            phonebook.close();
        }
        cout<<"Enter a pattern : ";
        string pattern;
        cin>>pattern;

        clock_t start,end;
        start= clock();
        int n=namelist.size();
        for(int i=1;i<n;i++)
        {
            int start_pos=i*(n/num_of_process);
            int end_pos=(i+1)*(n/num_of_process);
            if(i==num_of_process-1) end_pos=n;

            string namelist_string=generate_a_string(namelist,start_pos,end_pos);
            int range=namelist_string.size()+1;
            send_a_number(range,0);
            send_a_string(namelist_string,range,0);


        //phone send
            string phonelist_string=generate_a_string(phonelist,start_pos,end_pos);
            range=phonelist_string.size()+1;
            send_a_number(range,0);
            send_a_string(phonelist_string,range,0);

        //pattern send
            int len=pattern.size()+1;
            send_a_number(len,0);
            send_a_string(pattern,len,0);

        }
        //work for rank 0
        for(int i=0;i<n/num_of_process;i++)
        {
            check(namelist[i],phonelist[i],pattern);
        }
        end= clock();
        double time_taken=double(end-start)/double(CLOCKS_PER_SEC);
        cout<<time_taken<<endl;

    }
    else
    {
        
        clock_t start,end;
        start= clock();

        int len_name=receive_a_number(0);
        vector<string>namelist=get_list(receive_a_string(0,len_name));


        int len_phone=receive_a_number(0);
        vector<string>phonelist=get_list(receive_a_string(0,len_phone));

        int len_pattern=receive_a_number(0);
        string pattern=receive_a_string(0,len_pattern);

        int n=namelist.size();
        for(int i=0;i<n;i++)
        {
            check(namelist[i],phonelist[i],pattern);
        }

        
        end= clock();
        double time_taken=double(end-start)/double(CLOCKS_PER_SEC);
        cout<<time_taken<<endl;

    }

    MPI_Finalize();
    return 0;
}