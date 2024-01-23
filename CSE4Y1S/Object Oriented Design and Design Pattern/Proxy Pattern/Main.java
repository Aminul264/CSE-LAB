public class Main {
    public static void main(String[] args) {
        
      
        
        String []products={"shampoo","toothPaste","soup","brush","noteBook","pen"};


        Warehouse warehouse = new Warehouse();

        Item item;

        for(int i=0;i<products.length;i++)
        {
            item =new Item(products[i], 100);
            warehouse.addItem(item);
        }
        Order order = new Order();

        for(int i=0;i<4;i++)
        {
            item= new  Item(products[i],2);
            order.addItem(item);
        }

        Proxy proxy =new Proxy();
        proxy.addWarehouse(warehouse);


        //proxy.orderFullfil(order);
        //proxy.orderFullfil(order);
        //proxy.orderFullfil(order);

        for(String name: products)
        {
            System.out.println(warehouse.getItemCount(name));
        }

    }
}
