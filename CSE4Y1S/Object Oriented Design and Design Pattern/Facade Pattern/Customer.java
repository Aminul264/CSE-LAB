
public class Customer {
    public static void main(String[] args) {
        Facade facade = new Facade();

        int x= facade.createNewAccount("saving",101,1000);
        // System.out.println(x);
        // facade.deposit(101,100);

        int y= facade.createNewAccount("investment",102,1000);
        // System.out.println(y);
        // facade.deposit(102,1);

        // facade.withdraw(101,1000);
        // facade.withdraw(101,1000);
        facade.transfer(101,102,1000);





        
    }
}
