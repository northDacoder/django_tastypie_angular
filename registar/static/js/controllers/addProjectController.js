function addProjectController($scope, $http) {

    $scope.submitForm = function() {
        $http.post('/api/v1/student/?format=json', $scope.student)
            .success(function(response){
                $location.path('/');
            });
    }
}