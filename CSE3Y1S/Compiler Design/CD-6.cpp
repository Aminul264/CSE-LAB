#include<bits/stdc++.h>
using namespace std;
bool is_binary_number(string str)
{
    if(str.size()<2 || str[0]!='0')
        return false;
    for(int i=1;i<str.size();i++)
    {
        if(str[i]!='0' && str[i]!='1')
            return false;
    }
    
    return true;
    
}
bool is_character_variable(string str)
{
    if(str.size()<4)
        return false;
    else if(str[0]!='c' ||  str[1]!='h' || str[2]!='_')
        return false;
    else
    {
        for(int i=3;i<str.size();i++)
        {
            if(!isalpha(str[i]) &&  !isdigit(str[i]))
                return false;
        }
    }
    return true;
}

bool is_binary_variable(string str)
{
   if(str.size()<4)
        return false;
    else if(str[0]!='b' ||  str[1]!='n' || str[2]!='_')
        return false;
    else
    {
        for(int i=3;i<str.size();i++)
        {
            if(!isalpha(str[i]) &&  !isdigit(str[i]))
                return false;
        }
    }
    return true;
}

int main()
{

    freopen("input6.txt","r",stdin);
    string str;
    cin>>str;

    if(is_character_variable(str))
        cout<<" Character Variable "<<'\n';
    else if(is_binary_variable(str))
        cout<<" Binary Variable "<<'\n';
    else if(is_binary_number(str))
        cout<<"Binary Number "<<'\n';
    else
        cout<<" Invalid Input "<<'\n';


}