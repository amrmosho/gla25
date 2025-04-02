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



    _chart(options = {}, type = "") {

        var d = eval(this.options["j"])

        var id = this.options.o._getAttribute("id")


        ins("https://www.gstatic.com/charts/loader.js")._onload(function() {

            google.charts.load("current", { packages: ['corechart'] });
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {
                var data = google.visualization.arrayToDataTable(d);
                var view = new google.visualization.DataView(data);

                if (type == "pie") {
                    var chart = new google.visualization.PieChart(document.getElementById(id));
                } else if (type == "bar") {
                    var chart = new google.visualization.BarChart(document.getElementById(id));;

                } else if (type == "line") {
                    var chart = new google.visualization.LineChart(document.getElementById(id));;





                } else {
                    var chart = new google.visualization.ColumnChart(document.getElementById(id));
                }

                chart.draw(view, options);

            }
        });

    }
    _out() {

        this._chart({ legend: { position: "none" } }, this.options["type"]);


    }
}