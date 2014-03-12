function studentController($scope, $http, $routeParams) {

    $http.get('api/v1/student/' + $routeParams.id + '/?format=json')
        .success(function(student){
            console.log(student);
            $scope.student = student;
    }).error(function(student){
        console.log("You have an error in your code");
    });

}

