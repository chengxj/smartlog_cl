package com.cl.auth;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.crypto.hash.Md5Hash;
import org.apache.shiro.subject.Subject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

/**
 * Created by chengxj on 2015/10/19.
 */
@Service
public class AuthServiceImpl implements AuthService {

    private static final Logger LOGGER = LoggerFactory.getLogger(AuthServiceImpl.class);

    /**
     *
     * @param vo
     */
    public void login(LoginVO vo) {
        String passWord = new Md5Hash(vo.pwd).toString();
        UsernamePasswordToken token = new UsernamePasswordToken(vo.name, passWord);
        if (null!=vo.rememberme && !"".equals(vo.rememberme)) {
            token.setRememberMe(true);
        } else {
            token.setRememberMe(false);
        }
        try {
            Subject user = SecurityUtils.getSubject();
            user.login(token);
            LOGGER.debug("user login : {}", vo.name);
        } catch (UnknownAccountException e) {
            LOGGER.info(vo.name + "：未知用户");
            throw new AuthException("未知用户", e);
        } catch (IncorrectCredentialsException e) {
            LOGGER.info(vo.name + "：密码不正确！");
            throw new AuthException("密码不正确！", e);
        } catch (AuthenticationException e) {
            LOGGER.info(vo.name + "：用户名或密码不正确！");
            throw new AuthException("用户名或密码不正确！", e);
        } catch (Exception e) {
            LOGGER.info(vo.name + "：用户名或密码不正确！");
            throw new AuthException("用户或密码不正确！", e);
        }
    }

    /**
     *
     */
    public void logout() {
        Subject subject = SecurityUtils.getSubject();
        if (subject.isAuthenticated()) {
            subject.logout(); // session 会销毁，在SessionListener监听session销毁，清理权限缓存
        }
    }

}
