package com.cl.entity;

import com.cl.entity.common.DBObject;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.io.Serializable;

/**
 * Created by chengxj on 2015/10/22.
 */
@Entity
public class Component implements Serializable, DBObject {

    @Id
    @GeneratedValue
    private Long id;
    @Column(name = "server_id")
    private Long serverId;
    @Column(name = "type")
    private String type;
    @Column(name = "install_dir")
    private String installDir;
    @Column(name = "data_dir")
    private String dataDir;
    @Column(name = "log_dir")
    private String logDir;
    @Column(name = "description")
    private String description;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getServerId() {
        return serverId;
    }

    public void setServerId(Long serverId) {
        this.serverId = serverId;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getInstallDir() {
        return installDir;
    }

    public void setInstallDir(String installDir) {
        this.installDir = installDir;
    }

    public String getDataDir() {
        return dataDir;
    }

    public void setDataDir(String dataDir) {
        this.dataDir = dataDir;
    }

    public String getLogDir() {
        return logDir;
    }

    public void setLogDir(String logDir) {
        this.logDir = logDir;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

}
