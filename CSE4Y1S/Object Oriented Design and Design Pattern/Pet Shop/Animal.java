abstract class Animal {

    String name,type;

    void eat(){
        System.out.println(this.name+"is eating");
    }
    abstract void sound();
}
