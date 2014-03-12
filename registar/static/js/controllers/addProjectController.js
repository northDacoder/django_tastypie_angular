function addProjectController($scope, $http, $location) {

    $scope.get('/api/v1/student/?format=json').success(function(data){
        console.log(data);
    }).error(function(data){
        console.log(data);
    })

    $scope.submitForm = function() {
        $http.post('/api/v1/student/?format=json')
            .success(function(students){
                $scope.students = students.objects;
            });
    }


}