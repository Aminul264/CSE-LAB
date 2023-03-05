data =[0 1 0 0  1];
point=200;
signal =zeros(length(data)*point);
k=1;
for i=1:length(data)
  if data(i)==0
    for j=1:point/2
      signal(k)=-1;
      k++;
    endfor
    for j=1:point/2
      signal(k)=0;
      k++;
    endfor
  else
    for j=1:point/2
      signal(k)=1;
      k++;
    endfor
    for j=1:point/2
      signal(k)=0;
      k++;
    endfor
  endif
endfor

plot(signal,'LineWidth',2,'blue');

ylim([-2,2]);

#decoding
#i=1:length(data)
#if the first point of a level is equal to negative
#then decode(i)=0
#else 1

decode =zeros(1,length(data));

for i=1:length(data)
  if signal(i*point-point+1)==-1
    decode(i)=0;
  else
    decode(i)=1;
  endif
endfor

disp(decode);
