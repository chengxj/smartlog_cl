package com.cl.web;

import javax.servlet.http.HttpServletRequest;
import com.cl.auth.AuthException;
import com.cl.auth.AuthService;
import com.cl.auth.LoginVO;
import org.apache.shiro.SecurityUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import com.cl.entity.common.User;

@Controller
public class WebController {

	@Autowired
	private AuthService authService;

	@RequestMapping(value = "/example")
	public String activities(Model model) {
		return "statement";
	}
	
	@RequestMapping(value = "/example/danji")
	public String danji(Model model) {
		return "danji";
	}
	
	@RequestMapping(value = "/example/finish")
	public String finish(Model model) {
		return "finish";
	}
	
	@RequestMapping(value = "/example/host")
	public String host(Model model) {
		return "host";
	}

	@RequestMapping(value = "/example/jiqun")
	public String jijun(Model model) {
		return "jiqun";
	}
	
	@RequestMapping(value = "/example/in")
	public String in(Model model) {
		return "in";
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
		return "error";
	}

}