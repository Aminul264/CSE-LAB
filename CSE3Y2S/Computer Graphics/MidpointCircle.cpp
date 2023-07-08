
#include<bits/stdc++.h>
#include<graphics.h>
using namespace std;


void  midpoint(int cx,int cy,int r)
{
    int x0,y0,p;
        x0=0;
        y0=r;
        p=r;

       while(x0<=y0)
       {
            if(p<0)
            {
                x0=x0+1;
                y0=y0;
                p=p+2*x0+1;
            }
            else
            {
                x0=x0+1;
                y0=y0-1;
                p=p+2*x0+1-2*y0;
            }

            putpixel(cx+x0,cy+y0,10);
            putpixel(cx-x0,cy+y0,10);
            putpixel(cx+x0,cy-y0,10);
            putpixel(cx-x0,cy-y0,10);

            //symmetry x<->y
            putpixel(cx+y0,cy+x0,10);
            putpixel(cx-y0,cy+x0,10);
            putpixel(cx+y0,cy-x0,10);
            putpixel(cx-y0,cy-x0,10);

            delay(5);

       }

}

int main()
{


    initwindow(1000,1000);

    int cx,cy,r;

    cout<<"Enter center point : ";
    cin>>cx>>cy;
    cout<<"\nEnter radius : ";
    cin>>r;

    midpoint(cx,cy,r);



    getch();


}
