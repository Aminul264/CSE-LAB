#include<bits/stdc++.h>
using namespace std;

string keyword[]={"int","do","while","for"};
string arithmatic_operator[]={"+","-","*","/"};

bool is_keyword(string str)
{
for(int i=0;i<4;i++)
    {
        if(str==keyword[i])
        {
            cout<<"Keyword"<<endl;
        }
}
int main()
{
    freopen("input.txt","r",stdin);
    string str;
        cin>>str;
    
    if(is_keyword(str))
    {
        cout<<"Keyword"<<endl;
    }
    for(int i=0;i<4;i++)
    {
        if(str==keyword[i])
        {
            cout<<"Keyword"<<endl;
        }
        else if(str==arithmatic_operator[i])
        {
            cout<<"Arithmatic Operator"<<endl;
        }
        else if(isdigit(str))
    }
}  