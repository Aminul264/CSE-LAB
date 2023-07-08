#include<bits/stdc++.h>
#include<graphics.h>

using namespace std;


void drawCircle()
{
    setcolor(5);
    circle(100,100,50);
    setfillstyle(SOLID_FILL,5);
    floodfill(101,101,5);
}

void  drawRectangle()
{
    setcolor(10);
    rectangle(100,100,200,200);
    setfillstyle(SOLID_FILL,10);
    floodfill(101,101,10);
}

void  drawTriangle()
{
    setcolor(1);
    line(150,150,250,250);
    line(150,150,150,250);
    line(150,250,250,250);
    setfillstyle(SOLID_FILL,1);
    floodfill(151,200,1);

}
int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
    initgraph(&gd,&gm,"");

    string sequence;
    while(1)
    {
        cout<<"Enter a Sequence (0 for quit):";
        cin>>sequence;

        for(char ch:sequence)
        {
            if(ch=='r')
            {
                drawRectangle();
            }
            else if(ch=='c')
            {
                   drawCircle();
            }
            else  drawTriangle();
        }
    }


    getchar();
}
