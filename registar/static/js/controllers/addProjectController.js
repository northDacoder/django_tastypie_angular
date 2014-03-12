function addProjectController($scope, $http, $location) {

    $scope.get('/api/v1/student/?format=json')

    $scope.submitForm = function() {
        $http.post('/api/v1/student/?format=json')
            .success(function(students){
                $scope.students = students.objects;
            });
    }


}