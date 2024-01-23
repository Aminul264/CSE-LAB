import java.util.Hashtable;

public class Warehouse implements IOrder{
    
    //name ,count
    Hashtable<String,Integer>stock=new Hashtable<>();
    
    void addItem(Item item)
    {
        this.stock.put(item.name, item.count);

    }
    int getItemCount(String name)
    {
        if(this.stock.containsKey(name))
        {
           return stock.get(name);
        }
        return 0;
    }

    public void  orderFullfil(Order order)
    {
        for(Item item :order.items)
        {
            int x=stock.get(item.name);
            stock.put(item.name, x-item.count);
        }
    }

}
