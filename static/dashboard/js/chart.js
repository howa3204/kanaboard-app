"use strict";

// Shared Colors Definition
const primary = '#6993FF';
const success = '#1BC5BD';
const info = '#8950FC';
const warning = '#FFA800';
const danger = '#F64E60';

// Class definition
function generateBubbleData(baseval, count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;;
      var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
      var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;
  
      series.push([x, y, z]);
      baseval += 86400000;
      i++;
    }
    return series;
  }

function generateData(count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
        var x = 'w' + (i + 1).toString();
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

        series.push({
            x: x,
            y: y
        });
        i++;
    }
    return series;
}

var KTApexChartsDemo = function () {
	// Private functions
	var _demo1 = function () {
		const apexChart = "#chart_1";
		var options = {
			series: [{
				name: "Cumulative GPA",
				data: cumulative_gpa_trend,
			}],
			chart: {
				height: 240,
				type: 'line',
				zoom: {
					enabled: false
				},
				toolbar: {
					tools: {
						download: false
					}
				}
			},
			dataLabels: { 	
				enabled: false
			},
			stroke: {
				curve: 'straight'
			},
			grid: {
				row: {
					colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
					opacity: 0.5
				},
			},
			xaxis: {
				categories: cumulative_year,
				title: {
					text: 'Year'
				},
			},
			yaxis: {
				min: 0,
				max: 4.0,
				tickAmount: 8,
				title: {
					text: 'GPA'
				},
			},
			colors: [primary]
		};

		var chart = new ApexCharts(document.querySelector(apexChart), options);
		chart.render();
	}

	var _demo4 = function () {
		const apexChart = "#chart_4";
		var options = {
			series: [{
				name: "Cumulative GPA",
				data: bcpm_gpa_trend,
			}],
			chart: {
				height: 240,
				type: 'line',
				zoom: {
					enabled: false
				},
				toolbar: {
					tools: {
						download: false
					}
				}
			},
			dataLabels: { 	
				enabled: false
			},
			stroke: {
				curve: 'straight'
			},
			grid: {
				row: {
					colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
					opacity: 0.5
				},
			},
			xaxis: {
				categories: bcpm_year,
				title: {
					text: 'Year'
				},
			},
			yaxis: {
				min: 0,
				max: 4.0,
				tickAmount: 8,
				title: {
					text: 'GPA'
				},
			},
			colors: [primary]
		};

		var chart = new ApexCharts(document.querySelector(apexChart), options);
		chart.render();
	}

	var _demo2 = function () {
		const apexChart = "#chart_2";
		var options = {
			series: [{
				name: 'series1',
				data: [31, 40, 28, 51, 42, 109, 100]
			}, {
				name: 'series2',
				data: [11, 32, 45, 32, 34, 52, 41]
			}],
			chart: {
				height: 350,
				type: 'area'
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: 'smooth'
			},
			xaxis: {
				type: 'datetime',
				categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
			},
			tooltip: {
				x: {
					format: 'dd/MM/yy HH:mm'
				},
			},
			colors: [primary, success]
		};

		var chart = new ApexCharts(document.querySelector(apexChart), options);
		chart.render();
	}

	var _demo3 = function () {
		const apexChart = "#chart_3";
		var options = {
			series: [{
				name: 'Section Score',
				data: mcat_data,
			}],
			chart: {
				type: 'bar',
				height: 240,
				toolbar: {
					tools: {
						download: false
					}
				}
			},
			plotOptions: {
				bar: {
					horizontal: false,
					columnWidth: '40%',
					endingShape: 'rounded'
				},
			},
			dataLabels: {
				enabled: true
			},
			stroke: {
				show: true,
				width: 2,
				colors: ['transparent']
			},
			xaxis: {
				title: {
					text: 'Section'
				},
				categories: ['Chem/Physics', 'Bio/Biochem', 'Pysch/Soc', 'CARS'],
			},
			yaxis: {
				title: {
					text: 'Score'
				},
				min: 116,
				max: 132,
				tickAmount: 8,
			},
			fill: {
				opacity: 1
			},
			colors: [primary, success, warning]
		};

		var chart = new ApexCharts(document.querySelector(apexChart), options);
		chart.render();
	}

	return {
		// public functions
		init: function () {
			_demo1();
			_demo2();
			_demo3();
			_demo4();
		}
	};
}();

jQuery(document).ready(function () {
	KTApexChartsDemo.init();
});
