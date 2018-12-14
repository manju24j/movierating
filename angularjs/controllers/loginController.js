
movie.controller('loginController', function($scope , $http) {
    
    $scope.loginData = {
        userName:"",
        password:""
    }
    $scope.login = function(){
        console.log($scope.loginData ,$scope.loginData.userName);
    $http({
        method: 'POST',
        url: 'https://example.com/user/login',
        data: $scope.loginData,
    }).success(function (data, status, headers, config) {
        // handle success things
        console.log("yes");
    }).error(function (data, status, headers, config) {
        // handle error things
        console.log("yes");
    });
};
$scope.signupfn = function(){
    $scope.signup = {
            "username": "",
            "email": "",
            "password": ""
         }
         console.log( $scope.signup);
        $http({
            method: 'POST',
            url: 'https://example.com/user/login',
            data: $scope.loginData,
        }).success(function (data, status, headers, config) {
            // handle success things
            console.log("yes");
        }).error(function (data, status, headers, config) {
            // handle error things
            console.log("yes");
        });
    };
});
movie.directive("passwordVerify", function() {
    return {
        require: "ngModel",
        scope: {
            passwordVerify: '='
        },
        link: function(scope, element, attrs, ctrl) {
            scope.$watch(function() {
                var combined;
                
                if (scope.passwordVerify || ctrl.$viewValue) {
                   combined = scope.passwordVerify + '_' + ctrl.$viewValue; 
                }                    
                return combined;
            }, function(value) {
                if (value) {
                    ctrl.$parsers.unshift(function(viewValue) {
                        var origin = scope.passwordVerify;
                        if (origin !== viewValue) {
                            ctrl.$setValidity("passwordVerify", false);
                            return undefined;
                        } else {
                            ctrl.$setValidity("passwordVerify", true);
                            return viewValue;
                        }
                    });
                }
            });
        }
    };
});