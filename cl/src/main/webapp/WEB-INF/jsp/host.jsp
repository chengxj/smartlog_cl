<!DOCTYPE html>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %><html xmlns="http://www.w3.org/1999/xhtml">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>首页</title>
<link href="/resources/css/style.css" rel="stylesheet" type="text/css" />
<link href="/resources/css/host.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <div class="logo"><div class="logo_sub1">
	    	<img class="logo_sub2" src="/resources/images/logo.png" />
        </div></div>
    <div class="head">
        <div class="nav">
       
            <div class="nav1_sub1"><span>1 用户名</span></div>
            <div class="nav1"><span>2 集群管理</span></div>
            <div class="nav1"><span>3 告警内容</span></div>
            <div class="nav2"><span>4 安装</span></div>
            <div class="nav_bg"></div>
            
        </div>
    </div>
    <div class="main">
        <div class="mount">主机IP</div>
        <div class="schedule"> </div>
        <div class="classify">

        </div>
        <div class="host">
            <div class="center_1">
            	<div class="input_move">
                	<div class="input_font_blue">IP</div>
                	<input type="text" class="input_yuanjiao box-shadow-2" value="例如:127.0.0.1" />
                </div>
                
                
            </div>
        </div>
        <div class="note">请填写一台安装了zookeeper 的主机IP地址</div>
        <div class="next_button">
            <div class="finish_1"><div class="finish_2">下一步</div></div>
        </div>
    </div>
    <div  id="footer"><div class="fanxiang">Copyright 2015-2020  神州泰岳 版权所有</div></div>
   

</body>
</html>
