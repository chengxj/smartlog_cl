package com.cl.entity.common;

import java.io.Serializable;
import java.util.Set;
import javax.persistence.*;
import org.hibernate.annotations.BatchSize;

/**
 * The persistent class for the role database table.
 * 
 */
@Entity
@Table(name="role")
public class Role implements Serializable {
	private static final long serialVersionUID = 1L;

	@Id
	@GeneratedValue
	private long id;
	private String role;
	private String description;
	private boolean available;
	
	@ManyToMany(fetch = FetchType.EAGER)
	@JoinTable(name = "user_role",
	joinColumns = @JoinColumn(name="role_id", insertable=false, updatable=false),
	inverseJoinColumns = @JoinColumn(name = "user_id", insertable=false, updatable=false))
	@BatchSize(size = 10)
	private Set<User> users;
	
	@ManyToMany(fetch = FetchType.EAGER)
	@JoinTable(name = "role_permission",
	joinColumns = @JoinColumn(name="role_id", insertable=false, updatable=false),
	inverseJoinColumns = @JoinColumn(name = "permission_id", insertable=false, updatable=false))
	@BatchSize(size = 10)
	private Set<Permission> permissions;

	public Role() {
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

	public String getRole() {
		return this.role;
	}

	public void setRole(String role) {
		this.role = role;
	}

	/**
	 * @return the users
	 */
	public Set<User> getUsers() {
		return users;
	}

	/**
	 * @param users the users to set
	 */
	public void setUsers(Set<User> users) {
		this.users = users;
	}

	/**
	 * @return the permissions
	 */
	public Set<Permission> getPermissions() {
		return permissions;
	}

	/**
	 * @param permissions the permissions to set
	 */
	public void setPermissions(Set<Permission> permissions) {
		this.permissions = permissions;
	}

}