package com.neusoft.thrift;

import com.neusoft.thrift.ThriftAsync.ThriftAsync;
import org.apache.thrift.TException;
import org.apache.thrift.async.AsyncMethodCallback;
import org.apache.thrift.async.TAsyncClientManager;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.transport.TNonblockingSocket;

import java.io.IOException;

/**
 * Hello world!
 *
 */
public class Client
{
    private void invoke() {
        try {
            ThriftAsync.AsyncClient client = new ThriftAsync.AsyncClient(
                    new TBinaryProtocol.Factory(), new TAsyncClientManager(),
                    new TNonblockingSocket("localhost", 9097)
            );
            client.add(12, 23, new AddMethodCallback());
        } catch (IOException e) {
            e.printStackTrace();
        } catch (TException e) {
            e.printStackTrace();
        }
    }
    public static void main( String[] args )
    {
        Client client = new Client();
        client.invoke();
        System.out.println("Done!");
    }

    class AddMethodCallback implements AsyncMethodCallback<ThriftAsync.AsyncClient.add_call> {

        @Override
        public void onComplete(ThriftAsync.AsyncClient.add_call add_call) {
            try {
                long result = add_call.getResult();
                System.out.println("Add from server: " + result);
            } catch (TException e) {
                e.printStackTrace();
            }
        }

        @Override
        public void onError(Exception e) {
            System.out.println("Error : ");
            e.printStackTrace();
        }
    }
}
