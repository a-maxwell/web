app.controller('lifetimeController',
    function($rootScope, $scope, $routeParams, adminService,
             formService, messageService) {

      initController();

      function initController() {
        console.log('Fetching form');
        $scope.loading = true;
        formService.fetchForms(function(forms) {
          console.log('Fetching form');
          if (!forms) {
            messageService.pushMessage({
              text: 'Error fetchnig forms',
              type: 'error',
            });
          }
          $scope.forms = forms;
          $scope.loading = false;
        });
      }

      $scope.updateForm = function(form, param) {

        if (param.date_start > param.date_end) {
          return;
        }

        angular.extend(form, param);

        formService.updateForm(form, function(data) {
          if (!data) {
            messageService.pushMessage({
              text: 'Error while updating form',
              type: 'error',
            });
          } else {
            messageService.pushMessage({
              text: 'Form updated',
              type: 'info',
            });
          }
        });
      }
      ;

    });
