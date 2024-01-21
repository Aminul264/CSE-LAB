public class Investment implements IAccount  {

    private int accountNumber;
    private int investmentAmount;

    Investment(int accountNumber,int amount){
        this.accountNumber=accountNumber;
        this.investmentAmount=amount;
    }

    public void deposit(int amount){
        this.investmentAmount+=amount;
        System.out.println("succesffully deposited\nTotal amount :"+investmentAmount);
    }
    public void withdraw(int amount){
        if(this.investmentAmount>=amount){
            this.investmentAmount-=amount;
            System.out.println("succesfully withdrawn");
        }
        else{
            System.out.println("Insufficient Balance to withdraw");
        }
    }

    public void transfer(IAccount toAccount,int amount){
        if(this.investmentAmount>=amount){
            this.investmentAmount-=amount;
            toAccount.deposit(amount);
            System.out.println("sucessfully transfered and Recent Balance :"+this.investmentAmount);
        }
        else{
            System.out.println("Insufficient Amount to Transfer ");
        }
    }
    public int getAccount(){
        return accountNumber;
    }
}
