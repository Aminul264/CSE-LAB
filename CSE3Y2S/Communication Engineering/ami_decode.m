#generating signal : 1 point into 200 point
point=500;
data =[0 1 0 1 1 0 1 1 1 0];
signal=zeros(length(data)*point);
k=1;
#check 0 means last non-zero level was -ve
#check 1 means last non-zero level was +ve
check=0;

for i=1:length(data)
  if data(i)==0
    for j=1:point
      signal(k)=0;
      k=k+1;
    endfor
  else
    if check==0
      for j=1:point
        signal(k)=5;
        k=k+1;
      endfor
      check=1;
    else
      for j=1:point
        signal(k)=-5;
        k++;
      endfor
      check=0;
    endif
  endif
endfor

subplot(2,1,1);
plot(signal);

#decoding
decode =zeros(length(data));
for i=1:length(data)
  if signal(i*point)==0#check the last position of a bitstream
    decode(i)=0;
  else
    decode(i)=1;
  endif
endfor

subplot(2,1,2);
stem(decode);



