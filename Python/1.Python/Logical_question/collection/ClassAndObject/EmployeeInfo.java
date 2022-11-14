//Write a program that would print the information (name, year of joining, salary, address) of three employees by creating a class named 'Employee'. The output should be as follows:
  //      Name        Year of joining        Address
  //      Robert            1994                64C- Wall Street
    //    Sam                2000                68D- Wall Street
    //    John                1999                26B- Wall Street


        package ClassAndObject;

class Employee{
    String name;
    int DOJ;
    int salary;
    String Address;

    Employee(String naam, int JoiningYear, int Paisa, String Thau){
        this.name=naam;
        this.DOJ=JoiningYear;
        this.salary=Paisa;
        this.Address=Thau;
    }

    public void displayInfo(){
        System.out.println(this.name+"        "+this.DOJ+"        "+salary+"        "+Address);
    }
}

public class EmployeeInfo {
    public static void main(String[] args) {
        System.out.println("Name        DOJ        salary        Address");
        Employee e1 = new Employee("Ravi",1998,5000,"Imadol");
        Employee e2 = new Employee("Saam",1997,5100,"Nepalgunj");
        Employee e3 = new Employee("John",2000,6000,"Kanpur");
        Employee e4 = new Employee("Aksh",2015,7000,"Janakpur");

        e1.displayInfo();
        e2.displayInfo();
        e3.displayInfo();
        e4.displayInfo();
    }
}
