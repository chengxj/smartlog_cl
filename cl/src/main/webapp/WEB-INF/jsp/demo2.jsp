<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="ngApp" value="app"/>
<c:set var="ngController" value="appCtrl"/>
<%@include file="include/header.jspf" %>

		<!-- /section:basics/navbar.layout -->
		<div class="main-container" id="main-container">
			<script type="text/javascript">
				try{ace.settings.check('main-container' , 'fixed')}catch(e){}
			</script>

			<!-- #section:basics/sidebar -->
			<div id="sidebar" class="sidebar responsive">
				<script type="text/javascript">
					try{ace.settings.check('sidebar' , 'fixed')}catch(e){}
				</script>

				<div class="sidebar-shortcuts" id="sidebar-shortcuts">
					<div class="sidebar-shortcuts-large" id="sidebar-shortcuts-large">
						<button class="btn btn-success">
							<i class="ace-icon fa fa-signal"></i>
						</button>

						<button class="btn btn-info">
							<i class="ace-icon fa fa-pencil"></i>
						</button>

						<!-- #section:basics/sidebar.layout.shortcuts -->
						<button class="btn btn-warning">
							<i class="ace-icon fa fa-users"></i>
						</button>

						<button class="btn btn-danger">
							<i class="ace-icon fa fa-cogs"></i>
						</button>

						<!-- /section:basics/sidebar.layout.shortcuts -->
					</div>

					<div class="sidebar-shortcuts-mini" id="sidebar-shortcuts-mini">
						<span class="btn btn-success"></span>

						<span class="btn btn-info"></span>

						<span class="btn btn-warning"></span>

						<span class="btn btn-danger"></span>
					</div>
				</div><!-- /.sidebar-shortcuts -->
				
				<%@include file="include/menu.jspf" %>

				<!-- /section:basics/sidebar.layout.minimize -->
				<script type="text/javascript">
					try{ace.settings.check('sidebar' , 'collapsed')}catch(e){}
				</script>
			</div>

			<!-- /section:basics/sidebar -->
			<div class="main-content">
				<!-- #section:basics/content.breadcrumbs -->
				<div class="breadcrumbs" id="breadcrumbs">
					<script type="text/javascript">
						try{ace.settings.check('breadcrumbs' , 'fixed')}catch(e){}
					</script>

					<ul class="breadcrumb">
						<li>
							<i class="ace-icon fa fa-home home-icon"></i>
							<a href="#">Home</a>
						</li>

						<li>
							<a href="#">Other Pages</a>
						</li>
						
						<li class="active">Blank Page</li>
						
					</ul><!-- /.breadcrumb -->

					<!-- #section:basics/content.searchbox -->
					<div class="nav-search" style="top:5px;">
						<button class="btn btn-custom btn-primary" ng-click="next('/example/demo4')"> 下一步 </button>
						<button class="btn btn-custom btn-primary" ng-click="go('/example/demo1')"> 返回 </button>&nbsp;
					</div>
					<!-- /section:basics/content.searchbox -->
					
				</div>

				<!-- /section:basics/content.breadcrumbs -->
				<div class="page-content">					
					<div class="page-content-area">
					
					
						<div class="row">
							<div class="col-xs-12">
								<!-- PAGE CONTENT BEGINS -->
									
								<div class="row">
									<div class="col-xs-12">
									
										demo2
										
									</div><!-- /.span -->
									<div class="col-xs-12">
										<table cellpadding="1" cellspacing="2" border="1">
											<tr>
												<td align="right">IP:</td><td style="width:250px"><input type="text" ng-model="server.ip" style="width:100%"/></td>
											</tr>
											<tr>
												<td align="right">HOSTNAME:</td><td><input type="text" ng-model="server.hostname" style="width:100%"/></td>
											</tr>
											<tr>
												<td align="right">用户名:</td><td><input type="text" ng-model="server.username" style="width:100%"/></td>
											</tr>
											<tr>
												<td align="right">密码:</td><td><input type="password" ng-model="server.password" style="width:100%"/></td>
											</tr>
										</table>
									</div><!-- /.span -->
								</div><!-- /.row -->
								
								
								<!-- PAGE CONTENT ENDS -->
							</div><!-- /.col -->
						</div><!-- /.row -->
					</div><!-- /.page-content-area -->
				</div><!-- /.page-content -->
			</div><!-- /.main-content -->
			
			<%@include file="include/footer.jspf" %>

			<a href="#" id="btn-scroll-up" class="btn-scroll-up btn btn-sm btn-inverse">
				<i class="ace-icon fa fa-angle-double-up icon-only bigger-110"></i>
			</a>
		</div><!-- /.main-container -->

		<!-- basic scripts -->

		<!--[if !IE]> -->
		<script type="text/javascript">
			window.jQuery || document.write("<script src='../assets/js/jquery.min.js'>"+"<"+"/script>");
		</script>

		<!-- <![endif]-->

		<!--[if IE]>
		<script type="text/javascript">
		 window.jQuery || document.write("<script src='../assets/js/jquery1x.min.js'>"+"<"+"/script>");
		</script>
		<![endif]-->
		
		<script type="text/javascript">
			if('ontouchstart' in document.documentElement) document.write("<script src='../assets/js/jquery.mobile.custom.min.js'>"+"<"+"/script>");
		</script>
		<script src="../assets/js/bootstrap.min.js"></script>

		<!-- page specific plugin scripts -->

		<!-- ace scripts -->
		<script src="../assets/js/ace-elements.min.js"></script>
		<script src="../assets/js/ace.min.js"></script>
		
<script>
jQuery(function($) {
	$(document).on('click', 'th input:checkbox' , function(){
		var that = this;
		$(this).closest('table').find('tr > td:first-child input:checkbox')
		.each(function(){
			this.checked = that.checked;
			$(this).closest('tr').toggleClass('selected');
		});
	});
});
		
angular.module('app', ['ngResource'])
.factory('appDAO', ['$resource', function($resource){
	return {
		validSingleServer:function() {
			return $resource("/api/valid_single_server.json");
		}
	}
}])
.controller('appCtrl', ['$scope','appDAO',
	function($scope, appDAO) {

		$scope.server = {"ip":null, "hostname":null, "username":"root", "password":"","type":"single"};

		$scope.go = function(url) {
			document.location.href = url;
		};

		$scope.next = function(url) {
			appDAO.validSingleServer().save({'server':$scope.server}).$promise.then(function(data){
				if(data.server.id);
					$scope.go(url);
			});
		};

	}
]);
</script>
</body>
</html>
