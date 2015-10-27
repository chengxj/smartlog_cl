<!DOCTYPE html>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %><html xmlns="http://www.w3.org/1999/xhtml">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>首页</title>
<link href="/resources/css/style.css" rel="stylesheet" type="text/css" />
<link href="/resources/css/cluster.css" rel="stylesheet" type="text/css" />
</head>

<body>

	
    <div class="logo"><div class="logo_sub1">
	    	<img class="logo_sub2" src="/resources/images/logo.png" />
        </div></div>
    <div class="head">
        <div class="nav">
            <div class="nav2">1 创建集群</div>
            <div class="nav1">2 集群管理</div>
            <div class="nav1">3 告警内容</div>
            <div class="nav1">4 安装</div>
        </div>
    </div>
    <div class="main">
        <div class="mount">创建集群</div>
        <div class="schedule"> </div>
        <div class="classify">

        </div>
        <div class="jiqun">
            <div class="center_1">
            	
                <div class="kuang_all">
	                <div class="jiqun_newadd box-shadow-blue">新建集群</div>
                    <div class="font_note">
                    	<p>请填写主机信息后点击下一步</p>
                        <p>包括配置说明，以及要安装的组件、建议分配情况</p>
                    </div>
                </div>
                
                <div class="kuang_all">
	                <div class="jiqun_newadd box-shadow-hui">管理/扩展</div>
                    <div class="font_note1">
                    	<p>请填写主机信息后点击下一步</p>
                        <p>包括配置说明，以及要安装的组件、建议分配情况</p>
                    </div>
                </div>
                
                <div class="kuang_all">
	                <div class="jiqun_newadd box-shadow-hui">单机 > 集群</div>
                    <div class="font_note2">
                    	<p>请填写主机信息后点击下一步</p>
                        <p>包括配置说明，以及要安装的组件、建议分配情况</p>
                    </div>
                </div>
                
               
                
            </div>
        </div>
        
        <div class="next_button">
            <div onclick="javascript:window.location.href='#'" class="finish_1"><div class="finish_2">下一步</div></div>
        </div>
    </div>
    <div  id="footer"><div class="fanxiang">Copyright 2015-2020  神州泰岳 版权所有</div></div>
   

</body>
</html>
