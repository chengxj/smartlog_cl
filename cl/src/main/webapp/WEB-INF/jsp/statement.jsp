<!DOCTYPE html>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html xmlns="http://www.w3.org/1999/xhtml"  ng-app="app">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>首页</title>
<link href="/resources/css/style.css" rel="stylesheet" type="text/css" />
<link href="/resources/css/statement.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="/resources/js/angular.min.js"></script>
</head>
<body ng-controller="controller">
    <div class="logo"><div class="logo_sub1">
	    	<img class="logo_sub2" src="/resources/images/logo.png" />
        </div></div>
    <div class="head">
        <div class="nav">
       
            <div class="nav1_sub1"></div>
            <div class="nav1"></div>
            <div class="nav1"></div>
            <div class="nav1"></div>
            <div class="nav_bg_line"></div>
            <div class="nav_bg"></div>
            
        </div>
    </div>
    <div class="main">
        <div class="mount">声明</div>
        <div class="schedule">
            
            
        </div>
        <div class="classify">
            
            
        </div>
        <div class="statement">
            <div class="center_1">
                <p class="title">版权声明</p>
	            <p class="text_hui">1、本网站所有内容，凡注明"来源：233网校"的所有文字、图片、页面的版式、和音视频资料，版权均属233网校所有，任何媒体、网站或个人未经本网协议授权不得转载、链接、转贴或以其他方式复制发布、发表。已经本网协议授权的媒体、网站，在下载使用时必须注明"稿件来源 ——233网校网 "，违者本网将依法追究责任。</p>
                <p class="text_hui"> 2、本网站（233网校）授权您使用的网络课程等内容，仅限您个人使用不得用于任何商业用途。对于原始内容中所注明的版权及所有权声明，您必须在其副本中予以保留，您不得以任何方式修改、复制、公开展示、公布或分发这些材料或以其他方式把它们用于任何公开或商业目的，禁止以任何目的或形式把这些材料用于其他任何网站或网络计算机环境。 </p>
                <p class="text_hui">3、转载或引用本网版权所有之内容须注明“转自（或引自）233网校”字样，并标明本网网址www.233.com。</p>
                <p class="text_hui">4、对于不当转载或引用本网内容而引起的民事纷争、行政处理或其他损失，本网不承担责任。 5、对不遵守本声明或其他违法、恶意使用本网内容者，本网保留追究其法律责任的权利。</p>
               
                
            </div>
        </div>
        <div class="statement_next">
            <div class="radio"><input ng-model="checkType" type="radio" value="agree" />同意以上说明</div>
            <div class="radio"><input ng-model="checkType" type="radio" value="disagree" />不同意以上说明</div>
            <div class="title_box">
                    
                    <div class="title_buttom">
        
                    	<div class="buttom_type" ng-click="next()"><div class="buttom_type_text">下一步</div></div>
                    </div>
               		</div>
            </div>
    </div>
    <div  id="footer"><div class="fanxiang">Copyright 2015-2020  神州泰岳 版权所有</div></div>
<script>
angular.module('app', [])
.controller('controller', ['$scope', 
	function($scope) {

		$scope.next = function() {
			if ($scope.checkType == "agree") {
				window.location.href = '/example/index';
			};
		};
		
	}
]);
</script>
</body>
</html>
