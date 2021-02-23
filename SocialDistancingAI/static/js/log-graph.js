var jsonfile = {};
let dropdown = $('#log-dropdown');
var unit = 'second';
var chart;
const url = 'http://localhost:5000/get-all-logs';

$(document).ready(function () {
    dropdown.empty();

    dropdown.append('<option selected="true" disabled>Select log file: </option>');
    dropdown.prop('selectedIndex', 0);

    // Populate dropdown with list of logs
    $.getJSON(url, function (data) {
        $.each(data, function (key, entry) {
            dropdown.append($('<option></option>').attr('value', entry).text(entry));
        });
        dropdown.prop('selectedIndex', 1);
        create_chart();
    });
});




function toggle_unit(string) {
    unit = string;
    create_chart();
}


$('#log-dropdown').change(create_chart);


function create_chart() {
    const context = canvas.getContext('2d');

    context.clearRect(0, 0, canvas.width, canvas.height);
    value = $('#log-dropdown').val();
    $.get(`http://localhost:5000/logs/${value}`, (data) => {

        if ($.trim(data)) {
            jsonfile = JSON.parse(data);

            var labels = jsonfile.entries.map(function (e) {
                return e.time;
            });
            var data = jsonfile.entries.map(function (e) {
                return e.violations;
            });

            var ctx = canvas.getContext('2d');
            var config = {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Violations',
                        data: data,
                        backgroundColor: 'rgba(0, 119, 204, 0.3)'
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        xAxes: [{
                            type: 'time',
                            time: {
                                parser: 'hh:mm:ss',
                                tooltipFormat: 'hh:mm:ss',
                                unit: unit,
                                unitStepSize: 1,
                                displayFormats: {
                                    second: 'hh:mm:ss',
                                }
                            },
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Time'
                            },
                            ticks: {
                                source: 'auto',
                                major: {
                                    fontStyle: 'bold',
                                    fontColor: '#FF0000'
                                }
                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Violations'
                            }
                        }]
                    }
                }

            };
            if (typeof(chart) != "undefined") {
                chart.destroy();
            }
            chart = new Chart(ctx, config);
            chart.update();
        }
        else {
            var ctx = canvas.getContext('2d');
            var config = {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'No data available',
                        data: [0],
                        backgroundColor: 'rgba(0, 119, 204, 0.3)'
                    }]
                }
            };
            if (typeof(chart) != "undefined") {
                chart.destroy();
            }
            chart = new Chart(ctx, config);
            chart.update();
        }


    });
}