function indexController($scope, $http,) {

    $http.get('api/v1/student/?format=json').success(function(data){

    });

}