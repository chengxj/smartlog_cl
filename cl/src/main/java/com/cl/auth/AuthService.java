package com.cl.auth;

/**
 * Created by chengxj on 2015/10/19.
 */
public interface AuthService {

    /**
     *
     * @param vo
     */
    public void login(LoginVO vo);

    /**
     *
     */
    public void logout();

}
