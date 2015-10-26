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

//	private static int pageSize = 10;
	
	/**
	 * 
	 * @param obj
	 * @return
	 */
	public Server findExistServer(Server obj) {
		String hql = "from Server where type=:type and ip = :ip and hostname = :hostname and username = :username and password = :password";
		try {
//			List<Server> list = entityManager.createQuery(hql, Server.class)
//					.setParameter("type", obj.getType())
//					.setParameter("ip", obj.getIp())
//					.setParameter("hostname", obj.getHostname())
//					.setParameter("username", obj.getUsername())
//					.setParameter("password", obj.getPassword())			 
//					.getResultList();
//			return list.get(0);
			return entityManager.createQuery(hql, Server.class)
					.setParameter("type", obj.getType())
					.setParameter("ip", obj.getIp())
					.setParameter("hostname", obj.getHostname())
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
	 * @param userid
	 * @return
	 */
	public User getUserByUid(String userid) {
		 String hql = "from User where userid = :userid";
		 return entityManager.createQuery(hql, User.class)
				 .setParameter("userid", userid)
				 .getSingleResult();
	}

//	/**
//	 *
//	 * @param activities_id
//	 * @return
//	 */
//	public List<Registration> getRegistrations(long activities_id) {
//		String hql = "from Registration where activities_id = :activities_id";
//		return entityManager.createQuery(hql, Registration.class).setParameter("activities_id", activities_id)
//				.getResultList();
//	}
//
//	/**
//	 *
//	 * @param uuid
//	 * @param activities_id
//	 * @return
//	 */
//	public Registration getRegistrationById(long uuid, long activities_id) {
//		 String hql = "from Registration where id = :uuid and activities_id = :activities_id";
//		 return entityManager.createQuery(hql, Registration.class)
//				 .setParameter("uuid", uuid)
//				 .setParameter("activities_id", activities_id)
//				 .getSingleResult();
//	}
//
//	/**
//	 *
//	 * @param searchTerm
//	 * @param index
//	 * @return
//	 */
//	public List<Activities> searchActivities(String searchTerm, int index) {
//		String hql;
//		if (searchTerm == null || searchTerm.isEmpty()) {
//			hql = "from Activities";
//		} else {
//			hql = "From Activities where title like '%" + searchTerm + "%'";
//		}
//		return entityManager.createQuery(hql, Activities.class)
//				.setFirstResult(index)
//				.setMaxResults(pageSize)
//				.getResultList();
//	}
//
//	/**
//	 *
//	 * @param searchTerm
//	 * @return
//	 */
//	public int getSearchActivitiesCount(String searchTerm) {
//		try {
//			String hql;
//			if (searchTerm == null || searchTerm.isEmpty()) {
//				hql = "select count(*) from Activities";
//			} else {
//				hql = "select count(*) From Activities where title like '%" + searchTerm + "%'";
//			}
//			return entityManager.createQuery(hql, Long.class)
//					.getSingleResult().intValue();
//		} catch (NoResultException e) {
//			return 0;
//		}
//	}

}