package com.cl.service;

public class BaseException extends RuntimeException {

	private static final long serialVersionUID = 1L;

	public BaseException() {

	}

	public BaseException(String s) {
		super(s);
	}

	public BaseException(String s, Throwable throwable) {
		super(s, throwable);
	}

	public BaseException(Throwable throwable) {
		super(throwable);
	}
	
}