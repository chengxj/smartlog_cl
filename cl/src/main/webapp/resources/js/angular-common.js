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
		go: function(url) {
			document.location.href = url;
		}
	};
}]);