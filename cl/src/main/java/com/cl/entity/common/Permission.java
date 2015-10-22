package com.cl.entity.common;

import java.io.Serializable;
import java.util.Set;

import javax.persistence.*;

import org.hibernate.annotations.BatchSize;


/**
 * The persistent class for the permission database table.
 * 
 */
@Entity
@Table(name="permission")
public class Permission implements Serializable {
	private static final long serialVersionUID = 1L;

	@Id
	@GeneratedValue
	private long id;
	private String permission;
	private String description;
	private boolean available;

	@ManyToMany(fetch = FetchType.EAGER)
	@JoinTable(name = "role_permission",
	joinColumns = @JoinColumn(name="permission_id", insertable=false, updatable=false),
	inverseJoinColumns = @JoinColumn(name = "role_id", insertable=false, updatable=false))
	@BatchSize(size = 10)
	private Set<Role> roles;
	
	public Permission() {
	}

	public long getId() {
		return this.id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public boolean getAvailable() {
		return this.available;
	}

	public void setAvailable(boolean available) {
		this.available = available;
	}

	public String getDescription() {
		return this.description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getPermission() {
		return this.permission;
	}

	public void setPermission(String permission) {
		this.permission = permission;
	}

	/**
	 * @return the roles
	 */
	public Set<Role> getRoles() {
		return roles;
	}

	/**
	 * @param roles the roles to set
	 */
	public void setRoles(Set<Role> roles) {
		this.roles = roles;
	}

}