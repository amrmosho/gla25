/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_py_chart {
    options = {};
    constructor(o) {
        this.options = o;
    }



    _chart_geochart(options = {}, type = "") {

        var d = eval(this.options["j"])
        var id = this.options.o._getAttribute("id")

        google.charts.load('current', {
            'packages': ['geochart'], // Note: Because markers require geocoding, you'll need a mapsApiKey.
            // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings

            'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
        });
        google.charts.setOnLoadCallback(drawRegionsMapa);

        function drawRegionsMapa() {


            var data = google.visualization.arrayToDataTable(d);
            var chart = new google.visualization.GeoChart(document.getElementById(id));
            chart.draw(data, options);
        }

    }


    _chart_orgchart(options = {}, type = "") {

        options["allowHtml"] = true



        var d = eval(this.options["j"])

        var id = this.options.o._getAttribute("id")



        google.charts.load('current', { packages: ["orgchart"] });
        google.charts.setOnLoadCallback(drawChart2);

        function drawChart2() {
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Name');
            data.addColumn('string', 'Manager');
            data.addColumn('string', 'ToolTip');

            data.addRows(d);


            // Create the chart.
            var chart = new google.visualization.OrgChart(document.getElementById(id));
            // Draw the chart, setting the allowHtml option to true for the tooltips.
            chart.draw(data, options);



        }

    }

    _chart(options = {}, type = "") {

        var d = eval(this.options["j"])

        var id = this.options.o._getAttribute("id")


        google.charts.load("current", { packages: ['corechart'] });
        google.charts.setOnLoadCallback(drawChart);

        function drawChart() {

            if (type == "candles") {
                var data = google.visualization.arrayToDataTable(d, true);
            } else {

                var data = google.visualization.arrayToDataTable(d);

            }

            var view = new google.visualization.DataView(data);

            if (type == "pie") {
                var chart = new google.visualization.PieChart(document.getElementById(id));
            } else if (type == "bar") {
                var chart = new google.visualization.BarChart(document.getElementById(id));

            } else if (type == "line") {
                var chart = new google.visualization.LineChart(document.getElementById(id));

            } else if (type == "area") {
                var chart = new google.visualization.AreaChart(document.getElementById(id));
            } else if (type == "stepped_area") {
                var chart = new google.visualization.SteppedAreaChart(document.getElementById(id));


            } else if (type == "candles") {

                var chart = new google.visualization.CandlestickChart(document.getElementById(id));

            } else if (type == "scatter") {


                var chart = new google.visualization.ScatterChart(document.getElementById(id));

            } else if (type == "bubble") {


                var chart = new google.visualization.BubbleChart(document.getElementById(id));





            } else {
                var chart = new google.visualization.ColumnChart(document.getElementById(id));
            }

            chart.draw(view, options);

        }

    }
    _out() {
        var op = {};

        if (this.options["ops"] != "") {
            op = this.options["ops"]

            op = op.replace(/'/g, '"');


            op = JSON.parse(op);
        }
        var t = this;

        ins("https://www.gstatic.com/charts/loader.js")._onload(function() {


            if (t.options["type"] == "org") {

                t._chart_orgchart(op, t.options["type"]);

            } else if (t.options["type"] == "geo") {

                t._chart_geochart(op, t.options["type"]);



            } else {

                t._chart(op, t.options["type"]);


            }
        });

    }
}