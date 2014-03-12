var registar = angular.module('registar', ['ngRoute']);

registar.config(['$routeProvider', function($routeProvider){
    $routeProvider
        .when('/', { templateUrl: '/static/views/index.html', controller: 'indexController'})
        .when('/add/student/', { templateUrl: '/static/views/add_student.html', controller: 'addStudentController'})
        .when('/student/', { templateUrl: '/static/views/student.html', controller: 'studentController'})
        .when('/secret/', { templateUrl: '/static/views/secret.html', controller: 'addStudentController' })
        .when('/add/project/', { templateUrl: '/static/views/add_project.html', controller: 'addProjectController' })
        .otherwise({ redirectTo: '/' });
}]);