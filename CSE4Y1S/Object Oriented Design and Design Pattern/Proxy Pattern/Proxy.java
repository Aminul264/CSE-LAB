import java.util.ArrayList;

public class Proxy implements IOrder{
    

    ArrayList<Warehouse>warehouses=new ArrayList<>();

    void addWarehouse(Warehouse warehouse)
    {
        this.warehouses.add(warehouse);
    }

    public void orderFullfil(Order order)
    {
        for(IOrder it: warehouses)
        {
            Warehouse warehouse= (Warehouse)it;

            boolean check=true;
            for(Item item: order.items)
            {
                if(item.count>warehouse.getItemCount(item.name));
                check=false;
            }
            if(check)
            {
                warehouse.orderFullfil(order);
                break;
            }
        }
    }
}
