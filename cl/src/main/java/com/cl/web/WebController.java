package com.cl.web;

import javax.servlet.http.HttpServletRequest;
import com.cl.auth.AuthException;
import com.cl.auth.AuthService;
import com.cl.auth.LoginVO;
import org.apache.shiro.SecurityUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import com.cl.entity.common.User;

@Controller
public class WebController {

	@Autowired
	private AuthService authService;

	@RequestMapping(value = "/{url}")
	public String index(@PathVariable String url, Model model) {
		if(SecurityUtils.getSubject().isAuthenticated()){
			return url;
		}
		return null;
	}

	@RequestMapping(value = "/example")
	public String activities(Model model) {
		return "demo1";
	}
	
	@RequestMapping(value = "/example/demo4/{id}")
	public String demo4test(Model model, @PathVariable Long id) {
		model.addAttribute("id", id);
		return "demo4";
	}

	@RequestMapping(value = "/example/demo{url}")
	public String demotest(Model model, @PathVariable String url) {
		return "demo" + url;
	}

	@RequestMapping(value = "/example/login", method = RequestMethod.GET)
	 public String login(Model model, HttpServletRequest request) throws Exception {
		if(SecurityUtils.getSubject().isAuthenticated()){
			return "redirect:/example";
		}
		return "login";
	}

	@RequestMapping(value = "/example/login", method = RequestMethod.POST)
	public String login(User loginUser, Model model, HttpServletRequest request) {
		LoginVO vo = new LoginVO();
		vo.name = loginUser.getUserid();
		vo.pwd = loginUser.getPassword();
		vo.rememberme = request.getParameter("rememberme");
		try {
			authService.login(vo);
			return "redirect:/example";
		} catch (AuthException e) {
			model.addAttribute("message", "用户名或密码不正确");
			return "login";
		}
	}

	@RequestMapping(value = "/example/logout")
	public String logout(Model model) {
		authService.logout();
		return "redirect:/example";
	}

	@RequestMapping(value = "/example/error")
	public String error(Model model) {
		return "error-404";
	}

}