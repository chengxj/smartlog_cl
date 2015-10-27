<!DOCTYPE html>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %><html xmlns="http://www.w3.org/1999/xhtml">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>首页</title>
<link href="/resources/css/shouye.css" rel="stylesheet" type="text/css" />
<link href="/resources/css/login.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <div class="logo"><div class="logo_sub1">
	    	<img class="logo_sub2" src="/resources/images/logo.png" />
        </div></div>
    <div class="head">
        <div class="nav">
            <div class="nav2">1 用户名</div>
            <div class="nav1">2 集群管理</div>
            <div class="nav1">3 告警内容</div>
            <div class="nav1">4 安装</div>
        </div>
    </div>
    <div class="main">
        <div class="mount">单机-安装</div>
        <div class="schedule"> </div>
        <div class="classify">

        </div>
        <div class="login">
            <div class="center_1">
            	<div class="input_move">
                	<div class="input_font_blue">IP</div>
                	<input class="input_yuanjiao box-shadow-2" type="text" />
                </div>
                <div class="input_move">
                	<div class="input_font_blue">用户名</div>
                	<input class="input_yuanjiao input_radius1" type="text" />
                </div>
                <div class="input_move">
                	<div class="input_font_blue">密码</div>
                	<input class="input_yuanjiao input_radius1" type="text" />
                </div>
            </div>
        </div>
        <div class="note">请填写主机信息后点击下一步，如未安装将跳转到安装页，所以安装页，所以安装则自动跳转到管理员</div>
        <div class="next_button">
            <div class="finish_1"><div class="finish_2">下一步</div></div>
        </div>
    </div>
    <div  id="footer"><div class="fanxiang">Copyright 2015-2020  神州泰岳 版权所有</div></div>
   

</body>
</html>
