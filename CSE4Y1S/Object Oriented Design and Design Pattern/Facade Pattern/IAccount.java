public interface IAccount {

    public void deposit(int amount);
    public void withdraw(int amount);
    public void transfer(IAccount toAccount, int amount);
    public int getAccount();

}