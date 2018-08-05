app.directive('datepicker', function($timeout) {
  return {
    restrict: 'E',
    require: ['^ngModel'],
    replace: true,
    template: '<div class="ui calendar" >\n' +
    '    <div class="ui input left icon"> \n' +
    '      <i class="calendar icon"></i>\n' +
    '      <input type="text" placeholder="">\n' +
    '    </div>\n' +
    '  </div>',
    link: function(scope, element, attrs, ngModel) {

      ngModel = ngModel[0];

      let calendar = $(element);
      let inputDiv = calendar.children('.input');

      scope.$watch(function() {
        return ngModel.$modelValue;
      }, function(modelValue) {

        $timeout(function() {
          calendar.calendar('set date', modelValue);
        });

      });
      scope.$watch(attrs.invalid, function(newVal) {
        scope.invalid = newVal;
      });

      function onChange(date, text, mode) {
        if (date !== undefined) {
          scope.$apply(function() {
            ngModel.$setViewValue(moment(date).format('YYYY-MM-DD HH:mm:ss'));
          });
        }

        if (date === undefined || scope.invalid) {
          inputDiv.addClass('error');
        } else {
          inputDiv.removeClass('error');
        }
      }

      calendar.calendar({
        type: 'datetime',
        ampm: false,
        formatter: {
          'datetime': function(date, settings) {
            return moment(date).format('YYYY-MM-DD HH:mm:ss');
          },
        },
        onChange: onChange,
      });

    },
  };
});