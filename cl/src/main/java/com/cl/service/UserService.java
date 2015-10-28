package com.cl.service;

import com.cl.entity.common.User;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.session.Session;
import org.springframework.stereotype.Service;

/**
 * Created by chengxj on 2015/10/23.
 */
@Service
public class UserService {

	/**
	 * 
	 * @return
	 */
    public User getCurrentLoginUser() {
        Session session = SecurityUtils.getSubject().getSession();
        return (User)session.getAttribute("LoginUser");
    }
    
    /**
     * 
     * @return
     */
    public Long getCurrentUserTeam() {
    	return 1l;
//        User currentUser = getCurrentLoginUser();
//        if (currentUser!=null && currentUser.getTeam()!=null) {
//            return currentUser.getTeam().getId();
//        } else {
//        	return null;
//        }
    }
    
}