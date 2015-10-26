package com.cl.service;

import com.cl.dto.SingleServerDTO;
import com.cl.dto.SingleServerWarnDTO;
import com.cl.entity.Server;
import com.cl.entity.common.User;
import com.cl.request.SingleServerComponentsRequest;
import com.cl.request.SingleServerRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.cl.dao.CommonDao;
import com.cl.dao.SearchDao;

@Service
public class CommonService {

    protected Logger log = LoggerFactory.getLogger(this.getClass());

    @Autowired
    private SearchDao searchDao;

    @Autowired
    private CommonDao commonDao;

    @Autowired
    private DTOHelper dtoHelper;

    @Autowired
    private ServerService serverService;

    @Autowired
    private UserService userService;

    /**
     * 
     * @param request
     * @return
     */
    public SingleServerDTO validSingleServer(SingleServerRequest request) {
        SingleServerDTO dto = new SingleServerDTO();
        // 已存在的记录就不用验证，直接通过。
        // 不存在的记录需要验证，通过后，保存一份。
        Server server = searchDao.findExistServer(request.server);
        if (server != null && server.getId() != null) {
        	dto.success = true;
        	dto.server = server;
        } else {
            boolean validStatus = serverService.validSingleServer(request);
            if (validStatus) {
            	dto.success = true;
                Server newServer = request.server;
                User currentUser = userService.getCurrentLoginUser();
                Long team = currentUser.getTeam().getId();
                newServer.setTeam(team);
                commonDao.saveDBOject(newServer);
                dto.server = newServer;                
            } else {
            	dto.success = false;            	
            }
        }
        return dto;
    }

    public SingleServerWarnDTO validSingleServerComponents(SingleServerComponentsRequest request) {

        return null;
    }

}
