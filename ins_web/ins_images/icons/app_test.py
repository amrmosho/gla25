
from ins_kit._engine._bp import App


class AppTest(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def test(self):
        return self.ins._server._req()

    def _key(self):
        
        v= "123"
        
        return  v



    def out(self):

        aaaa = """ 
        <script type="importmap">
                {
                "imports": {
                    "three": "https://cdn.jsdelivr.net/npm/three@0.154.0/build/three.module.js",
                    "three/examples/jsm/controls/OrbitControls.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/controls/OrbitControls.js",
                    "three/examples/jsm/loaders/FBXLoader.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/loaders/FBXLoader.js",
                    "three/examples/jsm/loaders/EXRLoader.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/loaders/EXRLoader.js",
                    "three/src/extras/PMREMGenerator.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/src/extras/PMREMGenerator.js",               
                    "three/examples/jsm/postprocessing/EffectComposer.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/postprocessing/EffectComposer.js",
                    "three/examples/jsm/postprocessing/RenderPass.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/postprocessing/RenderPass.js",
                    "three/examples/jsm/postprocessing/UnrealBloomPass.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/postprocessing/UnrealBloomPass.js",
                    "three/examples/jsm/postprocessing/FilmPass.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/postprocessing/FilmPass.js",
                    "three/examples/jsm/postprocessing/ShaderPass.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/postprocessing/ShaderPass.js",
                    "three/examples/jsm/shaders/GammaCorrectionShader.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/shaders/GammaCorrectionShader.js",
                    "three/examples/jsm/shaders/ConvolutionShader.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/shaders/ConvolutionShader.js",
                    "three/examples/jsm/webxr/ARButton.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/webxr/ARButton.js"

                  
                  
                  
                  
                  
                    }
                }
            </script>
            
            
            <link rel="stylesheet" crossorigin="anonymous" href="/ins_web/ins_apps/app_test/insv.css">
       
       
                   <div id='insv-text-btns' class="insv-flex" > </div>




            <div class='-insv-side-panel ins-hidden control ins-flex' >
            <div id="rotateBtn_up"    style='width:100%;'><span  style='background-image: url(/ins_web/ins_images/icons/arrow-upward.svg);'></span> </div>
            <div id="rerotateBtn"  data-rend='metal'   style=';'><span  style='background-image: url(/ins_web/ins_images/icons/arrow-left.svg);'></span> </div>
            <div id="centerBtn"  data-rend='color'   > <span  style='background-image: url(/ins_web/ins_images/icons/expand-arrow-1.svg);'></span>  </div>
             <div id="rotateBtn"   ><span  style='background-image: url(/ins_web/ins_images/icons/arrow-right.svg);'></span> </div>
             <div id="rotateBtn_down"   style='width:100%;'><span  style='background-image: url(/ins_web/ins_images/icons/arrow-downward.svg)'></span> </div>
            </div>

            <div class='-insv-side-panel material ins-hidden ins-flex' >
            <div class="-rend-btn fitem active"   data-rend='final'><span  style='background-image: url(/ins_web/ins_images/icons/insv_render.svg);'></span>  Final Render</div>
            <div class="-rend-btn fitem"  data-rend='color'> <span  style='background-image: url(/ins_web/ins_images/icons/insv_wcolor.svg);'></span> Base Color </div>
            <div class="-rend-btn fitem"  data-rend='metal'><span  style='background-image: url(/ins_web/ins_images/icons/insv_metalness.svg);'></span> Metalness</div>
            <div class="-rend-btn fitem"  data-rend='rough'><span  style='background-image: url(/ins_web/ins_images/icons/insv_roughness.svg);'></span> Roughness</div>
            <div class="-rend-btn fitem"  data-rend='normal'><span  style='background-image: url(/ins_web/ins_images/icons/ins_normal.svg);'></span> Normal Map</div>
            <div class="-rend-btn fitem" data-rend='wire'> <span  style='background-image: url(/ins_web/ins_images/icons/insv_wireframe.svg);'></span>Wire Frame</div>
            </div>
                
            <div class='insv ins-panel ins-flex' >
            <span id="fullscreenBtn" title='Full Screen' style='background-image: url(/ins_web/ins_images/icons/expand-square-4.svg);'></span>
            <span id="screenshotBtn" title='Screen Shot'   style='background-image: url(/ins_web/ins_images/icons/camera-1.svg);'></span>
            <span class="-view-panel"  title='Material' data-p='material' style='background-image: url(/ins_web/ins_images/icons/search.svg);'> </span>
            <span class="-view-panel"  title='Controlller' data-p='control' style='background-image:url(/ins_web/ins_images/icons/insv_controllaer.svg);'></span>
            <span id="arBtn"  title='Settings'  style='background-image: url(/ins_web/ins_images/icons/gear-1.svg);'></span>
            <span id="vrBtn" title='Helap'  style='background-image: url(/ins_web/ins_images/icons/question-mark-circle.svg);'></span>
            </div>
                
                
                <div id='insvAnimationCont'  class='insv-animation-cont insv-flex ins-panel'>
                
                

                
                    <input type="range" id="animProgress" value="0" min="0" max="1" step="0.001">
                    <div style="width:100%"></div>
                              <span id="playAnimBtn" title='Play' class='insv-icon_btn active' style=''></span>

  <select id="animList"></select>
  

  

</div>
                 <script   type="module" src="/ins_web/ins_apps/app_test/v.js"></script>
             """

        return aaaa
