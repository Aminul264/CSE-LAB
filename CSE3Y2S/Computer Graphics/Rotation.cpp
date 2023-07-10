#include<bits/stdc++.h>
#include<graphics.h>

int n,roate,xr,yr;
int angle;
using namespace std;

void draw(vector<int>x,vector<int>y)
{
    for(int i=0;i<n;i++)
    {
        line(x[i],y[i],x[(i+1)%n],y[(i+1)%n]);
    }
}
void  rotate(vector<int>&x,vector<int>&y)
{
   for(int i=0;i<n;i++)
   {
       int x1=xr+(x[i]-xr)*cos(angle*(acos(-1.0))/180) -(y[i]-yr)*sin(angle*(acos(-1.0))/180);
       int y1=yr+(x[i]-xr)*sin(angle*(acos(-1.0))/180) +(y[i]-yr)*cos(angle*(acos(-1.0))/180);
       x[i]=x1;
       y[i]=y1;
   }
}
int main()
{
    initwindow(1000,1000);
    cin>>n;
    vector<int>x(n),y(n);
    for(int i=0;i<n;i++)
    {
        cin>>x[i]>>y[i];
    }
    //rotation angle ange pivot point
    cin>>angle>>xr>>yr;
    //before rotation
     draw(x,y);
    //roatate
    rotate(x,y);
    //after rotation
    setcolor(13);
    draw(x,y);

     getch();

}
