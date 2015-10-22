package com.cl.web.common;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.cl.auth.AuthException;
import com.cl.dto.common.ErrorDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.DefaultHandlerExceptionResolver;
import org.springframework.web.servlet.view.json.MappingJacksonJsonView;

import java.util.HashMap;
import java.util.Map;

@Controller
public class WebHandlerExceptionResolver extends DefaultHandlerExceptionResolver {
	
	  protected Logger log = LoggerFactory.getLogger(this.getClass());
	  
	  @Override
	  public ModelAndView resolveException(HttpServletRequest request, HttpServletResponse response, Object handler, Exception e) {
		  Map model = new HashMap();
		  if (e instanceof Exception) {
			  if(e instanceof AuthException) {
				  model.put("error", new ErrorDTO("用户名或密码不正确 : 请重新输入", 1));
				  e.printStackTrace();
				  response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
			  } else {
				  model.put("error", new ErrorDTO(e.getMessage() + " : " + e.getCause(), 1));
				  e.printStackTrace();
				  response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
			  }
		  }
		  return new ModelAndView(new MappingJacksonJsonView(), model);
	  }

}
