data =[0 1 0 0  1 1];
point=200;
signal =zeros(length(data)*point);
k=1;

for i=1:length(data)
  if data(i)==0
    for j=1:point/2
      signal(k)=1;
      k++;
    endfor
    for j=1:point/2
      signal(k)=-1;
      k++;
    endfor
  else
    for j=1:point/2
      signal(k)=-1;
      k++;
    endfor
    for j=1:point/2
      signal(k)=1;
      k++;
    endfor
  endif
endfor

plot(signal,'LineWidth',2,'blue');


#decoding
#last point of nth(i*point) is  negative then decode(i)=0
#else decode(i)=1

decode =zeros(1,length(data));
for i=1:length(data)
  if signal(i*point)==-1
    decode(i)=0;
  else
    decode(i)=1;
  endif
endfor

disp(decode);
