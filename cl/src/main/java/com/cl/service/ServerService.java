package com.cl.service;

import com.cl.request.SingleServerRequest;
import org.springframework.stereotype.Service;

/**
 * Created by chengxj on 2015/10/22.
 */
@Service
public class ServerService {

    /**
     *
     * @param request
     * @return
     */
    public boolean validSingleServer(SingleServerRequest request) {
    	
        return true;
    }

}
