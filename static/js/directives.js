angular.module('components',[])
	.directive('helloWorld',function(){
			return{
				restrict: 'A',
				templateUrl:"static/partials/hello.html"
			}
		})
		
	
angular.module('testApp',['components'])