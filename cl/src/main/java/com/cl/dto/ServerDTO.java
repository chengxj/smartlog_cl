package com.cl.dto;

import java.util.List;
import com.cl.dto.common.BaseDTO;
import com.cl.entity.Component;
import com.cl.entity.Server;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;

@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class ServerDTO extends BaseDTO {
	
	public Server server;
	public List<Component> components;

}
