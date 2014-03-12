function addStudentController($scope, $http) {
    $http.get('/api/v1/class/?format=json')
        .success(function(classes){
            console.log(classes);
            $scope.classes = classes.objects;
        });
}