/**
 * @Author: fengsc
 * @Date: 2022-04-20 14:21:22
 * @LastEditTime: 2022-04-20 18:45:41
 */
import java.io.*;
import java.net.*;
import java.util.*;

public class TCPClient {
    public static void main(String[] args) throws Exception {
        String serverName = InetAddress.getLocalHost().getHostAddress();
        int serverPort = 12000;
        
        try (Socket clientSocket = new Socket(serverName, serverPort);
                OutputStream out = clientSocket.getOutputStream();
                InputStream in = clientSocket.getInputStream();
                Scanner scanner = new Scanner(System.in);) {
            System.out.println("Connect to " + serverName + ":" + serverPort + " successfully");
            out.write(scanner.next().getBytes());// *编码，传输对象为byte类型
            out.flush();
            clientSocket.shutdownOutput();// *停止输入标志，否则服务器会阻塞以继续接收
            byte[] bytes = new byte[1024];// 缓冲区大小
            int len = in.read(bytes);
            System.out.println(new String(bytes, 0, len));// 解码
        } catch (IOException e)// *手动关闭时需要 InterruptedException,有残余线程时报错
        {
            e.printStackTrace();
        }
    }
}
