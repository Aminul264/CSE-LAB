#Differential Manchester: Rule
#bit 1 : no transition :same as befor
#:::):positive to negative or negatibve to positie
#bit 0 :  transituion ;


data =[0 1 0 1 1 0 1];
#substitute one point to 300
point=300;
half=150;
signal =zeros(length(data)*point);

# 1 means +ve
#-1 means -ve
lastHalf=1;#let last half level was negative to positive
k=1;
for i=1:length(data)
  if data(i)==1#no transition
    if lastHalf==1#so level will be now  +ve to -ve
      for j=1:half
        signal(k)=5;
        k=k+1;
      endfor
      for j=1:half
        signal(k)=-5;
        k=k+1;
      endfor
     lastHalf=-1;
    else#so level will be now  -ve to +ve
      for j=1:half
        signal(k)=-5;
        k=k+1;
      endfor
      for j=1:half
        signal(k)=5;
        k=k+1;
      endfor
     lastHalf=1;
    endif
  else#transition
    if lastHalf==1#so level will be now -ve to +ve
      for j=1:half
        signal(k)=-5;
        k++;
      endfor
      for j=1:half
        signal(k)=5;
        k++;
      endfor
      lastHalf=1;
    else# now will be +ve to -ve
      for j=1:half
        signal(k)=5;
        k++;
      endfor
      for j=1:half
        signal(k)=-5;
        k++;
      endfor
     lastHalf=-1;
    endif
  endif
endfor

plot(signal);
ylabel('Differential Manchester');
ylim([-6 6]);


