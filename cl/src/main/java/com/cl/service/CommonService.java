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

    public SingleServerDTO validSingleServer(SingleServerRequest request) {
        SingleServerDTO dto = new SingleServerDTO();
        boolean validStatus = serverService.validSingleServer(request);
        if (validStatus) {
            Server server = request.server;
            User currentUser = userService.getCurrentLoginUser();
            Long team = currentUser.getTeam().getId();
            server.setTeam(team);
            commonDao.saveDBOject(server);
            dto.server = server;
        }
        return dto;
    }

    public SingleServerWarnDTO validSingleServerComponents(SingleServerComponentsRequest request) {

        return null;
    }

}
