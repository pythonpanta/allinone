//Write a program to print the names of students by creating a Student class. If no name is passed while
// creating an object of Student class, then the name should be "Unknown", otherwise the name should be equal
// to the String value passed while creating object of Student class.

package Constructor;

public class Student {
    String name;

    Student() {
        name = "UNKNOWN";
    }

    Student(String naam) {
        this.name = naam;
    }

    public void display() {
        System.out.println("YOU ENTERED: " + this.name);
    }

    public static void main(String[] args) {
        Student s = new Student();
        Student s1 = new Student("Apple");
        s.display();
        s1.display();
    }
}
