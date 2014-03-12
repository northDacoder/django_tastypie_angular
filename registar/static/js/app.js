var registar = angular.module('registar', ['ngRoute']);

registar.config(['$routeProvider', function($routeProvider){
    $routeProvider
        .when('/', { templateUrl: '/static/views/index.html', controller: 'indexController'})
        .otherwise({ redirectTo: '/' });
}]);