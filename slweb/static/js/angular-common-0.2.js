angular.module('common', ['ngResource'])
.factory('commonDao', ['$resource', '$http', function($resource, $http){
	return {
		validSingleServer:function() {
			return $resource("/api/valid_single_server.json");
		},
		validSingleServerComponents:function() {
			return $resource("/api/valid_single_server_components.json");
		},
		validESingleServerComponents:function() {
			return $resource("/api/valid_esingle_server_components.json");
		},
		validClusterServerComponents:function() {
			return $resource("/api/valid_cluster_server_components.json");
		},
		getSingleServer:function() {
			return $resource("/api/get_single_server.json");
		},
		getSingleServerComponents:function() {
			return $resource("/api/get_single_server_components.json");
		},
		getSingleWarn:function() {
			return $resource("/api/get_single_warn.json");
		},
		getSingleServerFinish:function() {
			return $resource("/api/get_single_server_finish.json");
		},
		getClusterServerComponents:function() {
			return $resource("/api/get_cluster_server_components.json");
		},
		addClusterServerComponents: function() {
			return $resource("/api/add_cluster_server_components.json");
		},
		editClusterServerComponents: function() {
			return $resource("/api/edit_cluster_server_components.json");
		},
		validClusterServerComponents: function() {
			return $resource("/api/valid_cluster_server_components.json");
		},
		getClusterServerFinish:function() {
			return $resource("/api/get_cluster_server_finish.json");
		}
	};
}])
.factory('commonUtil', [function(){
	return {
		createServer: function() {
			return {"ip":"10.0.0.200", "hostname":"cxj001", "username":"root", "password":"ultra","type":"single"};
		},
		ipv4: function() {
			return /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
		},
		go: function(url) {
			document.location.href = url;
		}
	};
}]);
