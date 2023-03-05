data =[0 1 0 0 1 1 1 0];

point =200;
signal=zeros(1,length(data)*point);

k=1;
for i=1:length(data)
  if data(i)==0
    for j=1:point
      signal(k)=1;
      k++;
    endfor
  else
    for j=1:point
      signal(k)=-1;
      k++;
    endfor
  endif
endfor


#size =0:1/point:length(data)-1/point;
plot(signal,'LineWidth',2,'r');

#title('NRZ L');
#ylim([-3,3]);


#decoding
# positive voltage(1) => 0
# negative voltage(-1) => 1
#if the last point of a level is equal to positive
#then decode(i)=0
#else decode(i)=1
decode =zeros(1,length(data));
for i=1:length(data)
  if signal(i*point)==1
    decode(i)=0;
  else
    decode(i)=1;
  endif
endfor

disp(decode);


