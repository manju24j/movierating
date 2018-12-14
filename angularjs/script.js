var movie = angular.module('movie', ['ngRoute','ui.bootstrap']);
movie.config(function($routeProvider) {
    $routeProvider
                // route for the home page

    .when('/', {
        templateUrl : 'pages/home.html',
        controller  : 'homeController'
    })
            // route for the BookMarks page

    .when('/BookMarks', {
        templateUrl : 'pages/BookMarks.html',
        controller  : 'BookMarksController'
    })
                // route for the Suggested_movie.html page

    .when('/Suggested', {
        templateUrl : 'pages/Suggested_movie.html',
        controller  : 'Suggested_movieController'
    })

    .when('/login', {
        templateUrl : 'pages/login.html',
        controller  : 'loginController'
    });
});
