from ins_kit._engine._bp import App


class AppTest(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def test(self):
        return self.ins._server._req()

    def _key(self):
        v = "123"
        return v

    def ui(self):
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
                    "three/examples/jsm/webxr/ARButton.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/webxr/ARButton.js",
                                      "three/examples/jsm/shaders/FXAAShader.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/shaders/FXAAShader.js"
                    }
                }
            </script>
              <div id="loaderOverlay">Loading...</div>
            <link rel="stylesheet" crossorigin="anonymous" href="/ins_web/ins_apps/app_test/insv.css">
                   <div id='insv-text-btns' class="insv-flex" > </div>
            <div id="annotations" style="position: absolute; top: 0; left: 0; pointer-events: none;"></div>
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
               <span id="arBtn"  title='Settings'  style='background-image: url(/ins_web/ins_images/icons/insv_ar.svg);'></span>
            <span id="vrBtn" title='Helap'  style='background-image: url(/ins_web/ins_images/icons/insv_vr.svg);'></span>
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

    def epanel_lighting_color(self):

        b = """
         <div class="ins-col-12"><input type="color" class="ins-col-12" id="insv-ebackground-color" name="favcolor" value="#ff0000"></div>"""

        return b

    def epanel_lighting_env(self):

        b = """ <div  class='range_inut ins-col-12 ins-flex'>
        <label class='ins-col-grow'>envIntensity</label>

        <span>0</span>
        <input type="range" class="ins-col-12"  id="envBlur" value="0" min="0" max="0.1" step="0.001">
        </div>"""

        return b

    def epanel_lighting_image(self):

        b = """img"""

        return b

    def epanel_lighting(self):
        b = """<div  class='ins-flex ins-col-12'>
         <button data-m='color'  class='insv-background-btn  color ins-active ins-col-4 ins-button'>Color</button>
        <button   data-m='image'  class='insv-background-btn  image ins-col-4 ins-button' >Image</button>
        <button  data-m='env'  class='insv-background-btn env ins-col-4 ins-button'  >HDR</button>
        </div><div id="insv-epanel-background-body" class="ins-col-12 ins-flex"></div>"""
        r = ""

        l = """
<select  class='ins-col-12' id="lightingPreset">
  <option value="none">none</option>

  <option value="threePoint">Three-Point</option>
  <option value="lowKey">Low Key</option>
  <option value="moonlight">Full Moon Night</option>
  <option value="evil">Evil Genius</option>
  <option value="fairy">Fairy Camp</option>
</select>

<div id="lightControls"></div>


"""

        r += self.cart("Lighting Persets", l)

        s = """        
         <label>Shadow Intensity</label>
  <input type="range" id="shadowIntensity" min="0" max="2" step="0.1" value="1">

  <label>Shadow Softness (Radius)</label>
  <input type="range" id="shadowRadius" min="0" max="10" step="0.1" value="1">

  <label>Shadow Bias (Height Offset)</label>
  <input type="range" id="shadowBias" min="-0.05" max="0.05" step="0.001" value="0">

  <label>Shadow Map Size</label>
  <select id="shadowSize">
    <option value="512">512</option>
    <option value="1024" selected>1024</option>
    <option value="2048">2048</option>
    <option value="4096">4096</option>
  </select>
        """

        e = """ 
 

          <select class='ins-col-12' id="envList">
          <option value='christmas_photo_studio_06_1k'>christmas_photo_studio</option>
          <option value='christmas_photo_studio_07_1k'>christmas_photo_studio</option>
          <option value='studio_small_08_1k'>studio_small</option>
          <option value='voortrekker_interior_1k'>voortrekker_interior</option>
          </select>
       
               <img id="envListTH" class='ins-col-12' src='' />

       
       
        <div  class='range_inut ins-col-12 ins-flex'>
        <label class='ins-col-grow'>envIntensity</label>

        <span>0.5</span>
        <input type="range" class="ins-col-12"  id="envIntensity" value="0" min="0" max="20" step="0.01">
        </div>
        
        <div  class='range_inut ins-col-12 ins-flex'>
                  <label class='ins-col-grow'>EnvMap Rotation </label>

        <span>0.5</span>
        <input type="range" class="ins-col-12"  id="envRotation" value="0" min="0" max="360" step="1">
        
          </div>
        """

        r += self.cart("Envroment", e)
        r += self.cart("BackGround", b)
        r += self.cart("Shadows",  s)

        return r

    def epanel_post(self):

        r = ""

        s = """
            <input type="checkbox" id="enableBloom"  />
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> bloomStrength </label>
            <span>0.5</span>  
            <input type="range"    class="ins-col-12 postRangeInput"  data-p='noiseIntensity'   id="bloomStrength" value="1.0" min="0" max="3" step="0.05">
            </div>
        
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> bloomRadius </label>
            <span>0.5</span>  
            <input type="range"   class="ins-col-12 postRangeInput"  data-p='bloomRadius'   id="bloomRadius" value="0.4" min="0" max="1" step="0.01">
            </div>
         
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> bloomThreshold </label>
            <span> 0.85</span>  
            <input type="range"    class="ins-col-12 postRangeInput" data-p='scanlinesCount'  id="bloomThreshold" value="0.85" min="0" max="1.0" step="0.01">
            </div>    
            """
        r += self.cart("Bloom",  s)

        s = """
            <input type="checkbox" id="enableVignette" />
           
        
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> vignetteOffset </label>
            <span>0.5</span>  
            <input type="range"   class="ins-col-12 postRangeInput"    id="vignetteOffset" value="0.5" min="0.3" max="0.7" step="0.01">
            </div>
         
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> vignetteDarkness </label>
            <span>0.5</span>  
            <input type="range"    class="ins-col-12 postRangeInput"  id="vignetteDarkness" value="0.6" min="0" max="1" step="0.05>
            </div>    
            """
        r += self.cart("Vignette",  s)

        s = """
            <input type="checkbox" id="enableFilm"  />
            <div  class='ins-col-12 ins-flex'>
            <input type="checkbox" id="enableGrayFilm"  /> <span> grayscale </span>
            </div>

        
        
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> filmNoise </label>
            <span>0.5</span>  
            <input type="range"   class="ins-col-12 postRangeInput"    id="filmNoise"  min="0" max="1" step="0.01" value="1" />
            </div>
         
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> filmScanlines </label>
            <span>0.5</span>  
            <input type="range"    class="ins-col-12 postRangeInput"  id="filmScanlines" min="0" max="1" step="0.01" value="1" />
         
            </div>    
            
            <!--
              <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> filmScanlines </label>
            <span>0.5</span>  
            <input type="range"    class="ins-col-12 postRangeInput"  id="filmScanlines" min="64" max="4096" step="1" value="1024" />
         
         
         
            </div>  -->
            """
        r += self.cart("Film",  s)

        s = """
            <input type="checkbox" id="enableChroma"  />
      

        
        
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> Chromatic Offset X </label>
            <span>0.5</span>  
            <input type="range"  class="ins-col-12 postRangeInput"    id="chromaOffsetX"  min="0" max="0.01" step="0.001" />
            </div>
         
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> Chromatic Offset Y </label>
            <span>0.5</span>  
            <input type="range"   class="ins-col-12 postRangeInput"  id="chromaOffsetY" min="0" max="0.01" step="0.001"  />
         
            </div>    
       
            """
        r += self.cart("chromatic Aberration",  s)

        s = """
              <input type="checkbox" id="enableColorBalance" />
<div class='ins-flex ins-col-12' id="colorBalanceControls">


    <div  data-p="shadows" style="padding: 2px;text-align: center;font-size: 12px;" class="ins-col-4  ins-button cbitem-btn ">Shadows</div>
    <div data-p="midtones" style="padding: 2px;text-align: center;font-size: 12px;" class="ins-col-4  ins-active ins-button cbitem-btn">Midtones</div>
    <div  data-p="highlights"   style="padding: 2px;text-align: center;font-size: 12px;"  class="ins-col-4 ins-button cbitem-btn">Highlights</div>
    
    
    <div class='ins-col-12 ins-flex shadows ins-hidden  cbitem-tab-body'>
        <div class='range_inut ins-col-12 ins-flex'>
            R: <input id="shadowsR" type="range" min="0" max="2" step="0.01" value="1"> <span>0.5</span>
        </div>
        <div class='range_inut ins-col-12 ins-flex'>
            G: <input id="shadowsG" type="range" min="0" max="2" step="0.01" value="1"> <span>0.5</span>
        </div>
        <div class='range_inut ins-col-12 ins-flex'>
            B: <input id="shadowsB" type="range" min="0" max="2" step="0.01" value="1"><span>0.5</span>
        </div>
    </div>
    <div class='ins-col-12 ins-flex midtones   cbitem-tab-body'>
        <div class='range_inut ins-col-12 ins-flex'>
            R: <input id="midtonesR" type="range" min="0" max="2" step="0.01" value="1"><span>0.5</span>
        </div>
        <div class='range_inut ins-col-12 ins-flex'>
            G: <input id="midtonesG" type="range" min="0" max="2" step="0.01" value="1"><span>0.5</span>
        </div>
        <div class='range_inut ins-col-12 ins-flex'>
            B: <input id="midtonesB" type="range" min="0" max="2" step="0.01" value="1"> <span>0.5</span>
        </div>
    </div>
    <div class='ins-col-12 ins-flex ins-hidden  highlights  cbitem-tab-body'>
        <div class='range_inut ins-col-12 ins-flex'>
          h  R: <input id="highlightsR" type="range" min="0" max="2" step="0.01" value="1"> <span>0.5</span>
        </div>
        <div class='range_inut ins-col-12 ins-flex'>
            G: <input id="highlightsG" type="range" min="0" max="2" step="0.01" value="1"> <span>0.5</span>
        </div>
        <div class='range_inut ins-col-12 ins-flex'>
            B: <input id="highlightsB" type="range" min="0" max="2" step="0.01" value="1"> <span>0.5</span>
        </div>
    </div>
</div>
       
            """
        r += self.cart("chromatic Aberration",  s)


        s = """
            <input type="checkbox" id="enableSharpen"  />
      

        
        
            <div  class='range_inut ins-col-12 ins-flex'>
            <label class='ins-col-grow'> sharpens Strength </label>
            <span>0.5</span>  
            <input type="range"  class="ins-col-12 postRangeInput"    id="sharpensStrength" min="0" max="2" step="0.01" value="0.3" />
            </div>
         
               
       
            """
        r += self.cart("Sharpen",  s)






        return r

    def epanel_mats(self):
        return "epanel_mats"

    def cart(self, title, data):
        a = "<div class='ins-card ins-col-12 ins-flex'>"
        a += f"<div class='insv-title ins-col-12 ins-flex'><span class='ins-col-grow'>{title}</span><i  class='ins-title-icon' style='background-image: url(/ins_web/ins_images/icons/question-mark-circle.svg);'></i></div>"
        a += data
        a += "</div> "

        return a

    def update_data(self):
        r = self.ins._server._post("data")

        r = self.ins._json._decode(r)
        path: str = r["path"]
        path = path.replace("/ins_web", "ins_web")
        self.ins._json._file_write(path, r)
        return r

    def epanel_settins(self):

        c = """
        
        <div id="transformInfo" class="ins-col-12 ins-flex">
  <label class='ins-col-12'>Position</label>
  <input id="posX" type="number" class="ins-col-4 ins-input" step="0.01"> 
  <input id="posY" type="number" class="ins-col-4 ins-input" step="0.01"> 
  <input id="posZ" type="number" class="ins-col-4 ins-input" step="0.01">

  <label class='ins-col-12'>Rotation</label>
  <input id="rotX" type="number" class="ins-col-4 ins-input" step="0.01"> 
  <input id="rotY" type="number" class="ins-col-4 ins-input" step="0.01"> 
  <input id="rotZ" type="number" class="ins-col-4 ins-input" step="0.01">

  <label class='ins-col-12'>Scale</label>
  <input id="scaleX" type="number" class="ins-col-4 ins-input" step="0.01"> 
  <input id="scaleY" type="number" class="ins-col-4 ins-input" step="0.01"> 
  <input id="scaleZ" type="number" class="ins-col-4 ins-input" step="0.01">
</div>
        
        
        <div  class='ins-flex ins-col-12'><button data-m='translate'  class='insv-translate-btn ins-active ins-col-4 ins-button'>Move</button>
<button   data-m='rotate'  class='insv-translate-btn ins-col-4 ins-button' >Rotate</button>
<button  data-m='scale'  class='insv-translate-btn ins-col-4 ins-button'  >Scale</button></div>"""

        a = """
        
        <div id="cameraControls"  class="ins-col-12 ins-flex">
  <label  class='ins-col-4'> FOV</label>
    <label  class='ins-col-4'>Near Clip</label>
    <label  class='ins-col-4'>Far Clip</label>
  
  <input class="ins-col-4 ins-input"  id="camFOV" type="number" step="0.1" min="10" max="150">



  <input class="ins-col-4 ins-input" step="0.01" id="camNear" type="number" step="0.01">

  <input class="ins-col-4 ins-input" step="0.01"  id="camFar" type="number" step="1">

  <label  class='ins-col-12'>Position</label>
  <input class="ins-col-4 ins-input" step="0.01" id="camPosX" type="number" step="0.1">
  <input class="ins-col-4 ins-input" step="0.01" id="camPosY" type="number" step="0.1">
  <input class="ins-col-4 ins-input" step="0.01" id="camPosZ" type="number" step="0.1">
  
  
  
  <label class='ins-col-12'>Rotation (deg)</label>
<input  class="ins-col-4 ins-input" id="camRotX" type="number" step="1">
<input class="ins-col-4 ins-input" id="camRotY" type="number" step="1">
<input  class="ins-col-4 ins-input"  id="camRotZ" type="number" step="1">
  
</div>
        
        
        """

        r = self.cart("Camera", a)
        r += self.cart("Translatetion", c)

        return r

    def eui(self):
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
                    "three/examples/jsm/webxr/ARButton.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/webxr/ARButton.js",
                    "three/examples/jsm/shaders/FXAAShader.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/shaders/FXAAShader.js",
                                       "three/examples/jsm/controls/TransformControls.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/controls/TransformControls.js",
                    "three/examples/jsm/loaders/RGBELoader.js": "https://cdn.jsdelivr.net/npm/three@0.154.0/examples/jsm/loaders/RGBELoader.js"

                 
                    }
                }
            </script>
            
      
              <div id="loaderOverlay">Loading...</div>
              

            <div style="    right: 8px;
    width: 280px; left: auto;top: 20px;bottom: auto;padding: 6px; background: #eee" class='insv ins-panel ins-flex' >
          
                                    <span class="insv-get-epanel active"  data-p='epanel_settins'    title='Settings'  style='background-image: url(/ins_web/ins_images/icons/gear-1.svg);'></span>

          
            <span  title='Full Screen'   class="insv-get-epanel"  data-p='epanel_lighting'        style='background-image: url(/ins_web/ins_images/icons/insv_lighting.svg);'></span>
           
           
            <span   title='Full Screen'   class="insv-get-epanel"  data-p='epanel_post'       style='background-image: url(/ins_web/ins_images/icons/camera-1.svg);'></span>
            <span class="insv-get-epanel"  title='Material' data-p='epanel_mats' style='background-image: url(/ins_web/ins_images/icons/search.svg);'> </span>
            <span class="insv-get-epanel"  title='Controlller' data-p='epanel_lighting' style='background-image:url(/ins_web/ins_images/icons/insv_controllaer.svg);'></span>
            <span title='Helap'  style='background-image: url(/ins_web/ins_images/icons/question-mark-circle.svg);'></span>
            </div>
            
                        <div class='ins-flex'  id="insv-epanel-body"  >
sdfsd
                        </div>

            
            

              
              <div id="insv-body">
            <link rel="stylesheet" crossorigin="anonymous" href="/ins_web/ins_apps/app_test/insv.css">
                   <div id='insv-text-btns' class="insv-flex" > </div>
            <div id="annotations" style="position: absolute; top: 0; left: 0; pointer-events: none;"></div>
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
            <span id="arBtn"  title='Settings'  style='background-image: url(/ins_web/ins_images/icons/insv_ar.svg);'></span>
            <span id="vrBtn" title='Helap'  style='background-image: url(/ins_web/ins_images/icons/insv_vr.svg);'></span>
            <span id="arBtn"  title='Settings'  style='background-image: url(/ins_web/ins_images/icons/gear-1.svg);'></span>
            <span id="vrBtn" title='Helap'  style='background-image: url(/ins_web/ins_images/icons/question-mark-circle.svg);'></span>
            </div>
                <div id='insvAnimationCont'  class='insv-animation-cont insv-flex ins-panel'>
                    <input type="range" id="animProgress" value="0" min="0" max="1" step="0.001">
                    <div style="width:100%"></div>
                              <span id="playAnimBtn" title='Play' class='insv-icon_btn active' style=''></span>
  <select id="animList"></select>
  
  
</div></div>
                            <div class="insv-footer">

                            <div id="insv-update-btn" class="ins-button">Update</div>
</div>
<script    src="/ins_web/ins_apps/app_test/insv_actions.js"></script>
                 <script   type="module" src="/ins_web/ins_apps/app_test/v_editor.js"></script>
             """
        return aaaa

    def out(self):
        return self.eui()
