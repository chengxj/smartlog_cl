<!DOCTYPE html>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html xmlns="http://www.w3.org/1999/xhtml" ng-app="app">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>首页</title>
<link href="/resources/css/style.css" rel="stylesheet" type="text/css" />
<link href="/resources/css/component_selection.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="/resources/js/angular.min.js"></script>
<script type="text/javascript" src="/resources/js/angular-resource.min.js"></script>
<script type="text/javascript" src="/resources/js/angular-common-0.2.js"></script>
</head>
<body ng-controller="controller">
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
        <div class="mount">组件选择</div>
        <div class="schedule"> </div>
        <div class="classify">

        </div>
        <div class="component_selection">
            <div class="center_1">
            		<div class="title_box">
                    <div class="title_ip">
                        <p>IP:<input class="input_hide" value="{{server.ip}}" ng-readonly="true" /></p>
                        <p>HOSTNAME:<input class="input_hide" value="{{server.hostname}}" ng-readonly="true" /></p>
                        <p>PASSWORD:<input class="input_hide" type="password" value="{{server.password}}" ng-readonly="true" /></p>
                    </div>
               		</div>
               		
                    <div class="title_box">
                            <div class="input_move box-shadow-1">
                                <div class="ico_add_blue">ZOOKEEPER</div>
                                <p>端口:<input class="input_hide_hui"/></p>
                                <p>安装路径<input class="input_hide_hui"/></p>
                                <p>dataDir<input class="input_hide_hui"/></p>
                                <p>logDir<input class="input_hide_hui"/></p>
                            </div>
                            <div class="input_move box-shadow-1">
                                <div class="ico_add_blue">KAFKA</div>
                                <p>端口:<input class="input_hide_hui"/></p>
                                <p>安装路径<input class="input_hide_hui"/></p>
                                <p>dataDir<input class="input_hide_hui"/></p>
                                <p>logDir<input class="input_hide_hui"/></p>                                
                            </div>                       
                            <div class="input_move box-shadow-1">
                                 <div class="ico_add_blue">FLUME</div>
                                <p>端口:<input class="input_hide_hui"/></p>
                                <p>安装路径<input class="input_hide_hui"/></p>
                                <p>dataDir<input class="input_hide_hui"/></p>
                                <p>logDir<input class="input_hide_hui"/></p>
                            </div>
                            <div class="input_move box-shadow-1">
                                 <div class="ico_add_blue">STORM</div>
                                <p>端口:<input class="input_hide_hui"/></p>
                                <p>安装路径<input class="input_hide_hui"/></p>
                                <p>dataDir<input class="input_hide_hui"/></p>
                                <p>logDir<input class="input_hide_hui"/></p>
                            </div>                            
                   </div>
                   
                   <div class="title_box">
                            <div class="input_move box-shadow-1">
                                <div class="ico_jian_blue">ELASTICSEARCH</div>
                                <p>端口:<input class="input_hide_hui"/></p>
                                <p>安装路径<input class="input_hide_hui"/></p>
                                <p>dataDir<input class="input_hide_hui"/></p>
                                <p>logDir<input class="input_hide_hui"/></p>                                
                            </div>
                            <div class="input_move box-shadow-1">
                                <div class="ico_jian_blue">FRONTEND</div>
                                <p>端口:<input class="input_hide_hui"/></p>
                                <p>安装路径<input class="input_hide_hui"/></p>
                                <p>dataDir<input class="input_hide_hui"/></p>
                                <p>logDir<input class="input_hide_hui"/></p>                                
                            </div>                       
                            <div class="input_move box-shadow-1">
                                 <div class="ico_add_blue">WEB</div>
                                <p>端口:<input class="input_hide_hui"/></p>
                                <p>安装路径<input class="input_hide_hui"/></p>
                                <p>dataDir<input class="input_hide_hui"/></p>
                                <p>logDir<input class="input_hide_hui"/></p>
                            </div>
                            <div class="input_move box-shadow-1">
                                 <div class="ico_add_blue">DATABASE</div>
                                <p>端口:<input class="input_hide_hui"/></p>
                                <p>安装路径<input class="input_hide_hui"/></p>
                                <p>dataDir<input class="input_hide_hui"/></p>
                                <p>logDir<input class="input_hide_hui"/></p>
                            </div>                            
                   </div>
               	   
            </div>
            <div class="note">请填写主机信息后点击下一步，如未安装将跳转到安装页，所以安装页，所以安装则自动跳转到管理员</div>
            <div class="title_box">
                    
                    <div class="title_buttom">
        
                    	<div class="buttom_type "><div class="buttom_type_text">下一步</div></div>
                    </div>
               		</div>
        </div>
    </div>
    <div  id="footer"><div class="fanxiang">Copyright 2015-2020  神州泰岳 版权所有</div></div>
<script>
angular.module('app', ['common'])
.controller('controller', ['$scope', 'commonDao',
    function($scope, commonDao) {
	
		$scope.id = '${id}';
	
		$scope.getServer = function() {
			commonDao.getSingleServer().save({'server':{'id':$scope.id}}).$promise.then(function(data) {			
				if (data.success) {
					$scope.server = data.server;				
				}			
			});	
		};
		
		$scope.getServer();
		
		$scope.validSingleServerComponents = function() {
			
		};
	}
]);
</script>  
</body>
</html>
