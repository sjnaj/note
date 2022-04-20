
/**
 * @Author: fengsc
 * @Date: 2022-04-20 15:01:19
 * @LastEditTime: 2022-04-20 17:05:16
 */
import java.io.*;
import java.net.*;

public class TCPServer {
    public static void main(String[] args) throws Exception {
        try (ServerSocket serverSocket = new ServerSocket(12000);) {
            System.out.println("Ready to get access");
            while (true) {// 循环接受请求，创建专有套接字
                try (Socket connectionSocket = serverSocket.accept();
                        BufferedReader in = new BufferedReader(
                                new InputStreamReader(connectionSocket.getInputStream()));
                        BufferedWriter out = new BufferedWriter(
                                new OutputStreamWriter(connectionSocket.getOutputStream()));) {
                    // *使用BufferReader和BufferWriter免去编解码
                    System.out.println("Connect to" + ":"
                            + connectionSocket.getRemoteSocketAddress() + " successfully");// 客户端获取地址(ip+端口)
                    String str = in.readLine();

                    System.out.println("get: " + str);
                    out.write(str.toUpperCase());
                    
                } catch (NullPointerException | SocketException e) {// close或中途关闭
                    System.out.println("The client closed the connection");
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
