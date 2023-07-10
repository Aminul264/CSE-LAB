
#include<graphics.h>
#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
    initwindow(1000,1000);

    setcolor(GREEN);
    rectangle(50,50,220,150);
    setfillstyle(SOLID_FILL,GREEN);
    floodfill(51,51,GREEN);

    setcolor(0);
    rectangle(40,40,50,300);
    setfillstyle(SOLID_FILL,0);
    floodfill(41,41,0);

    setcolor(RED);
    circle(130,100,30);
    setfillstyle(SOLID_FILL,RED);
    floodfill(131,101,RED);


    getchar();
    return 0;
}
