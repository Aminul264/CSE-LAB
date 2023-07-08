
#include <bits/stdc++.h>
#include <graphics.h>

using namespace std;

//draw all the points
void  drawFractal(vector<pair<int,int> > points)
{
   for(int i=0;i<points.size()-1;i++)
   {
       line(points[i].first,points[i].second,points[i+1].first,points[i+1].second);
       delay(1);
   }
}

void snowflake(vector<pair<int,int> >points, int iteration)
{
   for(int j=0;j<iteration;j++)
   {
       vector<pair<int,int> >tmp;
       for(int i=0;i<points.size()-1;i++)
       {
           tmp.push_back(points[i]);

           //find first tri point
           int tpx1=(points[i+1].first+2*points[i].first)/3;
           int tpy1=(points[i+1].second+2*points[i].second)/3;
           //find secons tri point
           int tpx2=(tpx1+points[i+1].first)/2;
           int tpy2=(tpy1+points[i+1].second)/2;
            tpx2=(2*points[i+1].first+points[i].first)/3;
            tpy2=(2*points[i+1].second+points[i].second)/3;

        //push first tri point
           tmp.push_back({tpx1,tpy1});

        //find another point above and between the two tri points
        //x= x1+(x2-x1)cosp+(y2-y1)sinp;
        //y=y1+(x2-x1)sinp+(y2-y1)cosp

        double angle =60*M_PI/180;
        int x=tpx1+(tpx2-tpx1)*cos(angle)+ (tpy2-tpy1)*sin(angle);
        int y=tpy1-(tpx2-tpx1)*sin(angle)+ (tpy2-tpy1)*cos(angle);

        tmp.push_back({x,y});
        tmp.push_back({tpx2,tpy2});
        tmp.push_back({points[i+1].first,points[i+1].second});

       }
       points.clear();
       points=tmp;
       tmp.clear();
   }
   drawFractal(points);
}
int main(){

    initwindow(1000,1000);

    vector<pair<int, int>> points = {{150,150}, {450,150}, {300,300}, {150,150}}; //{150,150}, {450,150}, {300,300}, {150,150} good sample
    snowflake(points,5 ); //input 0 to see the initiator

    getch();
    closegraph;
    return 0;
}
