#include<bits/stdc++.h>
#include<graphics.h>

using namespace std;

int n;
void draw(vector<int>x,vector<int>y)
{
    for(int i=0;i<n;i++)
    {
        line(x[i],y[i],x[(i+1)%n],y[(i+1)%n]);
        delay(10);
    }
}
void scale(vector<int>&x,vector<int>&y,int sx,int sy)
{
   for(int i=0;i<n;i++)
   {
       x[i]*=sx;
       y[i]*=sy;
   }
}
int main()
{
    initwindow(1000,1000);
    int sx,sy;
    cin>>n;
    vector<int>x(n),y(n);
    for(int i=0;i<n;i++)
    {
        cin>>x[i]>>y[i];
    }
    cin>>sx>>sy;
    //before scalling
    draw(x,y);
    //scalling
    scale(x,y,sx,sy);
    //after scalling
    setcolor(9);
    draw(x,y);

    getch();

}
