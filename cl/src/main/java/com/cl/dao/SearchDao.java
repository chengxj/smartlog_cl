package com.cl.dao;

import javax.persistence.EntityManager;
import javax.persistence.NoResultException;
import javax.persistence.PersistenceContext;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;
import com.cl.entity.Server;
import com.cl.entity.common.User;

@Repository
@Transactional(noRollbackFor = { NoResultException.class })
public class SearchDao {

	@PersistenceContext(unitName = "entityManagerFactory")
	private EntityManager entityManager;

	private static int pageSize = 10;
	
	/**
	 * 
	 * @param obj
	 * @return
	 */
	public Server findExistServer(Server obj) {
		String hql = "from Server where type=:type and ip = :ip and username = :username and password = :password";
		try {
			return entityManager.createQuery(hql, Server.class)
					.setParameter("type", obj.getType())
					.setParameter("ip", obj.getIp())
					.setParameter("username", obj.getUsername())
					.setParameter("password", obj.getPassword())			 
					.getSingleResult();
		} catch (NoResultException e) {
			return null;
		} catch (Exception e) {
			return null;
		}
	}
	
	/**
	 * 
	 * @param obj
	 * @return
	 */
	public Server getServer(Server obj) {
		String hql = "from Server where id = :id";
		try {
			return entityManager.createQuery(hql, Server.class)
					.setParameter("id", obj.getId())
					.getSingleResult();
		} catch (NoResultException e) {
			return null;
		} 
	}

	/**
	 *
	 * @param userid
	 * @return
	 */
	public User getUserByUid(String userid) {
		 String hql = "from User where userid = :userid";
		 return entityManager.createQuery(hql, User.class)
				 .setParameter("userid", userid)
				 .getSingleResult();
	}

}