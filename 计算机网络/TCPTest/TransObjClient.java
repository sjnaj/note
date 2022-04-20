
/**
 * @Author: fengsc
 * @Date: 2022-04-20 15:55:47
 * @LastEditTime: 2022-04-20 15:56:53
 */
import java.net.*;
import java.io.*;
class User implements java.io.Serializable
{
    private String name;
    private String password;
    public User(String name,String password)
    {
        this.name=name;
        this.password=password;
    }
    public String getName()
    {
        return name;
    }
    public void setName(String name)
    {
        this.name=name;
    }
    public String getPassword()
    {
        return password;
    }
    public void setPassword(String password)
    {
        this.password=password;
    }
}
public class TransObjClient  {
    public static void main(String[] args) throws Exception{
        
    }

    
}