
#include<bits/stdc++.h>
#include<graphics.h>
using namespace std;

double fact(int n)
{
    if(n==0) return 1;
    return n*fact(n-1);
}

double ncr(int n,int i)
{
    return fact(n)/(fact(i)*fact(n-i));
}
double blendingFunc(int n,int i,double u)
{
    return ncr(n,i)*pow(u,i)*pow((1-u),(n-i));
}
void  beizerCurve(vector<pair<int,int> >xy)
{

    //printing the control point
    for(auto cp:xy)
    {
        setcolor(10);
        putpixel(cp.first,cp.second,10);
        circle(cp.first,cp.second,5);
    }

    //printing the curve
   int n=xy.size()-1;
   double u=0.005;
   for(double u=0;u<=1;u+=0.0005)
   {
        double x=0,y=0;
        for(int i=0;i<=n;i++)
        {
            double Bniu=blendingFunc(n,i,u);
            x+=xy[i].first*Bniu;
            y+=xy[i].second*Bniu;
        }
        putpixel(x,y,15);
        //delay(1);
   }
}

int main()
{


    initwindow(1000,1000);

    //control point
    vector<pair<int,int> >xy{{27,243},{101,47},{324,197},{437,23}};
    beizerCurve(xy);

    getch();


}
