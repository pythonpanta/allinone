//Create an abstract class 'Bank' with an abstract method 'getBalance'. $100, $150 and $200 are deposited
// in banks A, B and C respectively. 'BankA', 'BankB' and 'BankC' are subclasses of class 'Bank', each having
// a method named 'getBalance'. Call this method by creating an object of each of the three classes.

package Abstraction;

abstract class Bank{
    int balance;
    abstract int getBalance(int bBalance);
}
class A extends Bank{
    @Override
    int getBalance(int bBalance) {
        this.balance=bBalance;
        return bBalance;
    }
}

class B extends Bank{

    @Override
    int getBalance(int bBalance) {
        this.balance=bBalance;
        return bBalance;
    }
}

class C extends Bank{

    @Override
    int getBalance(int bBalance) {
        this.balance=bBalance;
        return bBalance;
    }
}

public class Banking {
    public static void main(String[] args) {
        A a = new A();
        System.out.println("Bank Balance in Account A is $"+a.getBalance(100));
        B b = new B();
        System.out.println("Bank Balance in Account B is $"+b.getBalance(150));
        C c = new C();
        System.out.println("Bank Balance in Account C is $"+c.getBalance(200));
    }
}
