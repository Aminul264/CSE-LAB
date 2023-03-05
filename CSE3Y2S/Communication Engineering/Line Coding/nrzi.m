data =[1 1 1 1 1 1 1];

point =200;

signal=zeros(length(data)*point);
k=1;
prev=1;
for i=1:length(data)
  if data(i)==0
    for j=1:point
      signal(k)=prev;
      k++;
    endfor
  else
    prev*=-1;
    for j=1:point
      signal(k)=prev;
      k++;
    endfor
  endif
endfor


size =1:1/point:length(data)-1/point;
plot(signal,'LineWidth',2,'blue');


#decoding
#if the last point of a level is equal
#to the first point of the next level
#then  decode(i)=0;
# else decode(i)=1

decode =zeros(1,length(data));
k=1;
check=signal(1);
decode(k)=data(1);
k++;
for i=1:length(data)-1
  if signal(i*point) !=signal(i*point+1)
    decode(k)=1;
    k++;
  else
    decode(k)=0;
    k++;
  endif
endfor
disp(decode);
