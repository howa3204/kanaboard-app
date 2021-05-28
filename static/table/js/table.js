"use strict";
// Class definition

var KTDatatableHtmlTableDemo = function() {
    // Private functions

    // demo initializer
    var demo = function() {

        var datatable = $('#kt_datatable').KTDatatable({
            data: {
                saveState: {cookie: false},
            },
            pagination: false,
            translate: {
                records: {
                    noRecords: 'Click on Add Task to get started!',
                },
            },
            search: {
                input: $('#kt_datatable_search_query'),
                key: 'generalSearch'
            },
            columns: [
                {
                    field: 'Task',
                    title: 'Task',
                }, {
                    field: 'Tag',
                    title: 'Tag',
                    autoHide: false,
                    // callback function support for column rendering
                    template: function(row) {
                        var status = {
                            1: {
                                'title': 'Activities',
                                'class': ' label-light-warning'
                            },
                            2: {
                                'title': 'Coursework',
                                'class': ' label-light-danger'
                            },
                            3: {
                                'title': 'Letters',
                                'class': ' label-light-primary'
                            },
                            4: {
                                'title': 'MCAT',
                                'class': ' label-light-success'
                            },
                            5: {
                                'title': 'Primary Essays',
                                'class': ' label-light-info'
                            },
                            6: {
                                'title': 'Secondaries',
                                'class': ' label-light-muted'
                            },
                            7: {
                                'title': 'Other',
                                'class': ' label-light-muted'
                            }
                        };
                        return '<span class="label font-weight-bold label-lg' + status[row.Tag].class + ' label-inline">' + status[row.Tag].title + '</span>';
                    },
                }, {
                    field: 'Due Date',
                    type: 'date',
                    format: 'MM-DD-YYYY',
                },{
                    field: 'Priority',
                    title: 'Priority',
                    autoHide: false,
                    // callback function support for column rendering
                    template: function(row) {
                        var status = {
                            1: {
                                'title': 'Urgent',
                                'state': 'danger'
                            },
                            2: {
                                'title': 'High',
                                'state': 'warning'
                            },
                            3: {
                                'title': 'Medium',
                                'state': 'primary'
                            },
                            4: {
                                'title': 'Low',
                                'state': 'success'
                            },
                        };
                        return '<span class="label-' + status[row.Priority].state + ' mr-2"></span><span class="font-weight-bold text-' +status[row.Priority].state + '">' +    status[row.Priority].title + '</span>';
                    },
                }, {
                    field: 'Actions',
                    type: 'Actions',
                },
            ],
        });

        $('#kt_datatable_search_status').on('change', function() {
            datatable.search($(this).val().toLowerCase(), 'Tag');
        });

        $('#kt_datatable_search_type').on('change', function() {
            datatable.search($(this).val().toLowerCase(), 'Priority');
        });

        $('#kt_datatable_search_status, #kt_datatable_search_type').selectpicker();

        // Activities Table

        var activities_datatable = $('#activities_datatable').KTDatatable({
            pagination: false,
            toolbar: {
                placement: ['top']
            },
            data: {
                type: 'local',
                saveState: {cookie: false},
            },
            translate: {
                records: {
                    noRecords: 'Click on Add Activity to get started!',
                },
            },
            search: {
                input: $('#activities_datatable_search_query'),
                key: 'generalSearch'
            },
            columns: [
                {
                    field: 'Activity',
                    title: 'Activity',
                },
                {
                    field: 'Experience Type',
                    title: 'Experience Type',
                },
                {
                    field: 'Hours',
                    title: 'Hours',
                },
                {
                    field: 'Start Date',
                    title: 'Start Date',
                },
                {
                    field: 'End Date',
                    title: 'End Date',
                },
            ],
        });

        $('#activities_datatable_search_status, #activities_datatable_search_type').selectpicker();

        // Coursework Table

        var coursework_datatable = $('#coursework_datatable').KTDatatable({
            pagination: false,
            toolbar: {
                placement: ['top']
            },
            data: {
                type: 'local',
                saveState: {cookie: false},
            },
            translate: {
                records: {
                    noRecords: 'Click on Add Course to get started!',
                },
            },
            columns: [
                {
                    field: 'Activity',
                    title: 'Activity',
                },
                {
                    field: 'Experience Type',
                    title: 'Experience Type',
                },
                {
                    field: 'Hours',
                    title: 'Hours',
                },
                {
                    field: 'Start Date',
                    title: 'Start Date',
                },
                {
                    field: 'End Date',
                    title: 'End Date',
                },
                {
                    field: 'Actions',
                    title: 'Actions',
                },
            ],
        });

        // Letters of Reccomendation Table

        var letters_datatable = $('#letters_datatable').KTDatatable({
            pagination: false,
            toolbar: {
                placement: ['top']
            },
            data: {
                type: 'local',
                saveState: {cookie: false},
            },
            translate: {
                records: {
                    noRecords: 'Click on Add Letter to get started!',
                },
            },
            search: {
                input: $('#letters_datatable_search_query'),
                key: 'generalSearch'
            },
            columns: [
                {
                    field: 'Course Name',
                    title: 'Course Name',
                    autoHide: false,
                },
                {
                    field: 'Year',
                    title: 'Year',
                    autoHide: false,
                },
                {
                    field: 'Course Number',
                    title: 'Course Number',
                    autoHide: false,
                },
                {
                    field: 'Academic Term',
                    title: 'Academic Term',
                    autoHide: false,
                },
                {
                    field: 'End Date',
                    title: 'End Date',
                    autoHide: false,
                },
                {
                    field: 'Credit Hours',
                    title: 'Credit Hours',
                    autoHide: false,
                },
                {
                    field: 'Grade',
                    title: 'Grade',
                    autoHide: false,
                },
                {
                    field: 'Actions',
                    title: 'Actions',
                    autoHide: false,
                },
            ],
        });

        $('#letters_datatable_search_status, #letters_datatable_search_type').selectpicker();

        // MCAT Table

        var mcat_datatable = $('#mcat_datatable').KTDatatable({
            pagination: false,
            toolbar: {
                placement: ['top']
            },
            data: {
                type: 'local',
                saveState: {cookie: false},
            },
            translate: {
                records: {
                    noRecords: 'Click on Add MCAT to get started!',
                },
            },
            search: {
                input: $('#mcat_datatable_search_query'),
                key: 'generalSearch'
            },
            columns: [
                {
                    field: 'Test',
                    title: 'Test',
                    width: 200,
                },
                {
                    field: 'Date',
                    title: 'Date',
                    width: 80,
                },
                {
                    field: 'Bio & Biochem',
                    title: 'Bio & Biochem',
                    width: 100,
                },
                {
                    field: 'Chem & Phys',
                    title: 'Chem & Phys',
                    width: 90,
                },
                {
                    field: 'Psych & Soc',
                    title: 'Psych & Soc',
                    width: 80,
                },
                {
                    field: 'CARS',
                    title: 'CARS',
                    width: 80,
                },
                {
                    field: 'Total Score',
                    title: 'Total Score',
                    width: 80,
                },
                {
                    field: 'Actions',
                    title: 'Actions',
                },
            ],
        });

        $('#mcat_datatable_search_status, #mcat_datatable_search_type').selectpicker();

    };

    return {
        // Public functions
        init: function() {
            // init dmeo
            demo();
        },
    };
}();

jQuery(document).ready(function() {
    KTDatatableHtmlTableDemo.init();
});
