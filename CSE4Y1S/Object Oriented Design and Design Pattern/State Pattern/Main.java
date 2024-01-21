

public class Main {
    public static void main(String[] args) {
        
        VendingMachine vendingMachine =new VendingMachine(3);
        vendingMachine.insertDollar();
        vendingMachine.insertDollar();
        vendingMachine.dispense();
        vendingMachine.ejectMoney();

    }
    
}
