//Assign and print the roll number, phone number and address of two students having names
// "Sam" and "John" respectively by creating two objects of class 'Student'.

package ClassAndObject;

class Student1{
    String name;
    String phoneNumber;
    String Address;

    Student1(String naam , String mobileNo , String Add){
        this.name = naam;
        this.phoneNumber = mobileNo;
        this.Address = Add;
    }
    public void displayInfo(){
        System.out.println("Name = "+this.name);
        System.out.println("Phone Number = "+this.phoneNumber);
        System.out.println("Address = "+this.Address);
    }
}

public class RollPhoneAddress {
    public static void main(String[] args) {
        Student1 s1 = new Student1("John","9818491379","Kupondole");
        Student1 s2 = new Student1("Sam","9748367701","Imadol");
        s1.displayInfo();;
        s2.displayInfo();
    }
}
