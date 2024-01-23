import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        String[] cateName={"cat1","cat2","cat3"};
        String[] dogName={"dog1","dog2","dog3"};


        Cat cat;
        Dog dog;
        PetShop petShop = new PetShop("My Shop");

        for(int i=0;i<cateName.length;i++)
        {
            cat =new Cat(cateName[i],"deshi");
            dog= new Dog(dogName[i],"bideshi");
            petShop.addPet(cat);
            petShop.addPet(dog);
        }

        //
        for(Animal pet : petShop.pets)
        {
            System.out.println(pet.name);

        }

        Scanner input = new Scanner(System.in);
        String name;

        while(true)
        {
            System.out.println("Enter a name: ");
            name = input.nextLine();
            petShop.sell(name);

            for(Animal pet :petShop.pets)
            {
                System.out.println(pet.name);
            }
        }


    }
}
