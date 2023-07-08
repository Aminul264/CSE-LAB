
#include<graphics.h>
#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
    initgraph(&gd,&gm," ");

    setcolor(GREEN);
    rectangle(50,50,220,150);
    setfillstyle(SOLID_FILL,GREEN);
    floodfill(51,51,GREEN);

    setcolor(WHITE);
    rectangle(40,40,50,300);
    setfillstyle(SOLID_FILL,WHITE);
    floodfill(41,41,WHITE);

    setcolor(RED);
    circle(130,100,30);
    setfillstyle(SOLID_FILL,RED);
    floodfill(131,101,RED);

    setcolor(YELLOW); // Ground Stand
    rectangle(30,300,60,310);
    setfillstyle(SOLID_FILL,YELLOW);
    floodfill(31,301,YELLOW);

    setcolor(BLUE);
    rectangle(20,310,70,320);
    setfillstyle(SOLID_FILL,BLUE);
    floodfill(21,311,BLUE);

    setcolor(CYAN);
    rectangle(10,320,80,330);
    setfillstyle(SOLID_FILL,CYAN);
    floodfill(11,321,CYAN);


    getchar();
    return 0;
}
