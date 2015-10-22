package com.cl.dto.common;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class ErrorDTO {
	
	  private String message;
	  private Integer level;
	 
	  public ErrorDTO() {
	  }
	  
	  public ErrorDTO(String message, Integer level) {
	    this.message = message;
	    this.level = level;
	  }

	  /**
	   * @return the message
	   */
	  public String getMessage() {
	    return message;
	  }

	  /**
	   * @return the level
	   */
	  public Integer getLevel() {
	    return level;
	  }

}
