//import javax.print.DocFlavor;
import org.cups4j.CupsClient;
import org.cups4j.CupsPrinter;
import org.cups4j.PrintJob;
import org.cups4j.PrintRequestResult;

import javax.print.PrintService;
import javax.print.PrintServiceLookup;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {

        CupsClient client = new CupsClient("127.0.0.1", 631);
        List<CupsPrinter> printers = client.getPrinters();
        CupsPrinter selectedPrinter = null;
        if (printers.size() == 0) {
            throw new RuntimeException("Cant list Printer");
        }
        
        for (CupsPrinter cupsPrinter : printers) {
            if (cupsPrinter.getName().equals("Canon_MF3010")) {
                System.out.println(cupsPrinter);
                selectedPrinter = cupsPrinter;
                String str = "ABCGVDVJHBDKDLNJOKBU" +
                        "\n HODVWFCVDHGSBDKS";
                byte[] inputStream = str.getBytes();;
                PrintJob printJob = new PrintJob.Builder(inputStream).jobName("Jobname").build();
                PrintRequestResult result = selectedPrinter.print(printJob);
            }
        }



//
        PrintService[] printServices = PrintServiceLookup.lookupPrintServices(null, null);
//        System.out.println(cupsPrinter);

    }
}
