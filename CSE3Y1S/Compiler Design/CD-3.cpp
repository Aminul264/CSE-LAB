#include<bits/stdc++.h>
using namespace std;

string abbrebiation(string str){
 map<string,string>abbr;

 abbr["CSE-3141"]="Comuter Science & Engineering ,year, 1st semester,Compiler Design, Theory";
  abbr["CSE-3141"]="Comuter Science & Engineering ,year, 1st semester,Compiler Design, Theory";
   abbr["CSE-3141"]="Comuter Science & Engineering ,year, 1st semester,Compiler Design, Theory";
    abbr["CSE-3141"]="Comuter Science & Engineering ,year, 1st semester,Compiler Design, Theory";
     abbr["CSE-3141"]="Comuter Science & Engineering ,year, 1st semester,Compiler Design, Theory";
      abbr["CSE-3141"]="Comuter Science & Engineering ,year, 1st semester,Compiler Design, Theory";
       abbr["CSE-3142"]="Comuter Science & Engineering ,year, 1st semester,Compiler Design, Lab";

 return abbr[str];

}
int main(){
    freopen("input3.txt","r",stdin);
    //freopen("output4.txt","w",stdout);

    string  str;
    cin>>str;

    cout<<abbrebiation(str);


}