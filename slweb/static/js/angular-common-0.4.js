angular.module('common', ['ngResource']).factory('commonDao', ['$resource',
function($resource) {
    return {
        addSingleServer: function() {
            return $resource("/api/add_single_server.json");
        },
        addSingleServerComponents: function() {
            return $resource("/api/add_single_server_components.json");
        },
        editSingleServerComponents: function() {
            return $resource("/api/edit_single_server_components.json");
        },
        getSingleServer: function() {
            return $resource("/api/get_single_server.json");
        },
        getSingleServerComponents: function() {
            return $resource("/api/get_single_server_components.json");
        },
        getSingleWarn: function() {
            return $resource("/api/get_single_warn.json");
        },
        getSingleServerFinish: function() {
            return $resource("/api/get_single_server_finish.json");
        },
        getClusterServerComponents: function() {
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
        getClusterServerFinish: function() {
            return $resource("/api/get_cluster_server_finish.json");
        },
        getClusterName: function() {
            return $resource("/api/get_cluster_name.json");
        },
        installSingleServer: function() {
            return $resource("/api/install_single_server.json");
        },
        installClusterServer: function() {
            return $resource("/api/install_cluster_server.json");
        }
    };
}]).factory('commonUtil', [function() {
    return {
        defaultSingleServer: function() {
            return {
                "ip": null,
                "hostname": null,
                "username": null,
                "password": null,
                "type": "single"
            };
        },
        defaultClusterServer: function(cluster_name, role) {
            return {
                "id": null,
                "ip": "10.0.0.200",
                "cluster_name": cluster_name,
                "role": role,
                "hostname": null,
                "username": "root",
                "password": null,
                "type": "cluster"
            };
        },
        serverComponent: function(type) {
            return {
                "type": type,
                "port": null,
                "install_dir": null,
                "data_dir": null,
                "log_dir": null,
                "install_bs": false,
                "db_username": "",
                "db_password": "",
                "web_service_name": "",
                "es_memory_limit": "",
                "es_index_number_of_shards": "",
                "es_index_refresh_interval": "",
                "es_path_data": "",
                "es_path_logs": "",
                "storm_works_num_per_host": "",
                "storm_dataProcess_works_num": "",
                "storm_dataIndex_works_num": "",
                "storm_spout_config_num": "",
                "storm_spout_dataprocess_num": "",
                "storm_spout_dataindex_num": "",
                "storm_bolt_default_num": "",
                "storm_bolt_rule_num": "",
                "storm_bolt_advanced_num": "",
                "storm_bolt_kafka_num": "",
                "storm_bolt_es_num": "",
                "frontend_service_name": ""
            };
        },
        serverComponents: function(id) {
            return {
                "id": id,
                "ip": null,
                "cluster_name": "",
                "hostname": null,
                "username": null,
                "password": null,
                "components": []
            };
        },
        componentsName: function() {
            return ["ZOOKEEPER", "KAFKA", "FLUME", "STORM", "ELASTICSEARCH", "FRONTEND", "DATABASE", "WEB"];
        },
        defaultComponents: function() {
            return {
                "ZOOKEEPER": {
                    "type": "ZOOKEEPER",
                    "port": "2181",
                    "install_dir": "/home/ultrapower",
                    "data_dir": "/home/ultrapower/data",
                    "log_dir": "/home/ultrapower/logs",
                    "install_bs": false,
                    "db_username": "",
                    "db_password": "",
                    "web_service_name": "",
                    "es_memory_limit": "",
                    "es_index_number_of_shards": "",
                    "es_path_data": "",
                    "es_path_logs": "",
                    "es_index_refresh_interval": "",
                    "storm_works_num_per_host": "",
                    "storm_dataProcess_works_num": "",
                    "storm_dataIndex_works_num": "",
                    "storm_spout_config_num": "",
                    "storm_spout_dataprocess_num": "",
                    "storm_spout_dataindex_num": "",
                    "storm_bolt_default_num": "",
                    "storm_bolt_rule_num": "",
                    "storm_bolt_advanced_num": "",
                    "storm_bolt_kafka_num": "",
                    "storm_bolt_es_num": "",
                    "frontend_service_name": ""
                },
                "KAFKA": {
                    "type": "KAFKA",
                    "port": "9092",
                    "install_dir": "/home/ultrapower",
                    "data_dir": "/home/ultrapower/data",
                    "log_dir": "/home/ultrapower/logs",
                    "install_bs": false,
                    "db_username": "",
                    "db_password": "",
                    "web_service_name": "",
                    "es_memory_limit": "",
                    "es_index_number_of_shards": "",
                    "es_index_refresh_interval": "",
                    "es_path_data": "",
                    "es_path_logs": "",
                    "storm_works_num_per_host": "",
                    "storm_dataProcess_works_num": "",
                    "storm_dataIndex_works_num": "",
                    "storm_spout_config_num": "",
                    "storm_spout_dataprocess_num": "",
                    "storm_spout_dataindex_num": "",
                    "storm_bolt_default_num": "",
                    "storm_bolt_rule_num": "",
                    "storm_bolt_advanced_num": "",
                    "storm_bolt_kafka_num": "",
                    "storm_bolt_es_num": "",
                    "frontend_service_name": ""
                },
                "FLUME": {
                    "type": "FLUME",
                    "port": null,
                    "install_dir": "/home/ultrapower",
                    "data_dir": "/home/ultrapower/data",
                    "log_dir": "/home/ultrapower/logs",
                    "install_bs": false,
                    "db_username": "",
                    "db_password": "",
                    "web_service_name": "",
                    "es_memory_limit": "",
                    "es_index_number_of_shards": "",
                    "es_index_refresh_interval": "",
                    "es_path_data": "",
                    "es_path_logs": "",
                    "storm_works_num_per_host": "",
                    "storm_dataProcess_works_num": "",
                    "storm_dataIndex_works_num": "",
                    "storm_spout_config_num": "",
                    "storm_spout_dataprocess_num": "",
                    "storm_spout_dataindex_num": "",
                    "storm_bolt_default_num": "",
                    "storm_bolt_rule_num": "",
                    "storm_bolt_advanced_num": "",
                    "storm_bolt_kafka_num": "",
                    "storm_bolt_es_num": "",
                    "frontend_service_name": ""
                },
                "STORM": {
                    "type": "STORM",
                    "port": null,
                    "install_dir": "/home/ultrapower",
                    "data_dir": "/home/ultrapower/data",
                    "log_dir": "/home/ultrapower/logs",
                    "install_bs": false,
                    "db_username": "",
                    "db_password": "",
                    "web_service_name": "",
                    "es_memory_limit": "",
                    "es_index_number_of_shards": "",
                    "es_index_refresh_interval": "",
                    "es_path_data": "",
                    "es_path_logs": "",
                    "storm_works_num_per_host": "5",
                    "storm_dataProcess_works_num": "6",
                    "storm_dataIndex_works_num": "6",
                    "storm_spout_config_num": "1",
                    "storm_spout_dataprocess_num": "10",
                    "storm_spout_dataindex_num": "10",
                    "storm_bolt_default_num": "10",
                    "storm_bolt_rule_num": "10",
                    "storm_bolt_advanced_num": "10",
                    "storm_bolt_kafka_num": "10",
                    "storm_bolt_es_num": "20",
                    "frontend_service_name": ""
                },
                "ELASTICSEARCH": {
                    "type": "ELASTICSEARCH",
                    "port": "9300",
                    "install_dir": "/home/ultrapower",
                    "data_dir": "/home/ultrapower/data",
                    "log_dir": "/home/ultrapower/logs",
                    "install_bs": false,
                    "db_username": "",
                    "db_password": "",
                    "web_service_name": "",
                    "es_memory_limit": "2g",
                    "es_index_number_of_shards": "3",
                    "es_index_refresh_interval": "3s",
                    "es_path_data": "/home/ultrapower/data/elasticsearch",
                    "es_path_logs": "/home/ultrapower/logs/elasticsearch",
                    "storm_works_num_per_host": "",
                    "storm_dataProcess_works_num": "",
                    "storm_dataIndex_works_num": "",
                    "storm_spout_config_num": "",
                    "storm_spout_dataprocess_num": "",
                    "storm_spout_dataindex_num": "",
                    "storm_bolt_default_num": "",
                    "storm_bolt_rule_num": "",
                    "storm_bolt_advanced_num": "",
                    "storm_bolt_kafka_num": "",
                    "storm_bolt_es_num": "",
                    "frontend_service_name": ""
                },
                "FRONTEND": {
                    "type": "FRONTEND",
                    "port": "8899",
                    "install_dir": "/home/ultrapower",
                    "data_dir": "/home/ultrapower/data",
                    "log_dir": "/home/ultrapower/logs",
                    "install_bs": false,
                    "db_username": "",
                    "db_password": "",
                    "web_service_name": "",
                    "es_memory_limit": "",
                    "es_index_number_of_shards": "",
                    "es_index_refresh_interval": "",
                    "es_path_data": "",
                    "es_path_logs": "",
                    "storm_works_num_per_host": "",
                    "storm_dataProcess_works_num": "",
                    "storm_dataIndex_works_num": "",
                    "storm_spout_config_num": "",
                    "storm_spout_dataprocess_num": "",
                    "storm_spout_dataindex_num": "",
                    "storm_bolt_default_num": "",
                    "storm_bolt_rule_num": "",
                    "storm_bolt_advanced_num": "",
                    "storm_bolt_kafka_num": "",
                    "storm_bolt_es_num": "",
                    "frontend_service_name": "frontend"
                },
                "DATABASE": {
                    "type": "DATABASE",
                    "port": "3306",
                    "install_dir": "/home/ultrapower",
                    "data_dir": "/home/ultrapower/data",
                    "log_dir": "/home/ultrapower/logs",
                    "install_bs": false,
                    "db_username": "smartlog",
                    "db_password": "smartlog",
                    "web_service_name": "",
                    "es_memory_limit": "",
                    "es_index_number_of_shards": "",
                    "es_index_refresh_interval": "",
                    "es_path_data": "",
                    "es_path_logs": "",
                    "storm_works_num_per_host": "",
                    "storm_dataProcess_works_num": "",
                    "storm_dataIndex_works_num": "",
                    "storm_spout_config_num": "",
                    "storm_spout_dataprocess_num": "",
                    "storm_spout_dataindex_num": "",
                    "storm_bolt_default_num": "",
                    "storm_bolt_rule_num": "",
                    "storm_bolt_advanced_num": "",
                    "storm_bolt_kafka_num": "",
                    "storm_bolt_es_num": "",
                    "frontend_service_name": ""
                },
                "WEB": {
                    "type": "WEB",
                    "port": "8888",
                    "install_dir": "/home/ultrapower",
                    "data_dir": "/home/ultrapower/data",
                    "log_dir": "/home/ultrapower/logs",
                    "install_bs": false,
                    "db_username": "",
                    "db_password": "",
                    "web_service_name": "web",
                    "es_memory_limit": "",
                    "es_index_number_of_shards": "",
                    "es_index_refresh_interval": "",
                    "es_path_data": "",
                    "es_path_logs": "",
                    "storm_works_num_per_host": "",
                    "storm_dataProcess_works_num": "",
                    "storm_dataIndex_works_num": "",
                    "storm_spout_config_num": "",
                    "storm_spout_dataprocess_num": "",
                    "storm_spout_dataindex_num": "",
                    "storm_bolt_default_num": "",
                    "storm_bolt_rule_num": "",
                    "storm_bolt_advanced_num": "",
                    "storm_bolt_kafka_num": "",
                    "storm_bolt_es_num": "",
                    "frontend_service_name": ""
                }
            };
        },
        ipv4: function() {
            return /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
        },
        go: function(url) {
            document.location.href = url;
        }
    };
}]);
