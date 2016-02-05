package com.neusoft.thrift;

import com.neusoft.thrift.ThriftAsync.ThriftAsync;
import org.apache.thrift.TException;
import org.apache.thrift.server.TNonblockingServer;
import org.apache.thrift.server.TServer;
import org.apache.thrift.transport.TNonblockingServerSocket;
import org.apache.thrift.transport.TNonblockingServerTransport;
import org.apache.thrift.transport.TTransportException;

/**
 * [Description]
 *
 * @author: joshua
 * @date: 15-10-30.
 */
public class Server {
    public class ThriftAsyncServiceImpl implements ThriftAsync.Iface {
        @Override
        public long add(int i1, int i2) throws TException {
            return i1 + i2;
        }

        @Override
        public long multiply(int i1, int i2) throws TException {
            return i1 * i2;
        }
    }
    private void start() {
        try {
            TNonblockingServerTransport serverTransport = new TNonblockingServerSocket(9090);
            ThriftAsync.Processor processor = new ThriftAsync.Processor(new ThriftAsyncServiceImpl());
            TServer server = new TNonblockingServer(new TNonblockingServer.Args(serverTransport).processor(processor));
            System.out.println("Starting serve on 9090");
            server.serve();
        } catch (TTransportException e) {
            e.printStackTrace();
        }
    }
    public static void main( String[] args )
    {
        Server srv = new Server();
        srv.start();
    }
}
