import java.io.*;
import java.net.*;

public class App {
    public static void main(String[] args) throws Exception {
        ServerSocket server = new ServerSocket(8080);
        System.out.println("Server started on port 8080");

        while (true) {
            Socket socket = server.accept();

            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            out.println("HTTP/1.1 200 OK");
            out.println("Content-Type: text/plain");
            out.println();
            out.println("Hello everyone, this is Docker Challenge Day 35.");

            socket.close();
        }
    }
}
