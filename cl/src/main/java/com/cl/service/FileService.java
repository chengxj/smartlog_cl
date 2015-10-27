package com.cl.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Created by chengxj on 2015/10/20.
 */
@Service
public class FileService {

    @Autowired
    private CmdService cmdService;

    public void createFileDir() {
//        String testShell = "mkdir chengxj" + (new Date()).getTime();
        String testShell = "mkdir chengxj";
        cmdService.exec(testShell);

    }

}
