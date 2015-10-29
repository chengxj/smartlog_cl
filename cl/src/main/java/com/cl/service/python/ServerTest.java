package com.cl.service.python;

import org.apache.thrift.protocol.TBinaryProtocol;  
import org.apache.thrift.protocol.TBinaryProtocol.Factory;  
import org.apache.thrift.server.TServer;  
import org.apache.thrift.server.TThreadPoolServer;  
import org.apache.thrift.server.TThreadPoolServer.Args;  
import org.apache.thrift.transport.TServerSocket;  
import org.apache.thrift.transport.TTransportException;  

public class ServerTest {
	
	public void startServer() {  
        try {  
            TServerSocket serverTransport = new TServerSocket(4321);
            pythonServiceApi.Processor process = new pythonServiceApi.Processor(new pythonService());  
            Factory portFactory = new TBinaryProtocol.Factory(true, true);  
            Args args = new Args(serverTransport);  
            args.processor(process);  
            args.protocolFactory(portFactory);  
            TServer server = new TThreadPoolServer(args);  
            server.serve();  
        } catch (TTransportException e) {  
            e.printStackTrace();  
        }  
    }  
      
    public static void main(String[] args) {  
    	ServerTest server = new ServerTest();  
        server.startServer();  
    }

}
