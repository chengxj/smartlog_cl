package com.cl.auth.pwd;

import com.cl.dao.SearchDao;
import com.cl.entity.common.Role;
import com.cl.entity.common.User;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authc.SimpleAuthenticationInfo;
import org.apache.shiro.authc.UnknownAccountException;
import org.apache.shiro.authz.AuthorizationException;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.session.Session;
import org.apache.shiro.subject.PrincipalCollection;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.ArrayList;
import java.util.List;

public class UsernamePasswordRealm extends AuthorizingRealm {

	protected Logger log = LoggerFactory.getLogger(this.getClass());

	@Autowired
	private SearchDao searchDao;

	/**
	 * 授权
	 */
	@Override
	protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principals) {
		if (principals == null) {
			throw new AuthorizationException("PrincipalCollection参数不能为空。");
		}
		String loginName = (String) getAvailablePrincipal(principals);
		List<String> roles = new ArrayList<String>();
		User user = searchDao.getUserByUid(loginName);
		if (user != null && user.getUserid().equals(loginName)) {
			if (user.getRoles() != null && user.getRoles().size() > 0) {
				for (Role role : user.getRoles()) {
					roles.add(role.getRole());
				}
			}
		} else {
			throw new AuthorizationException();
		}
		SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();
		info.addRoles(roles);
		return info;
	}

	/**
	 * 认证
	 */
	@Override
	protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token) {
		String loginName = (String) token.getPrincipal();
		User user = searchDao.getUserByUid(loginName);
		if (user == null)
			throw new UnknownAccountException();
		// 设置SESSION
        Session session = SecurityUtils.getSubject().getSession();
        session.setAttribute("LoginUser", user);// 登录用户信息
		SimpleAuthenticationInfo authInfo = new SimpleAuthenticationInfo(user.getUserid(), user.getPassword(), getName());
		return authInfo;
	}

}
