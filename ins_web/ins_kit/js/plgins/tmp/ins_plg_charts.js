/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_charts {
    options = {};
    constructor(options) {
        this.options = options;
    }
    o = null;
    /*
    chart: {
          events: {
            animationEnd: undefined,
            beforeMount: undefined,
            mounted: undefined,
            updated: undefined,
            mouseMove: undefined,
            mouseLeave: undefined,
            click: undefined,
            legendClick: undefined,
            markerClick: undefined,
            selection: undefined,
            dataPointSelection: undefined,
            dataPointMouseEnter: undefined,
            dataPointMouseLeave: undefined,
            beforeZoom: undefined,
            beforeResetZoom: undefined,
            zoomed: undefined,
            scrolled: undefined,
            scrolled: undefined,
          }
      }
    */
    _run() {
        var t = this;
        t.options.height = (t.options.height == null) ? 350 : t.options.height;
        var colors = ["#85c67d", '#0398e2', "#797bf2", "#75609f", "#ffa880", "#535A6C", "#ffa880"]; //["#d4526e", '#ff9800', "#85c67d", "#75609f", "#ffa880", "#535A6C", "#ffa880"]
        t.options.colors = (t.options.colors == null) ? colors : t.options.colors;
        var style = {
            mode: 'dark',
            foreColor: '#6c6c75',
            red: "#d4526e",
            green: "#85c67d",
            yellow: "#ff9800",
            colors: t.options.colors
        }
        var defOptions = t.options;
        defOptions.series = t.options.data;
        defOptions.tooltip = {
            theme: style.mode,
        };
        if (t.options.width != null) {
            defOptions.chart.width = t.options.width;
        }
        if (t.options.chart != null) {
            defOptions.chart = t.options.chart;
        } else {
            defOptions.chart = {
                foreColor: style.foreColor,
                height: t.options.height,
                type: t.options.type,
            };
        }
        defOptions.responsive = [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }];
        this._get_chart(defOptions);
    }
    _get_chart(defOptions) {
        this._render(defOptions);
    }
    _render(options) {
        var t = this;
        // ins(function() {
        if (ins(t.options.o)._isExists(true)) {
            ins(t.options.o)._sethtml("");
            var chart = new ApexCharts(document.querySelector(t.options.o), options);
            chart.render();
            if (t.options["time"]) {
                if (t.options["time"]["time"]) {
                    t.updateTime(chart);
                }
            }
        }
    }
    updateTime(chart) {
        var t = this;
        window.setInterval(function() {
                var v = [];
                if (t.options["time"]["data"] != null) {
                    if (t.options["type"] == "radar") {
                        console.log(t.options["time"]["data"]);
                    }
                    t.options["time"]["data"].forEach(function(mv, i) {
                        if (mv["from"] != null) {
                            var vd = [];
                            mv["from"].forEach(function(fmv, i) {
                                var m = t.generateRandom(fmv, mv["to"][i]);
                                vd.push(m)
                            });
                            t.options["time"]["data"][i]["data"] = vd;
                        }
                    });
                    v = t.options["time"]["data"];
                } else if (Array.isArray(t.options["time"]["from"])) {
                    var vd = [];
                    t.options["time"]["from"].forEach(function(mv, i) {
                        var m = t.generateRandom(mv, t.options["time"]["to"][i]);
                        vd.push(m)
                        v = [{
                            data: vd,
                        }];
                    })
                } else {
                    var m = t.generateRandom(t.options["time"]["from"], t.options["time"]["to"])
                    v.push(m)
                }
                chart.updateSeries(v)
            },
            t.options["time"]["time"])
    }
    generateRandom(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
    ondone;
    _out() {
        var t = this;




        if (this.options["data"] != null) {
            var c = this.options["data"];

            this.options = {
                ...this.options,
                ...c
            };

        } else if (this.options["chart_data"] != "") {
            var c = JSON.parse(this.options["chart_data"]);
            this.options = {
                ...this.options,
                ...c
            };
        }
        console.log(this.options);
        ins("/ins_lib/css/ins_charts.css")._insclude_css(function() {
            ins("https://cdn.jsdelivr.net/npm/apexcharts")._onload(function() {
                ins("https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/moment.min.js")._onload(function() {
                    var c = t._run();
                    if (t.onload != null) {
                        t.onload(c);
                    }
                });
            });
        });
    }
}