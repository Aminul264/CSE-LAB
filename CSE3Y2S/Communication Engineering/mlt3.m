#MLT-3 :Rule

#bit 0: no transition
#bit 1:  0 if last level not zero
#        1 else opposite of last non zero level

data =[0 1 1 1 1 1 1 1];
#substitute one point to 200
point=200;
signal =zeros(length(data)*point);
#status 1=+ve  -1=-ve
status=-1;#let last non zero level was negative
level=0;#let last level was 0
k=1;
for i=1:length(data)
  if data(i)==0
    if level==0
      for j=1:point
        signal(k)=0;
        k=k+1;
      endfor
    elseif status==1
      for j=1:point
        signal(k)=5;
        k=k+1;
      endfor
      level=1;
    else
      for j=1:point
        signal(k)=-5;
        k=k+1;
      endfor
      level=-1;
    endif
  else
    if level==0
      if status==1
        for j=1:point
          signal(k)=-5;
          k=k+1;
        status=-1;
        level=-1;
        endfor
      else
         for j=1:point
           signal(k)=5;
           k=k+1;
         status=1;
         level=1;
         endfor
      endif
     else
      for j=1:point
        signal(k)=0;
        k=k+1;
      endfor
      level=0;
   endif
  endif
endfor
plot(signal);


