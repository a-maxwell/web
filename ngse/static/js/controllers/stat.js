app.controller('statController',
    function($rootScope, $scope, $routeParams, $location, authService,
             adminService, $http) {

      $scope.aTypes = {
        'Master of Science': {
          'CE': 0,
          'ChE': 0,
          'CS': 0,
          'EE': 0,
          'EgyE': 0,
          'EnE': 0,
          'GmE': 0,
          'IE': 0,
          'ME': 0,
          'MetE': 0,
          'MSE': 0,
          'Total': 0,
        },
        'Doctor of Philosophy': {
          'CE': 0,
          'ChE': 0,
          'EEE': 0,
          'EnE': 0,
          'EgyE': 0,
          'MSE': 0,
          'Total': 0,
        },
        'Master of Engineering': {'EE': 0, 'IE': 0, 'Total': 0},
        'Doctor of Engineering': {'ChE': 0, 'EEE': 0, 'Total': 0},
      };

      function initController() {
        $scope.loading = true;
        adminService.fetchApplicants(function(a) {
          $scope.applicants = a;
          $scope.loading = false;
          calculate(a);
        });
      }

      initController();

      function calculate(a) {
        $scope.total = a.length;
        $scope.regularFormsCount = a.filter(e => {
          return e.user_type !== 'ERDT Applicant';
        }).length;
        $scope.erdtFormsCount = $scope.total - $scope.regularFormsCount;
        $scope.incompleteFromsCount = a.filter(e => {
          return e.application_status !== 'Complete';
        }).length;

        for (aType in $scope.aTypes) {

          let aTypeApplications = $scope.applicants.filter((a) => {
            if (a.level === aType) {
              $scope.aTypes[aType][a.program]++;
            }
            ;
            return a.level === aType;
          });
          let total = aTypeApplications.length;
          $scope.aTypes[aType]['Total'] = aTypeApplications.length;

          if (total !== 0) {
            for (let a of aTypeApplications) {
              console.log(a);
              $scope.aTypes[aType][a.program] /= total / 100;
              $scope.aTypes[aType][a.program] = $scope.aTypes[aType][a.program].toFixed(
                  2);
            }
          }
        }
      }

      $scope.print = function() {

      };

      $scope.pdf = function() {
        console.log('exporting to pdf...');
        let html = document.getElementById('pdfArea').innerHTML;
        var pdf = new jsPDF('p', 'pt', 'a4');

        let pdfStyle = '<style>table, th, td {' +
            '        border-collapse: collapse;' +
            '        border: 1px solid black;' +
            '        width: 580px;' +
            '        text-align: center;' +
            '    }' +
            '' +
            '    table {' +
            '        margin-bottom: 20px;' +
            '    }</style>';

        html += pdfStyle;
        console.log(html);
        html2pdf(html, pdf, function(pdf) {
          pdf.output('save')
        });
      };
    });