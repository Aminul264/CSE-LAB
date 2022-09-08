#include<bits/stdc++.h>
using namespace std;


//***count word 
void  count_word(string str)
{
    string vword,cword;
    for(int i=0;i<str.size();i++)
    {
        //str[i]=tolower(str[i]);

        if(str[i]=='a' || str[i]=='e'|| str[i]=='i' || str[i]=='o' || str[i]=='u')
        {
            for(;i<str.size();i++)
            {
                if(str[i]!=' ')
                {
                    vword+=str[i];
                }
                else
                {
                    vword+=' ';
                    break;
                }
            }
        }
        else if(isalpha(str[i]))
        {
            for(;i<str.size();i++)
            {
                if(str[i]!=' ')
                {
                    cword+=str[i];
                }
                else
                {
                    cword+=' ';
                    break;
                }
            }
        }
   
    
    }
    cout<<vword<<endl;
    cout<<cword<<endl;
}
int main()
{

    //freopen("input.txt","r",stdin);
    string str;
        cin>>str;
    count_word(str);

    
}