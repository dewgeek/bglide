'use strict';

angular.module('testApp',[])
	.config(function($routeProvider,$locationProvider){
	$routeProvider.when('hello',{
		templateUrl:'static/partials/hello.html'

	})	
	$locationProvider.html5Mode(true);
})