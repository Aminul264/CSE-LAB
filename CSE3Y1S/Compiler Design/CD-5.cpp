#include<bits/stdc++.h>
using namespace std;

bool is_float_variable(string str){
     
    if(str.size()<1)
        return false;
    for(int i=1;i<str.size();i++)
    {
      if(!isalpha(str[i]) && !isdigit(str[i]))
            return false;
    }
    if( (str[0]>='a'&& str[0]<='h') || (str[0]>='A'&& str[0]<='H') ||
        (str[0]>='o'&& str[0]<='z') || (str[0]>='O'&& str[0]<='Z') )
            return true;
    
    
    return false;
}
//***find out the point index
int get_point_index(string str)
{
    for(int i=0;i<str.size();i++)
    {
        if(str[i]=='.')
            return i;
    }
}

//***check float number

bool is_float_number(string str){

    int point = get_point_index(str);
        if(point==0)
            return false;
    int count=0;
    cout<<point<<endl;
    for(int i=point+1;i<str.size();i++)
    {
        if(isdigit(str[i]))
        {
            count++;
        }
        else
         return false;
    }

    if(count!=2)
        return false;

    for(int i=0;i<point;i++)
    {
        if(!isdigit(str[i])){
            return false;
        }
    }
    if(str[0]=='0' && str[1]!='.')
        return false;
    else 
        return true;
}


bool is_double_number(string str)
{
     int point = get_point_index(str);
        if(point==0)
            return false;
    int count=0;
    cout<<point<<endl;
    for(int i=point+1;i<str.size();i++)
    {
        if(isdigit(str[i]))
        {
            count++;
        }
        else
         return false;
    }

    if(count<3)
        return false;

    for(int i=0;i<point;i++)
    {
        if(!isdigit(str[i])){
            return false;
        }
    }
    if(str[0]=='0' && str[1]!='.')
        return false;
    else 
        return true;
}

int main(){
    freopen("input5.txt","r",stdin);
    //freopen("output4.txt","w",stdout);

    string  str;
    cin>>str;

    if(is_float_variable(str)){
        cout<<"Float Variable"<<endl;
    }
    else if(is_float_number(str)){
        cout<<"Float Number"<<endl;
    }
    else if(is_double_number(str)){
        cout<<"\n\n\nDouble Number"<<endl;
    }
    else {
        cout<<"\n\n\nInvalid Input"<<endl;
    }


}