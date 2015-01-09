package com.neusoft.speech2text;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TCompactProtocol;
import org.apache.thrift.protocol.TJSONProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

/**
 * Hello world!
 *
 */
public class App 
{
    public static final String SERVER_IP = "10.10.118.124";
    public static final int SERVER_PORT = 9090;
    public static final int TIMEOUT = 100000;

    /**
     *
     * @param userName
     */
    public void startClient() {
        TTransport transport = null;
        try {
            transport = new TSocket(SERVER_IP, SERVER_PORT, TIMEOUT);
            // transport = TBufferedTransport(transport);
            TProtocol protocol = new TBinaryProtocol(transport);
            // TProtocol protocol = new TCompactProtocol(transport);
            // TProtocol protocol = new TJSONProtocol(transport);
            SpeechRecService.Client client = new SpeechRecService.Client(protocol);
            transport.open();
            String result = client.SpeechRec("http://10.1.0.231:8080/resource/media-asr/20150525.wav");
            System.out.println("Thrify client result =: " + result);
        } catch (TTransportException e) {
            e.printStackTrace();
        } catch (TException e) {
            e.printStackTrace();
        } finally {
            if (null != transport) {
                transport.close();
            }
        }
    }

    public static void main( String[] args )
    {
        App client = new App();
        client.startClient();
    }
}
