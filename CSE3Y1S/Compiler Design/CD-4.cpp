#include<bits/stdc++.h>
using namespace std;

bool checkVariable(string str)
{
     
    bool check1 = false ,check2 =  true ;
    if( (str[0]>='i'&& str[0]<='n') || (str[0]>='I'&& str[0]<='N') )
    {
       check1 = true;
    }
    for(int i=1;i<str.size();i++)
    {
      if(!isalpha(str[i]) && !isdigit(str[i]))
      {
        check2 = false;
      }
    }
    
    if(check1 && check2)
    {
        return true;
    }
    return false;
}


bool checkShortInt(string str)
{

     for(int i=0;i<str.size();i++)
     {
        if(!isdigit(str[i]))
        {
            return false;
        }
    }
 
    if(str[0]!='0'&& str.size()<=4)
    {
        return true;
    }
    return false;
}

bool checkLongInt(string str)
{
   
    for(int i=0;i<str.size();i++)
    {
        if(!isdigit(str[i]))
        {
            return false;
        }
    }
    if(str[0]!='0' && str.size()>=5)
    {
        return true;
    }
    return false;
}

int main(){
    freopen("input4.txt","r",stdin);
    //freopen("output4.txt","w",stdout);

    string  str;
    cin>>str;

    if(checkVariable(str)){
        cout<<"\n\n\nInteger Variable"<<endl;
    }
    else if(checkShortInt(str))
    {
        cout<<"\n\n\nShortInt Number"<<endl;
    }
    else if(checkLongInt(str))
    {
        cout<<"\n\n\nLongtInt Number"<<endl;
    }
    else
    {
        cout<<"\n\n\nInvalid Input"<<endl;
    }


}