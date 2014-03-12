function indexController($scope, $http) {

    $http.get('api/v1/student/?format=json')
        .success(function(students){
            console.log(students);
            $scope.students = students.objects;
    });

}