data =[0 1 0 0  1 1];
point=200;
signal =zeros(length(data)*point);
k=1;
prevLast=1;
for i=1:length(data)
  if data(i)==0
    prevLast*=-1;
    for j=1:point/2
      signal(k)=prevLast;
      k++;
    endfor
    prevLast*=-1;
    for j=1:point/2
      signal(k)=prevLast;
      k++;
    endfor
  else
    for j=1:point/2
      signal(k)=prevLast;
      k++;
    endfor
    prevLast*=-1;
    for j=1:point/2
      signal(k)=prevLast;
      k++;
    endfor
  endif
endfor
size=0:1/point:length(data)-1/point;
plot(size,signal,'LineWidth',2);


#decodding
# if last point of level and first point of a level
# is equal then no transition :::decode(i)=1
#  else 0
k=1;
decode(k)=data(1);
k++;
decode =zeros(1,length(data));
for i=1:length(data)-1
  if signal(i*point)== signal(i*point+1)
    decode(k)=1;
    k++;
  else
    decode(k)=0;
    k++;
  endif
endfor

disp(decode);

