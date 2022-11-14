//17.Write a constructor in the Car class given below that initializes the brand class field with the string “Ford”.
//Call the getBrand() method in the main method of the Sample class  and store the value of the brand in a variable, and print the value.

package Constructor;

public class Car {
    String brand;

    Car(){
        this.brand="FORD";
    }

    public String getBrand(){
        return this.brand;
    }

    public static void main(String[] args) {
        Car c = new Car();
        String brand = c.getBrand();
        System.out.println("The Brand of the car is: "+brand);
    }
}
