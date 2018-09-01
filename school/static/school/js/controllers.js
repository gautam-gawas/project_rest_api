var projectControllers = angular.module('projectControllers',[]);

projectControllers.projectControllers('ProjectDetailControllers',['$scope','$routeParams','$http',
    function($scope,$routeParams,$http){
        $http.get('http://127.0.0.1:8000/prjoect/api/project/' + $routeParams.projectId + '/?format=json'
        ).success(function(data){
           $scope.project = data;
        });
    }

]);