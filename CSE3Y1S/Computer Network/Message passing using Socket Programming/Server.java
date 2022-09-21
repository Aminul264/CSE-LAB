import java.net.*;
import java.io.*;

public class Server
{
    public static void main(String args[]) throws Exception
    {
       ServerSocket server = new ServerSocket(4444);
       Socket socket = server.accept();
       DataInputStream dis = new DataInputStream(socket.getInputStream());
       String str = dis.readUTF();
       System.out.println(str);
       dis.close();
    }
}