public class Saving implements IAccount  {

    private int savingAmount;
    private int accountNumber;

    Saving(int accountNumber,int amount){
        this.accountNumber=accountNumber;
        this.savingAmount=amount;
    }
    public void deposit(int amount){
        this.savingAmount+=amount;
        System.out.println("succesffully deposited : \n Total amount:"+savingAmount);
    }
    public void withdraw(int amount){
        if(this.savingAmount>=amount){
            System.out.println("withdrwan successful");
            this.savingAmount-=amount;
        }
        else{
            System.out.println("Not enough money to withdraw");
        }
    }

    public void transfer(IAccount toAccount,int amount){
        if(this.savingAmount>=amount){
            this.savingAmount-=amount;
            toAccount.deposit(amount);
            System.out.println("transfer successful- Recent Balance :"+savingAmount);
        }
        else{
            System.out.println("Insufficient Balance to transfer");
        }
    }
    public int getAccount(){
        return accountNumber;
    }
}
