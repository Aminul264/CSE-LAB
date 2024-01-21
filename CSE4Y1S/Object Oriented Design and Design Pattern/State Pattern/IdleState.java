
public class IdleState implements State{

   public void insertDollar(VendingMachine vendingMachine){

    // State state= new HasOneDollarState();
        System.out.println("Dollar Inserted");

        vendingMachine.setState(
            //vendingMachine.getHasOneDollarState()
            new HasOneDollarState()
            // state
        );
        System.out.println("hello");
   }
   public void ejectMoney(VendingMachine vendingMachine){
    System.out.println("No money to return");
   }
   public void dispense(VendingMachine vendingMachine){
    System.out.println("Payment required");
   } 
}
