public class MAIL
{
    public static void main(String args[]) throws Exception
    {
        int delay =1000;
        String user="s1910676129@ru.ac.bd";
        String pass="64d89de2ff";
        String username= new String (Base64.getEncoder().encode(user.getBytes()));
        String password = new String (Base64.getEncode().encode(pass.getBytes()));
        SSLSocketFactory sslsocketfactory =(SSLSocketFactory)SSLSocketFactory.getDefault();

        SSLSocket  sock = (SSLSocket)sslsocketfactory.createSocket("smtp.gmail.com",465);

        final BufferedReader br = new BufferedReader (new InputStreamReader(sock.getInputStream()));

        dos = new DataOutputStream(sock.getOutputStream());



        send("EHLO smtp.gmsil.com\r\n");
        Thread.sleep(delay);
        System.out.println("SERVER: "+br.readLine());
        System.out.println("SERVER: "+br.readLine());
        System.out.println("SERVER: "+br.readline());
        System.out.println("SERVER: "+br.readLine());
        System.out.println("SERVER: "+br.readLine());
        System.out.println("SERVER: "+br.readline());
        System.out.println("SERVER: "+br.readLine());
        System.out.println("SERVER: "+br.readLine());
        System.out.println("SERVER: "+br.readline());

        send("AUTH LOGIN\r\n");
        Thread.sleep(delay);
        System.out.println("SERVER:"+br.readline());


        send(username +"\r\n");
        Thread.sleep(delay);
        System.out.println("SERVER:"+br.readline());

        send(password +"\r\n");
        Thread.sleep(delay);
        System.out.println("SERVER:"+br.readline());

        send("MAIL FROM:<s1910676129@ru.ac.bd>\r\n");
        Thread.sleep(delay);
        System.out.println("SERVER:"+br.readline());

        send("RCPT TO:<aminulislam681538@gmail.com>\r\n");
        Thread.sleep(delay);
        System.out.println("SERVER:"+br.readline());

        send("DATA\r\n");
        Thread.sleep(delay);
        System.out.println("SERVER:"+br.readline());

        send("hello sir,this is body part of the mail");
        send(".\r\n");
        Thred.sleep(delay);
        


        







    
    }
    public static void send(String s) throws Exception
    {
        dos.writeBytes(s);
        System.out.println("Client : "+s);
    }


}