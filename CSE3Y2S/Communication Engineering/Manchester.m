#Manchester : Rule
#bit 1 : Negative to positive  :half half
#bit 0 : Positive to negative :half half

data =[0 1 0 1 1 0 1];
#substitute one point to 200
point=300;
half=150;
signal =zeros(length(data)*point);

k=1;
for i=1:length(data)
  if data(i)==1
    for j=1:half
      signal(k)=-5;
      k=k+1;
    endfor
    for j=1:half
      signal(k)=+5;
      k=k+1;
    endfor
  else
    for j=1:half
      signal(k)=5;
      k=k+1;
    endfor
    for j=1:half
      signal(k)=-5;
      k=k+1;
    endfor
  endif
endfor

plot(signal);
ylabel('Manchester');
ylim([-5 5]);


