function addStudentController($scope, $http) {
    $http.get('/api/v1/class/?format=json')
        .success(function(classes){
            console.log(classes);
            $scope.classes = classes.objects;
        });

    $scope.submitForm = function() {
        $http.post('/api/v1/student/?format=json', $scope.student)
            .success(function(response){
                $location.path('/');
            });
    }
}