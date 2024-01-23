import java.util.ArrayList;

public class PetShop {
    
    String shopName;
    ArrayList<Animal> pets=new ArrayList<>();

    PetShop(String name)
    {
        this.shopName=name;
    }

    int addPet(Animal pet)
    {
        this.pets.add(pet);
        return pets.size()-1;
    }

    void sell(String name)
    {
        int i=-1;
        boolean find=false;
        for(Animal pet: pets)
        {  
            i++;
            if(pet.name.equals(name))
            {
                find=true;
                break;
            }
        }
        if(!find)
        {
            System.out.println("pet not found");
        }
        else
        {
            pets.remove(i);
        }
    }
}
