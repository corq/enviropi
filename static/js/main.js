$(document).ready(function() {
        Highcharts.setOptions({ global: {useUTC: false}});
        $(chart_id).highcharts({
                chart: chart,
                title: title,
                xAxis: xAxis,
                yAxis: yAxis,
                series: series
        });
});
