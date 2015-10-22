package com.cl.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.io.*;

/**
 * Created by chengxj on 2015/10/20.
 */
@Service
public class CmdService {

    protected Logger log = LoggerFactory.getLogger(this.getClass());

    /**
     * 执行脚本命令
     * @param command
    */
    public void exec(String command) {
        String shell = getShell(command);
        try {
            Runtime runtime = Runtime.getRuntime();
//            File file = new File("c:\\User\\chengxj");
//            Process process = runtime.exec(shell, null, file);
            Process process = runtime.exec(shell);
            InputStream stdin = process.getInputStream();
            InputStreamReader isr = new InputStreamReader(stdin);
            BufferedReader br = new BufferedReader(isr);
            String line = null;
            log.info("<output></output>");
            while ((line = br.readLine()) != null)
                log.info(line);
            int exitVal = process.waitFor();
            log.info("Process exitValue: " + exitVal);
        } catch (Exception e) {
            log.info(shell + "执行脚本出错!");
        }
    }

    /**
     * 获取当前系统下的执行脚本
     * @param command
     * @return
     */
    private String getShell(String command) {
        String os = getCurrentOS();
        String shell = "cmd /c ";
        if ("Windows".equals(os)) {
            shell += command;
        } else {
            shell = command;
        }
        return shell;
    }

    /**
     *
     * @return
     */
    private String getCurrentOS() {
        String os = "Linux";
        String osName = System.getProperties().getProperty("os.name");
        if(osName!=null && osName.indexOf("Windows")>=0) {
            os = "Windows";
        }
        return os;
    }

    public static void main(String[] args) {
        Runtime rt = Runtime.getRuntime();
        try {
            Process proc = rt.exec("cmd /c mkdir chengxj");
            InputStream stdin = proc.getInputStream();
            InputStreamReader isr = new InputStreamReader(stdin);
            BufferedReader br = new BufferedReader(isr);
            String line = null;
            System.out.println("<output></output>");
            while ((line = br.readLine()) != null)
                System.out.println(line);
            System.out.println("");
            int exitVal = proc.waitFor();
            System.out.println("Process exitValue: " + exitVal);
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("===========os.name:"+System.getProperties().getProperty("os.name"));
        System.out.println("===========file.separator:"+System.getProperties().getProperty("file.separator"));
    }
}
