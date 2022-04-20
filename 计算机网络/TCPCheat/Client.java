/**
 * @Author: fengsc
 * @Date: 2022-04-20 18:21:21
 * @LastEditTime: 2022-04-20 20:36:52
 */
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws Exception {
        String serverName = InetAddress.getLocalHost().getHostAddress();
        int serverPort = 12000;


        try (Socket clientSocket = new Socket(serverName, serverPort);
                BufferedReader in =
                        new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                BufferedWriter out =
                        new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));
                BufferedReader input = new BufferedReader(new InputStreamReader(System.in));) {
            System.out.println("User name:");
            String userName = input.readLine();
            out.write(userName);
            out.write("\n");// 流结尾标识
            out.flush();
            if (in.readLine().equals("0")) {// queren
                System.out.println("Access denied");
                return;
            }
            System.out.println("User: " + userName + " connect to " + serverName + ":" + serverPort
                    + " successfully");
            while (true) {

                String line = input.readLine();
                out.write(line);
                out.write("\n");
                out.flush();
            }

        } catch (IOException e)// *手动关闭时需要 InterruptedException,有残余线程时报错
        {
            e.printStackTrace();
        }
    }


}
