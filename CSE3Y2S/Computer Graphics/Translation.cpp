
//Translation  on two dimensional space
//n,(x,y)
//input 3 100 400 250 100  400 400 250 200

#include<bits/stdc++.h>
#include<graphics.h>
using namespace std;

int n,tx,ty,i;

void draw(vector<int>&x,vector<int>&y)
{
    for(int i=0;i<n;i++)
    {
        line(x[i],y[i],x[(i+1)%n],y[(i+1)%n]);
    }
}
void translate(vector<int>&x,vector<int>&y)
{
   for(int i=0;i<n;i++)
   {
       x[i]+=tx;
       y[i]+=ty;
   }
}
int main()
{
    initwindow(700,1000);
    floodfill(1,1,15);
    //n= number of points
    cin>>n;
    vector<int>x(n),y(n);
    for(i=0;i<n;i++){
        cin>>x[i]>>y[i];
    }
    //translation scale
    cin>>tx>>ty;
    //before translation
    outtextxy(x[0]+20,y[0]-20,"Before Translation");
    setcolor(0);
    draw(x,y);

    //translation
    translate(x,y);

    //after translation
    setcolor(15);
    outtextxy(x[0]+20,y[0]-20,"After Translation");
    setcolor(0);
    draw(x,y);

    getch();
    return 0;
}
