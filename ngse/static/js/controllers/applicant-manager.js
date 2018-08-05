app.controller('applicantManagerController', function($rootScope, $scope, $routeParams, adminService, authService, userService) {

    initController();

    // todo: load types from db
    $scope.validationStatusList = [
        'Accepted',
        'Rejected',
        'On Process'
    ];
    $scope.applicationStatusList = [
        'Submitted',
        'Incomplete Form'
    ];

    function initController() {
        $scope.loading = true;
        adminService.fetchApplicants(function(a) {
        	$scope.applicants = a;
            $scope.loading = false;
        });
    };

    $scope.setValidationStatus = function (applicant, status) {
        if (applicant.application_status === status) {
            return
        }
        userService.setValidationStatus(applicant, status, function(d) {
            applicant.validation_status = status
        })
    }

    $scope.setApplicationStatus = function (applicant, status) {
        if (applicant.application_status === status) {
            return
        }
        userService.setApplicationStatus(applicant, status, function(d) {
            applicant.application_status = status
        })
    }
});