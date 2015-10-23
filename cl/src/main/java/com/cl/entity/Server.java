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
public class Server implements Serializable, DBObject {

    @Id
    @GeneratedValue
    private Long id;
    @Column(name = "team")
    private Long team;
    @Column(name = "type")
    private String type;
    @Column(name = "cluster_name")
    private String clusterName;
    @Column(name = "role")
    private String role;
    @Column(name = "ip")
    private String ip;
    @Column(name = "hostname")
    private String hostname;
    @Column(name = "username")
    private String username;
    @Column(name = "password")
    private String password;
    @Column(name = "description")
    private String description;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }


    public Long getTeam() {
        return team;
    }

    public void setTeam(Long team) {
        this.team = team;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


    public String getClusterName() {
        return clusterName;
    }

    public void setClusterName(String clusterName) {
        this.clusterName = clusterName;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }


    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }


    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }

    public String getUsername() {
        return hostname;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

}