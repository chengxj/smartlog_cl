package com.cl.service.python;

import org.apache.thrift.TException;
import com.cl.service.python.pythonServiceApi.Iface;

public class pythonService implements Iface {

	@Override
	public ServerDTO validSingleServer(Server server) throws TException {
		// TODO Auto-generated method stub
		ServerDTO dto = new ServerDTO();
		dto.available = true;
		dto.hostname = "cxj001";
		return dto;
	}


}
