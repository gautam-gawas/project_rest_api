var projectApp = angular.module('projectApp',['ngRoute','projectControllers']);

projectApp.config(["$routeProvider",
    function($routeProvider){
        $routeProvider.when("/project/:projectId"),{
            templateUrl : 'http://127.0.0.1:8000/templates/school/project_details.html,
            controllers: 'projectControllers',
        }
    },

]);

projectApp.config(["$httpProvider",
    function($httpProvider){
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
 ]);