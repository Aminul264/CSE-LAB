

public class HasOneDollarState implements State {

    public void insertDollar(VendingMachine vendingMachine){
        System.out.println("Already have an dollar");
    }
    public void ejectMoney(VendingMachine vendingMachine){
        System.out.println("Returning money");
        vendingMachine.setState(new IdleState());
    }
    public void dispense(VendingMachine vendingMachine){
        System.out.println("Releasing product");
        int count=vendingMachine.getCount();
        vendingMachine.setCount(count-1);

        if(count>1){
            vendingMachine.setState(new IdleState());
        }
        else{
            vendingMachine.setState(new OutOfStockState());
        }

    }
    
}
