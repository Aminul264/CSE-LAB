public class Chequing implements IAccount  {

    private int accountNumber;
    private int chequingAmount;

    Chequing(int accountNumber,int amount){
        this.accountNumber=accountNumber;
        this.chequingAmount=amount;
    }

    public void deposit(int amount){
        this.chequingAmount+=amount;
        System.out.println("succesffully deposited : \n Total amount:"+chequingAmount);
    }
    public void withdraw(int amount){
        if(this.chequingAmount>=amount){
            this.chequingAmount-=amount;
            System.out.println("successfully withdrawn");
        }
        else{
            System.out.println("Insufficient Amount");
        }
    }

    public void transfer(IAccount toAccount,int amount){
        if(this.chequingAmount>=amount){
            this.chequingAmount-=amount;
            toAccount.deposit(amount);
            System.out.println("Successfully transferd");
        }
        else{
            System.out.println("Transferd failed-insufficient amount");
        }
    }
    public int getAccount(){
        return accountNumber;
    }
}
