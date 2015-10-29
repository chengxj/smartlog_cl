package com.cl.service.python;

import org.apache.thrift.TException;  
import org.apache.thrift.protocol.TBinaryProtocol;  
import org.apache.thrift.protocol.TProtocol;  
import org.apache.thrift.transport.TSocket;  
import org.apache.thrift.transport.TTransport;  
import org.apache.thrift.transport.TTransportException;  

public class ClientTest {
	
	public void startClient() {  
        TTransport transport;  
        try {  
            transport = new TSocket("127.0.0.1", 9091);  
            TProtocol protocol = new TBinaryProtocol(transport);  
            pythonServiceApi.Client client = new pythonServiceApi.Client(protocol);  
            transport.open();  
            System.out.println(client.validSingleServer(null));  
            transport.close();  
        } catch (TTransportException e) {  
            e.printStackTrace();  
        } catch (TException e) {  
            e.printStackTrace();  
        }  
    }  
  
    public static void main(String[] args) {  
    	ClientTest client = new ClientTest();  
        client.startClient();  
    }

}
