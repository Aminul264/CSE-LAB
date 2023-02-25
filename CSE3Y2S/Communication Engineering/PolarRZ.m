#PolarRZ : Rule
#bit 0 : Negative to zero
#bit 1 : Positive to zero

data =[0 1 1 0 0 1 0];
#substitute one point to 200
point=300;
half=150;
signal =zeros(length(data)*point);

k=1;
for i=1:length(data)
  if data(i)==1
    for j=1:half
      signal(k)=5;
      k=k+1;
    endfor
    for j=1:half
      signal(k)=0;
      k=k+1;
    endfor
  else
    for j=1:half
      signal(k)=-5;
      k=k+1;
    endfor
    for j=1:half
      signal(k)=0;
      k=k+1;
    endfor
  endif
endfor

plot(signal);

ylim([-5 5]);


