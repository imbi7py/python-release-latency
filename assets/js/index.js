//jQuery
//execute files in global context with script-loader: https://github.com/webpack/script-loader
require('script-loader!jquery/dist/jquery.min');

//Bootstrap JS
require('bootstrap/dist/js/bootstrap.min');

//Datatables, jQuery Grid Component
require('datatables/media/js/jquery.dataTables.min');

//PatternFly Custom Componets -  Sidebar, Popovers and Datatables Customizations
//Note: jquery.dataTables.js must occur in the html source before patternfly*.js
require('patternfly/dist/js/patternfly.min.js');

//Moment
require('moment/min/moment.min');

// Patternfly styles
require("patternfly/dist/css/patternfly.css");
require("patternfly/dist/css/patternfly-additions.css");
