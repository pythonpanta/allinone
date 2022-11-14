//8.Create a class named Bank which should contain the following data members [state]
//id  Long
//bankName String
//baseInterestRate Double
//numberOfBranch Integer
//headOfficeAddress String
//bankCategory String

//9.Make all the variables of bank private

//10.Create a function in bank class which should display all the data members inside a bank in following format
//BANK  ID : 1
//BANK NAME : GLOBAL BANK
//BASE INTEREST RATE : 20 %
//NUMBER OF BRANCH : 100
//HEAD OFFICE ADDRESS : TEXAS
//BANK CATEGORY : A CATEGORY


//11.Create another class named BankProgram which should have a main method
//Inside main method create an object ko bank class with name bankObject
//Call a function that displays all the bank data members
//Try to set the data to bank name using
//bankObject.bankName = “Himalayan Bank”;
//What error do you see ? Why ? Think about it !!
//Create a constructor in Bank Class which has all the parameters in Bank class.
//After creating the constructor, you will see some errors in BankProgram. Remember once you create a parameterized constructor JVM will not create a default constructor for you. So, you have to create a No Argument Constructor yourself.
//I hope the error is gone.


//12.Now create a new object of the bank named bankObject1 and pass all parameters in the constructor and display it calling a method in the Bank class.


//13.Create another constructor with any three parameters and again call the display method in the bank class.

package Constructor;

public class Bank {
    private long id;
    private String bankName;
    private Double baseInterestRate;
    private int numberOfBranch;
    private String headOfficeAddress;
    private String bankCategory;

    Bank() {
    }

    Bank(long id, String bname, Double rate, int branch, String add, String category) {
        this.id = id;
        this.bankName = bname;
        this.baseInterestRate = rate;
        this.numberOfBranch = branch;
        this.headOfficeAddress = add;
        this.bankCategory = category;
    }

    Bank(long id, String bname, int branch, String category) {
        this.id = id;
        this.bankName = bname;
        this.numberOfBranch = branch;
        this.bankCategory = category;
    }

    public void displayData() {
        System.out.println("BANK  ID :" + this.id);
        System.out.println("BANK NAME :" + this.bankName);
        System.out.println("BASE INTEREST RATE :" + this.baseInterestRate + "%");
        System.out.println("NUMBER OF BRANCH :" + this.numberOfBranch);
        System.out.println("HEAD OFFICE ADDRESS :" + this.headOfficeAddress);
        System.out.println("BANK CATEGORY : " + this.bankCategory + " CATEGORY");
    }
}

class BankProgram {
    public static void main(String[] args) {
        Bank bankObject = new Bank(1, "GLOBAL BANK", 20.0, 100, "TEXAS", "A");
        bankObject.displayData();
        System.out.println();
        Bank bankObject1 = new Bank(2, "CIVIL BANK", 86, "A");
        bankObject1.displayData();
    }
}