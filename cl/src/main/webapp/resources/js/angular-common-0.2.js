angular.module('common', ['ngResource'])
.factory('commonDao', ['$resource', function($resource){
	return {
		validSingleServer:function() {
			return $resource("/api/valid_single_server.json");
		}
	};
}])
.factory('commonUtil', [function(){
	return {
		createServer: function() {
			return {"ip":"10.0.0.200", "hostname":"cxj001", "username":"root", "password":"1423","type":"single"};			
		},
		ipv4: function() {
			return /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
		},
		go: function(url) {
			document.location.href = url;
		}
	};
}]);