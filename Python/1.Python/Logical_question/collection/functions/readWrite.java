package functions;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class readWrite {
    public static void ReadWrite() throws IOException {
        FileReader fr = new FileReader("/home/bitch/Downloads/InfoDev_Training/src/functions/input.txt");
        FileWriter fw = new FileWriter("/home/bitch/Downloads/InfoDev_Training/src/functions/output.txt");

        String str = "";
        int i;
        while ((i = fr.read()) != -1) {
            str += (char)i;
        }
        System.out.println(str);
        fw.write(str);
        fr.close();
        fw.close();
        System.out.println("File reading and writing both done");
    }

    public static void main(String[] args) throws IOException {
        ReadWrite();
    }
}
