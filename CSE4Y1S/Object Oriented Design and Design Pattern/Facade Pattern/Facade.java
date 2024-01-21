import java.util.Hashtable;

public class Facade {
    //acountNumber ,Type
     private Hashtable<Integer,IAccount>bankAccount;

     Facade(){
        this.bankAccount=new Hashtable<Integer,IAccount>();
     }
     public int createNewAccount(String type,int accountNumber,int amount){
        IAccount newAccount=null;

        switch (type) {
            case "chequing":
                newAccount=new Chequing(accountNumber, amount);
                break;
            case "saving":
                newAccount = new Saving(accountNumber, amount);
                break;
            case "investment":
                newAccount= new Investment(accountNumber, amount);
                break;
            default:
                System.out.println("Invalid Account Type");
                break;
        }
        if(newAccount!=null){
            this.bankAccount.put(accountNumber,newAccount);
            return accountNumber;
        }
        else{
            return 0;
        }
     }
    public void deposit(int accountNumber,int amount){
            IAccount type = this.bankAccount.get(accountNumber);
            type.deposit(amount);
    }

    public void withdraw(int accountNumber,int amount){
        IAccount type =this.bankAccount.get(accountNumber);
        type.withdraw(amount);
    }
    public void transfer(int from ,int to,int amount){
        IAccount typeFrom=this.bankAccount.get(from);
        IAccount typeTo=this.bankAccount.get(to);

        typeFrom.transfer(typeTo,amount);
    }
}
