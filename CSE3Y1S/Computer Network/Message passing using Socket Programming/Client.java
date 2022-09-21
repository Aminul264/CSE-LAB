import java.net.*;
import java.io.*;


public class Client
{
    public static void main(String args[]) throws Exception
    {
        Socket socket = new Socket("localhost",4444);
        DataOutputStream dis = new DataOutputStream(socket.getOutputStream());
        dis.writeUTF("Fuck Your Comfort Zone");
        dis.flush();
        dis.close();
    }
}
