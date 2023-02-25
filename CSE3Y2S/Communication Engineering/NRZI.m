#NRZI : Rule
#bit 1 : transition
#bit 0 : no transition


data =[0 1 1 0 1 0 0];
#substitute one point to 200
point=200;
signal =zeros(length(data)*point);
status=1;
k=1;
for i=1:length(data)
  if data(i)==0
      if status==1
        for j=1:point
          signal(k)=5;
          k=k+1;
        endfor
        status=1;
      else
        for j=1:point
          signal(k)=-5;
          k=k+1;
        endfor
        status=-1
      endif
  else
     if status==1
       for j=1:point
          signal(k)=-5;
          k=k+1;
       endfor
       status=-1;
     else
       for j=1:point
          signal(k)=5;
          k=k+1;
       endfor
       status=1
    endif
  endif
endfor

plot(signal);
ylim([-5 5]);


