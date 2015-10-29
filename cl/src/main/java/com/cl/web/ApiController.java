package com.cl.web;

import com.cl.dto.SingleServerDTO;
import com.cl.dto.SingleServerWarnDTO;
import com.cl.request.SingleServerComponentsRequest;
import com.cl.request.SingleServerRequest;
import com.cl.service.FileService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import com.cl.service.CommonService;

@Controller
public class ApiController {

	@Autowired
	private CommonService commonService;

	@Autowired
	private FileService fileService;

	@RequestMapping(value = "/api/valid_single_server", method = RequestMethod.POST)
	@ResponseBody
	public SingleServerDTO validSingleServer(@RequestBody SingleServerRequest request) {
		return commonService.validSingleServer(request);
	}
	
	@RequestMapping(value = "/api/get_single_server", method = RequestMethod.POST)
	@ResponseBody
	public SingleServerDTO getSingleServer(@RequestBody SingleServerRequest request) {
		return commonService.getSingleServer(request);
	}

	@RequestMapping(value = "/api/valid_single_server_components", method = RequestMethod.POST)
	@ResponseBody
	public SingleServerWarnDTO validSingleServerComponents(@RequestBody SingleServerComponentsRequest request) {
		return commonService.validSingleServerComponents(request);
	}

}