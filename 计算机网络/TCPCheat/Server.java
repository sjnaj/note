
/**
 * @Author: fengsc
 * @Date: 2022-04-20 17:10:52
 * @LastEditTime: 2022-04-20 20:35:56
 */
import java.net.*;
import java.io.*;
import java.util.*;

public class Server {
    public static List<String> list = new ArrayList<>(10);

    final static int MAX_USER_NUM = 10;

    public static void main(String[] args) throws Exception {

        try (

                ServerSocket serverSocket = new ServerSocket(12000);) {
            System.out.println("Ready to get access");
            while (true) {
                Socket userSocket = serverSocket.accept();

                new Thread(() -> {
                    try (BufferedReader in =
                            new BufferedReader(new InputStreamReader(userSocket.getInputStream()));
                            BufferedWriter out = new BufferedWriter(
                                    new OutputStreamWriter(userSocket.getOutputStream()));) {
                        String userName = in.readLine();
                        if (list.size() == MAX_USER_NUM) {// 超过标定容量,返回信号并return
                            out.write("0\n");
                            userSocket.close();
                            return;
                        }
                        list.add(userName);// 添加用户
                        out.write("1\n");
                        out.flush();
                        System.out.println("User: " + userName + " connect to "
                                + userSocket.getRemoteSocketAddress() + " successfully");
                        System.out.println(new Date());
                        System.out.println("Current user: " + list);
                        String input;
                        while ((input = in.readLine()) != null) {
                            System.out.println(userName + " : " + input);
                            System.out.println(new Date());
                        }
                        // 退出循环说明客户端退出
                        userSocket.close();
                        list.remove(userName);
                        System.out.println("User: " + userName + " quit");
                        System.out.println(new Date());
                        System.out.println("Current user: " + list);

                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }).start();
            }
        }
    }
}
