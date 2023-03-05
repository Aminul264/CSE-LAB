data =[0 1 0 0  1 0];
point=200;
signal =zeros(length(data)*point);
k=1;

prev=-1;
for i=1:length(data)
  if data(i)==0
    for j=1:point
      signal(k)=0;
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

plot(signal,'LineWidth',2,'blue');
ylim([-2,2]);

#decoding
#if the last position of a level is equal to 0 then decode(i)=0
#  else decode(i)=1
decode=zeros(1,length(data));
for i=1:length(data)
  if signal(i*point)==0
    decode(i)=0;
  else
    decode(i)=1;
  endif
endfor
disp(decode);
