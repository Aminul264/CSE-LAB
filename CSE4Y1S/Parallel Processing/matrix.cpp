
/* 
   compile : mpicxx matrix.cpp -o matrix
   terminal input
   run     : mpirun -n 4 ./matrix

           :mpirun -n 4 ./matrix < input.txt (for one input file)
*/
#include<bits/stdc++.h>
#include<mpi.h>
using namespace std;


void send_a_number(int number,int to){
    MPI_Send( &number , 1 , MPI_INT, to , 0 , MPI_COMM_WORLD);
}
int receive_a_number(int from){
    int len;
    MPI_Recv( &len, 1, MPI_INT ,from , 0 , MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    return len;
}
vector<int> receive_a_array(int from,int len){

    vector<int>ans(len);
    MPI_Recv( &ans[0] , len, MPI_INT ,from , 0 , MPI_COMM_WORLD , MPI_STATUS_IGNORE);
    return ans;
}
void send_a_array(int *arr,int sz,int to){
    MPI_Send( arr , sz , MPI_INT , to , 0,MPI_COMM_WORLD);
}


vector<int>multiplication(int *A,int *B,int n,int m,int p,int matrix_number){

    vector<int>C(n*p*matrix_number);

    for(int x=0;x<matrix_number;x++){
        //base adress 
        int add_a=x*n*m;
        int add_b=x*m*p;
        int add_c=x*n*p;

        for(int i=0;i<n;i++){
            for(int j=0;j<p;j++){
                int sum=0;
                for(int k=0;k<m;k++){
                    sum+=A[add_a+i*m+k]*B[add_b+k*p+j];
                }
                C[add_c+i*p+j]=sum;
            }
        }
    }
    return C;

}
int main(int argc,char *argv[]){

    MPI_Init(&argc,&argv);
    int rank,number_of_process;
    MPI_Comm_size( MPI_COMM_WORLD, &number_of_process);
    MPI_Comm_rank( MPI_COMM_WORLD, &rank);


    if(rank==0){
        int k,m,n,p;
        cin>>k>>n>>m>>p;
        cout<<"number of matrix: "<<k<<endl;
        cout<<"dimention of matrix A,B and C: \n";
        cout<<"Dimentio A: "<<n<<"x"<<m;
        cout<<"\ndimention B:"<<m<<"x"<<p;
        cout<<"\ndimention C:"<<n<<"x"<<p<<endl;

        //assign matrix,a and b =1
        int *A,*B;
        int len_a=k*n*m;//size of matrix A
        int len_b=k*m*p;////size of matrix B

        A=new int[len_a];
        B=new int[len_b];
        
        for(int i=0;i<len_a;i++){
            A[i]=1;
        }
        for(int i=0;i<len_b;i++){
            B[i]=1;
        }


        clock_t start,end;
        start = clock();

        for(int i=1;i<number_of_process;i++)
        {
                // koto gula kore matrix pabe
            int start_pos=i*(k/number_of_process);
            int end_pos=(i+1)*(k/number_of_process);
            if(i==number_of_process-1)
            {
                    end_pos=k;
            }

            send_a_number(n,i);
            send_a_number(m,i);
            send_a_number(p,i);
            //koyta matrix niye kaj korbe
            send_a_number(end_pos-start_pos,i);
          
            //  datar reference pass before size of data
            //for A and B
            int range_a_start=start_pos*n*m;
            int range_a_end=end_pos*n*m;
            int range_a=range_a_end-range_a_start;
            send_a_number(range_a,i);
            send_a_array(A+range_a_start,range_a,i);

            int range_b_start=start_pos*m*p;
            int range_b_end=end_pos*m*p;
            int range_b=range_b_end-range_b_start;
            send_a_number(range_b,i);
            send_a_array(B+range_b_start,range_b,i);
        }
        
        vector<int>C=multiplication(&A[0],&B[0],n,m,p,k/number_of_process);

        for(int i=1;i<number_of_process;i++)
        {
            int len=receive_a_number(i);
            vector<int>temp=receive_a_array(i,len);
            for(int j=0;j<len;j++){
                C.push_back(temp[j]);
            }
            //total_time+=
        }

        end=clock();
        double time=(end-start)/(double)CLOCKS_PER_SEC;
        cout<<"Cpu time taken by Rank: "<<rank<<" "<<time<<endl;
        // total_time+=time;


    }
    else{

        clock_t start,end;
        start =clock();

        int n=receive_a_number(0);
        int m=receive_a_number(0);
        int p=receive_a_number(0);
        int num_of_matrix=receive_a_number(0);

        int range_a=receive_a_number(0);
        vector<int>A=receive_a_array(0,range_a);

        int range_b= receive_a_number(0);
        vector<int>B=receive_a_array(0,range_b);

        vector<int>C=multiplication(&A[0],&B[0],n,m,p,num_of_matrix);

        send_a_number(C.size(),0);
        send_a_array(&C[0],C.size(),0);


    //   end=clock();
    //   double time=(end-start)/(double)CLOCKS_PER_SEC;
    //   cout<<"Cpu time taken by Rank: "<<rank<<" "<<time<<endl;

      //send_a_number(time,0);

    }

    MPI_Finalize();
}
