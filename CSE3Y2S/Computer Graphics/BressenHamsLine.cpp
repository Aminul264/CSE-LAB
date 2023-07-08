#include<bits/stdc++.h>
#include<graphics.h>
using namespace std;




void bresenHam(int x1,int y1,int x2,int y2)
{
    int dx,dy,p;
    dx=x2-x1;
    dy= (y2-y1);
    p=2*dy-dx;

    while(x1<=x2)
    {
        if(p<0)
        {
          x1=x1+1;
          y1=y1;
          p=p+2*dy;
          putpixel(x1,y1,10);
        }
        else
        {
            x1=x1+1;
            y1=y1+1;
            p=p+2*dy-2*dx;
            putpixel(x1,y1,10);
        }
        delay(5);
    }

}

int main()
{

    int gd,gm;
    detectgraph(&gd,&gm);
    initgraph(&gd,&gm," ");

    int x1,y1,x2,y2;
    cout<<"Enter starting point : ";
    cin>>x1>>y1;
    cout<<"\nEnter Ending point : ";
    cin>>x2>>y2;

    //indicate first and last point
    setcolor(15);
    circle(x1,y1,2);
    circle(x2,y2,2);


    if(x1>x2)
    {
        swap(x1,x2);
        swap(y1,y2);
    }
    bresenHam(x1,y1,x2,y2);



    getch();


}
