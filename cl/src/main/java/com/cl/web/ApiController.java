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

	// @RequestMapping(value = "/api/search_activities", method =
	// RequestMethod.POST)
	// @ResponseBody
	// public ActivitiesDTO searchActivities(@RequestBody ActivitiesRequest
	// request) {
	// return commonService.searchActivities(request);
	// }
	//
	// @RequestMapping(value = "/api/get_registration_detail", method =
	// RequestMethod.POST)
	// @ResponseBody
	// public RegistrationDetailDTO getRegistrationDetail(@RequestBody
	// RegistrationDetailRequest request) {
	// return commonService.getRegistrationDetail(request);
	// }
	//
	// @RequestMapping(value = "/api/add_registration", method =
	// RequestMethod.POST)
	// @ResponseBody
	// public RegistrationDTO addRegistration(@RequestBody RegistrationRequest
	// request) {
	// return commonService.addRegistration(request);
	// }
	//
	// @RequestMapping(value = "/api/edit_registration", method =
	// RequestMethod.POST)
	// @ResponseBody
	// public RegistrationDTO editRegistration(@RequestBody RegistrationRequest
	// request) {
	// return commonService.editRegistration(request);
	// }
	//
	// @RequestMapping(value = "/api/delete_registration", method =
	// RequestMethod.POST)
	// @ResponseBody
	// public void deleteRegistration(@RequestBody RegistrationRequest request)
	// {
	// commonService.deleteRegistration(request);
	// }

	@RequestMapping(value = "/api/valid_single_server", method = RequestMethod.POST)
	@ResponseBody
	public SingleServerDTO validSingleServer(@RequestBody SingleServerRequest request) {
		return commonService.validSingleServer(request);
	}

	@RequestMapping(value = "/api/valid_single_server_components", method = RequestMethod.POST)
	@ResponseBody
	public SingleServerWarnDTO validSingleServerComponents(@RequestBody SingleServerComponentsRequest request) {
		return commonService.validSingleServerComponents(request);
	}

}