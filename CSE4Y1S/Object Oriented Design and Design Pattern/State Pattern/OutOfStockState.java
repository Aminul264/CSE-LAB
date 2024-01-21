

public class OutOfStockState implements State {
    public void insertDollar(VendingMachine vendingMachine){
        System.out.println("Out of Stock");

    }
    public void ejectMoney(VendingMachine vendingMachine){
        System.out.println("Out of Stock");

    }
    public void dispense(VendingMachine vendingMachine){
        System.out.println("Out of Stock");

    }
}
