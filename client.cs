using System;
using System.IO;
using System.Net;
using System.Text;
using System.Net.Sockets;
using System.Threading;

namespace dote
{
    class Program
    {
static string GetMessage(TcpClient client, String message)
{
    String responseData = String.Empty;
  try
  {
    // Translate the passed message into ASCII and store it as a Byte array.
    Byte[] data = System.Text.Encoding.ASCII.GetBytes(message);

    NetworkStream stream = client.GetStream();

    // Send the message to the connected TcpServer.
    stream.Write(data, 0, data.Length);

    Console.WriteLine("Sent: {0}", message);

    // Receive the TcpServer.response.

    // Buffer to store the response bytes.
    data = new Byte[256];

    // String to store the response ASCII representation.
    

    // Read the first batch of the TcpServer response bytes.
    Int32 bytes = stream.Read(data, 0, data.Length);
    responseData = System.Text.Encoding.ASCII.GetString(data, 0, bytes);
    
    // Close everything.
    stream.Close();


  }
  catch (ArgumentNullException e)
  {
    Console.WriteLine("ArgumentNullException: {0}", e);
  }
  catch (SocketException e)
  {
    Console.WriteLine("SocketException: {0}", e);
  }    

   return responseData;

  
}

      public static void Main ()
        {
            string server = "127.0.0.1";
            var port = 5600;
            
            int count = 0 ;
            while(count < 1<<24)
            {
                count++;
                string message = string.Format("{0}",count);                
                using (var client = new TcpClient(server,port))
                {
                    var ret_message = GetMessage(client,message);
                    Console.WriteLine(ret_message);
                }       
                Thread.Sleep(500);
            }            
        }
    }
}

