app.factory('userService', function($rootScope, $http, $cookies, $location, authService, messageService) {
    var methods = {};

    var user = {};

    methods.answered = function() {
        return user.answered_pos;
    }

    methods.fetchUser = function(callback) {
        var user_id = authService.getUserID();
        return $http.get('/v1/users/show', {params: {'user_id': user_id}})
        .then(function successCallback(response) {
            var d = response.data;
            user = d;
            callback(d);
        }, function errorCallback(response) {
            callback({success: false});
        });
    }

    if (authService.isLoggedIn()) methods.fetchUser(function(data) {
        console.log(data);
    })

    methods.getUser = function() {
        return user;
    }

    methods.clear = function() {
        user = {};
    }

    methods.saveAnswers = function(callback, user_controller) {
        var user_id = authService.getUserID();

        $http.post('/v1/users/update', {'user_id': user_id, 'user': user_controller})
        .then(function successCallback(response) {
            user = user_controller;
            user.answered_pos = true;
            var d = response.data;
            callback(d);
        }, function errorCallback(response) {
            callback({success: false});
        });
    }

    methods.setApplicationStatus = function(user, status, callback) {
        var url = '/v1/users/'+user.id+'/application/status';
        $http.post(url, {'status': status})
        .then(function successCallback(response) {
            var d = response.data;
            callback(d);
        }, function errorCallback(response) {
            messageService.pushMessage({
              text: 'Error changing application status',
              type: 'error'
            })
        });
    };

    methods.setValidationStatus = function(user, status, callback) {
        var url = '/v1/users/'+user.id+'/validation/status';
        $http.post(url, {'status': status})
        .then(function successCallback(response) {
            var d = response.data;
            callback(d);
        }, function errorCallback(response) {
            messageService.pushMessage({
              text: 'Error changing validation status',
              type: 'error'
            })
        });
    };

    return methods;
});