public class VendingMachine{
    
    private State idleState;
    private State hasOneDollarState;
    private State outOfStockState;
    
    private int count;
    private State currentState;

    public VendingMachine(int count){

        idleState =new IdleState();
        outOfStockState=new OutOfStockState();

        this.count=count;
        if(count>0){
            this.currentState=idleState;
        }
        else{
            this.currentState=outOfStockState;
        }
    }
    
    //set
    public void setState(State state){
        this.currentState=state;
    }
    public void setCount(int n){
        this.count=n;
    }


    //get
    public int getCount(){
        return this.count;
    }


    public void insertDollar(){
        this.currentState.insertDollar(this);
    }
    public void  ejectMoney(){
        this.currentState.ejectMoney(this);
    }
    public void dispense(){
        this.currentState.dispense(this);
    }

}