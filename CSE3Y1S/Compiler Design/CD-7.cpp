#include<bits/stdc++.h>
using namespace std;

string keyword[]={"int","for","do","while"};
string arithmatic_operator[]={"+","-","*","/"};

//****check keyword
bool is_keyword(string str)
{   
    for(int i=0;i<4;i++)
    {
        if(str==keyword[i])
            return true;
    }
    return false;
}

//****check Arithmatic Operator
bool is_arithmatic_operator(string str)
{   
    for(int i=0;i<4;i++)
    {
        if(str==arithmatic_operator[i])
            return true;
    }
    return false;
}


//****check integer
bool is_integer(string str)
{
    for(int i=0;i<str.size();i++)
    {
        if(!isdigit(str[i])){
            return false;
        }
    }
    return true;
}


//****check float number
bool is_float(string str)
{   
    //bool get_dot=false;
    for(int i=0;i<str.size();i++)
    {
        if(str[i]=='.'){
          //  get_dot=true;
          return true;
        }
    }
    return false;
}

//*******check Identifier 
bool is_identifier( string str)
{
    if(str[0]=='_' || isalpha(str[0]))
    {
        for(int i=0;i<str.size();i++)
        {
            if(str[i]!='_' && !isalpha(str[i]) && !isdigit(str[i])){
                return false;
            }
        }
       return true;
    }
    return false;
   

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
    else if(is_arithmatic_operator(str))
    {
        cout<<"Arithmatic Operator"<<endl;
    }
    else if(is_integer(str))
    {
        cout<<"Integer"<<endl;
    }
    else if(is_float(str)){
        cout<<"Float"<<endl;
    }
    else if(is_identifier(str))
    {
        cout<<"Indetifier"<<endl;
    }
    else
    cout<<"Invalid"<<endl;
    
}