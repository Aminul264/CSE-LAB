data =[0 1 0 1 1 0 1 1];
point=200;
signal =zeros(length(data)*point);
k=1;
prevNonzero=-1;
prevLevel=0;
for i=1:length(data)
  if data(i)==0
    for j=1:point
      signal(k)=prevLevel;
      k++;
    endfor
  else
    if prevLevel!=0
      for j=1:point
        signal(k)=0;
        k++;
      endfor
      prevLevel=0;
    else
      prevNonzero*=-1;
      for j=1:point
        signal(k)=prevNonzero;
        k++;
      endfor
      prevLevel=prevNonzero;
    endif
  endif
endfor


plot(signal,'LineWidth',2,'b');

#decoding
#if the last point of a level is equal to the first point of the next level
#then  decode(k)=0;
#else decode(k)=1;
k=1;
decode =zeros(1,length(data));
decode(1)=data(1);
k++;
for i=1:length(data)-1
  if signal(i*point)==signal(i*point+1)
    decode(k)=0;
    k++;
  else
    decode(k)=1;
    k++;
  endif
endfor

disp(decode);




