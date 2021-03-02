var jsonfile = {};
let dropdown = $('#log-dropdown');
var unit = 'hour';
var chart;
const url = '/get-all-logs';

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

$('#refresh-button').on('click', ()=>{
    create_chart()
    $('#refresh').addClass("fa-spin")
    setTimeout(function() { $('#refresh').removeClass('fa-spin'); }, 1000);

})




function toggle_unit(string) {
    unit = string;
    create_chart();
}

const unit_map = {
    'second': {'substring': 8, 'parser': 'hh:mm:ss', 'unit': 'second', 'type': 'line'}, 
    'minute': {'substring': 5, 'parser': 'hh:mm', 'unit': 'minute', 'type': 'line' }, 
    'ten-minutes': {'substring': 4, 'parser': 'hh:mm', 'unit': 'minute', 'type': 'line'}, 
    'hour': {'substring': 3, 'parser': 'hh', 'unit': 'hour', 'type': 'line'}, 
    'day': {'substring': 0, 'parser': 'hh', 'unit': 'day', 'type': 'bar'}}


$('#log-dropdown').change(create_chart);


function create_chart() {
    const context = canvas.getContext('2d');

    context.clearRect(0, 0, canvas.width, canvas.height);
    value = $('#log-dropdown').val();
    $.get(`/logs/${value}`, (data) => {

        if ($.trim(data)) {
            jsonfile = JSON.parse(data);

            // var labels = jsonfile.entries.map(function (e) {
            //     return e.time;
            // });
            // var data = jsonfile.entries.map(function (e) {
            //     return e.violations;
            // });

            const grouping = _.groupBy(jsonfile.violations, element => element.time.substring(0, unit_map[unit].substring))
            let sections
            if(unit == 'ten-minutes'){
                sections = _.map(grouping, (items, date) => ({
                    date: date + '0',
                    alerts: items.length
                }));
            }
            else{
                sections = _.map(grouping, (items, date) => ({
                    date: date,
                    alerts: items.length
                }));
            }
            

            x_values = sections.map(x => x.date)
            y_values = sections.map(x => x.alerts)

            if(!x_values[0]) x_values[0] = 'total'
            console.log(x_values)
            console.log(y_values)


            var ctx = canvas.getContext('2d');
            var config = {
                type: 'line',
                data: {
                    labels: x_values,
                    datasets: [{
                        label: 'Violations',
                        data: y_values,
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
                                unit: unit_map[unit].unit,
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
                    },
                    elements: {
                        line: {
                            tension: 0 // disables bezier curves
                        }
                    },
                }

            };
            if (typeof (chart) != "undefined") {
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
            if (typeof (chart) != "undefined") {
                chart.destroy();
            }
            chart = new Chart(ctx, config);
            chart.update();
        }


    });
}