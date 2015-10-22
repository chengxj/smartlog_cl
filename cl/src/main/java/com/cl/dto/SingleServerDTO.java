package com.cl.dto;

import com.cl.dto.common.BaseDTO;
import com.cl.entity.Server;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;

/**
 * Created by chengxj on 2015/10/22.
 */
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class SingleServerDTO extends BaseDTO {

    public Server server;

}
