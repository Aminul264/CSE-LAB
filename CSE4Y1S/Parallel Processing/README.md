

 
   compile : mpicxx matrix.cpp -o matrix
   terminal input
   run     : mpirun -n 4 ./matrix
   file input
   run     :mpirun -n 4 ./matrix < input.txt (for one input file)

