#include<bits/stdc++.h>
using namespace std;

vector<string>pn={"Sagor","Selim","Salma","Nipu"};
vector<string>p={"he","She","I","We","you","they"};
vector<string>n={"book","","cow","dog","home","grass","rice","mango"};
vector<string>v={"read","eat","take","run","write"};

vector<string>words;

//*sepates words
void Words(string str)
{
    string x="";
    for(int i=0;i<str.size();i++)
    {
        if(str[i]==' ')
        {
            words.push_back(x);
            x="";
        }
        else
        {
            x+=str[i];
        }
    }
    if(x.size())
    {
        words.push_back(x);
    }
}


//**checking noun
bool Check_pn(string str)
{
    int len =pn.size();
    for(int i=0;i<len;i++)
    {
        if(pn[i]==str)
        {
            return true;
        }
    }
    return false;
}

//**checkming pronoun
bool Check_p(string str)
{
    int len =p.size();
    for(int i=0;i<len;i++)
    {
        if(p[i]==str)
        {
            return true;
        }
    }
    return false;
}
//**checking verb
bool Check_v(string str)
{
    int len =v.size();
    for(int i=0;i<len;i++)
    {
        if(v[i]==str)
        {
            return true;
        }
    }
    return false;
}
//**checking noun object
bool Check_n(string str)
{
    int len =n.size();
    for(int i=0;i<len;i++)
    {
        if(n[i]==str)
        {
            return true;
        }
    }
    return false;
}


#define  ll   long long
void solve()
{
    string str;
    getline(cin,str);

    //seperates words
    Words(str);
    
    int len=words.size();
    bool flag = false;

   if(len==2)
    {
        if(Check_pn(words[0]) || Check_p(words[0]))
        {
            if(Check_v(words[1]))
            {
                flag= true;
            }

        }
    }
    else if(len==3)
    {
        if(Check_pn(words[0]) || Check_p(words[0]))
        {
            if(Check_v(words[1]) &&  Check_n(words[2]))
            {
                flag = true ;
            }
        }
    }

    if(flag) cout<<"Valid"<<endl;
        else cout<<"Invalid"<<endl;

}

int main(){ 

ios_base::sync_with_stdio(0);
cin.tie(0);
   //file I/O
    freopen("input.txt","r",stdin);
    int test=1;
    // cin>>test;
    while(test--){
       solve();
    }
    return 0;
 }
