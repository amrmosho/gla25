/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_map {
    options = {};
    constructor(o) {
        this.options = o;
    }



     _get_location (options) {
        /* function error(err) {
        alert(`Failed to locate. Error: ${err.message}`)
      } 
    
      function success(pos) {
    
        alert(`${pos.coords.latitude}, ${pos.coords.longitude}`);
      }
    */
        //function getGeolocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(options.ondone, options.onerror);
        }
        // }
    };
    
_map(options) {
        var o = this.o;
        var script = document.createElement("script");
        script.src =
            "https://maps.googleapis.com/maps/api/js?key=AIzaSyCIAWRMS-am-n_Q2wkNjFWFjB_iIIchPOU&callback=initMap";
        script.defer = true;
    
        options.center = options.center ?
            options.center : {
                lat: 37.772,
                lng: -122.214,
            };
    
        options.zoom = options.zoom ? options.zoom : 8;
    
        function markers(map, data) {
            var ms = [];
            data.forEach(function(a) {
                var marker = new google.maps.Marker({
                    position: a,
                    title: a.title,
                    map: map,
                });
    
                marker.set;
    
                if (options.onaddmarker != null) {
                    options.onaddmarker(map, marker);
                }
    
                ms.push(marker);
            });
            return ms;
        }
    
        function path(map, path) {
            var flightPath = new google.maps.Polyline({
                path: path.data,
                geodesic: true,
                strokeColor: path.color ? path.color : "#FF0000",
                strokeOpacity: path.opacity ? path.opacity : 1.0,
                strokeWeight: path.weight ? path.weight : 2,
            });
    
            flightPath.setMap(map);
    
            return flightPath;
        }
    
        window.initMap = function() {
            var map = new google.maps.Map(document.querySelector(o), {
                zoom: options.zoom,
                center: options.center,
            });
    
            var ms = options.markers ? markers(map, options.markers) : false;
            var p = options.path ? path(map, options.path) : false;
    
            if (options.onload != null) {
                options.onload(map, ms, p);
            }
        };
    
        document.head.appendChild(script);
    };



    _out() {}
}