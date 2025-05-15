import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { FilmPass } from 'three/examples/jsm/postprocessing/FilmPass.js';
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass.js';
import { ConvolutionShader } from 'three/examples/jsm/shaders/ConvolutionShader.js';
import { GammaCorrectionShader } from 'three/examples/jsm/shaders/GammaCorrectionShader.js';



import { EXRLoader } from 'three/examples/jsm/loaders/EXRLoader.js';

var _send = function (url, options, callback, onprogress, type = "POST") {



    type = type == null ? "POST" : type;
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {


        if (this.readyState == 4 && this.status == 200) {
            if (callback != null) {
                callback(this.responseText, this);
            }
        } else if (this.readyState == 4) {
            if (callback != null) {

                callback(false);
            }
            console.error("inserror: code(" + this.status + ")\n call url want error\nurl:(" + url + ")\n options:");
            console.error(options);
        }
    };
    xhttp.upload.onprogress = function (e) {
        if (e.lengthComputable) {

        }
    };
    var fd = new FormData();
    try {

        if (options instanceof FormData) {
            fd = options;
        } else if (typeof options === "string") {
            url += "?" + options;
        } else {
            Object.keys(options).forEach(function (k) {
                if (type === "POST") {
                    fd.append(k, options[k]);
                } else {
                    if (url.indexOf("?") == -1) {
                        url += "?";
                    }
                    url += "&" + k + "=" + options[k];
                }
            });
        }


        xhttp.open(type, url, true);
        xhttp.send(fd);
        return xhttp;
    } catch (e) {
        console.log(o);
    }
};






/**
 * ThreeScene class encapsulates the setup and rendering of a Three.js scene,
 * including model loading, lighting, and post-processing effects.
 */
export class ThreeScene {
    /**
     * Constructs the ThreeScene instance.
     * @param {Object} config - Configuration object for the scene.
     */
    constructor(config) {
        this.config = config;
        this.scene = new THREE.Scene();


        const cam = config.camera;
        this.camera = new THREE.PerspectiveCamera(
            cam.fov,
            window.innerWidth / window.innerHeight,
            cam.near,
            cam.far
        );
        this.camera.position.set(...cam.position);

        this.renderer = new THREE.WebGLRenderer({ antialias: true });

        this.composer = null;
        this.controls = null;
        this.modelRoot = null;
        this.targetRotationY = 0;

        this.targetRotationX = 0;

        this.animations = [];
        this.currentAction = null;
        // this.activeAction= THREE.AnimationAction


        this.cameraTargetPos = null;
        this.controlsTarget = null;
    }




    /**
     * Initializes the scene, including renderer, controls, lighting, model, and post-processing.
     */
    async init() {
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.outputEncoding = THREE.sRGBEncoding;
        document.body.appendChild(this.renderer.domElement);

        this.controls = new OrbitControls(this.camera, this.renderer.domElement);
        this.controls.target.set(0, 1, 0);
        this.controls.update(); this.mixer = null;
        this.clock = new THREE.Clock();

        console.log(this.config.background_color);
        this.scene.background = new THREE.Color(this.config.background_color);

        this.setupLighting();


        _send('/ins_ajax/home/app_test/_key/do/_area/home/_alias/test/', { userToken: 'abc123' },
            (k) => {
                this.decryptAndLoadFBX(this.config.obj, k, (blobURL) => {
                    this.loadModel(blobURL)
                });
            }

        );


        this.setupPostProcessing();
        this.setupUI();

        this.animate();

        window.addEventListener('resize', () => this.onResize());
    }

    /**
     * Sets up ambient and directional lighting based on the configuration.
     */
    setupLighting() {
        const { ambient, directional, lightmap } = this.config.lighting;

        this.scene.add(new THREE.AmbientLight(ambient.color, ambient.intensity));

        const dirLight = new THREE.DirectionalLight(directional.color, directional.intensity);
        dirLight.position.set(...directional.position);
        this.scene.add(dirLight);

        // Load EXR environment map if enabled
        if (lightmap?.enabled && lightmap.url) {
            const exrLoader = new EXRLoader();
            const pmrem = new THREE.PMREMGenerator(this.renderer);
            pmrem.compileEquirectangularShader();

            exrLoader.load(lightmap.url, (texture) => {
                const envMap = pmrem.fromEquirectangular(texture).texture;
                if (lightmap.applyAs === 'environment' || lightmap.applyAs === 'both') {
                    this.scene.environment = envMap;
                }
                if (lightmap.applyAs === 'background' || lightmap.applyAs === 'both') {
                    this.scene.background = envMap;
                }

                this.envMap = envMap; // Save for later use
                this.envIntensity = lightmap.intensity ?? 1;
                texture.dispose();
            });
        }
    }


    setupUI() {
        const bgColors = [0x1e1e1e, 0x004477, 0xffffff];
        let bgIndex = 0;

        var t = this;


        document.getElementById('animProgress')?.addEventListener('input', (e) => {
            if (this.currentAction && this.currentClip) {
                const percent = parseFloat(e.target.value);
                const newTime = percent * this.currentClip.duration;
                this.currentAction.time = newTime;
                this.mixer.setTime(newTime);
            }
        });
        document.getElementById('playAnimBtn')?.addEventListener('click', (e) => {


            if (e.target.classList.contains("active")) {
                e.target.classList.remove("active");

                if (this.currentAction) {
                    this.currentAction.stop();
                }



            } else {
                e.target.classList.add("active");

                const index = parseInt(document.getElementById('animList').value);
                this.playAnimation(index);
            }

        });



        document.getElementById('screenshotBtn')?.addEventListener('click', () => {
            // Render the scene to the composer render target
            this.composer.render();

            // Read pixels from the renderer's canvas
            const dataURL = this.renderer.domElement.toDataURL('image/png');

            // Trigger download
            const link = document.createElement('a');
            link.href = dataURL;
            link.download = 'scene-screenshot.png';
            link.click();
        });



        // Background color toggle?
        document.querySelectorAll('.-view-panel').forEach(element => {
            element.addEventListener("click", function (e) {
                var cl = e.target.dataset["p"];





                document.querySelectorAll('.-insv-side-panel').forEach(p => {


                    if (!p.classList.contains("ins-hidden")) {
                        p.classList.add("ins-hidden");
                    }

                });

                if (element.classList.contains("active")) {
                    element.classList.remove("active");


                } else {

                    document.querySelectorAll('.-insv-side-panel.' + cl).forEach(p => {
                        p.classList.remove("ins-hidden");

                    });
                    element.classList.add("active");

                }



            });
        });

        // Background color toggle?
        document.querySelectorAll('.-rend-btn').forEach(element => {
            element.addEventListener("click", function (e) {




                document.querySelectorAll('.-rend-btn').forEach(p => {
                    p.classList.remove("active");
                });
                element.classList.add("active");





                if (e.target.dataset["rend"] == "wire") {


                    if (t.obj.material.wireframe == true) {
                        t.obj.material.wireframe = false;
                    } else {
                        t.obj.material.wireframe = true;
                    }
                } else if (e.target.dataset["rend"] == "normal") {
                    t.mat_normal()
                    t.obj.material = t.material;

                } else if (e.target.dataset["rend"] == "metal") {
                    t.mat_metal()
                    t.obj.material = t.material;

                } else if (e.target.dataset["rend"] == "rough") {
                    t.mat_roughness()
                    t.obj.material = t.material;

                } else if (e.target.dataset["rend"] == "color") {
                    t.mat_color()
                    t.obj.material = t.material;

                } else if (e.target.dataset["rend"] == "final") {
                    t.mat()
                    console.log(t.material);
                    t.obj.material = t.material;

                }




                t.obj.material.needsUpdate = true;






            });
        });


        document.getElementById('fullscreenBtn')?.addEventListener('click', () => {
            const canvas = this.renderer.domElement;
            if (!document.fullscreenElement) {
                canvas.requestFullscreen?.() || canvas.webkitRequestFullscreen?.();
            } else {
                document.exitFullscreen?.() || document.webkitExitFullscreen?.();
            }
        });


        document.getElementById('rotateBtn')?.addEventListener('click', () => {
            this.targetRotationY += Math.PI / 2; // Add 90 degrees

        });
        document.getElementById('rerotateBtn')?.addEventListener('click', () => {
            this.targetRotationY -= Math.PI / 2; // Add 90 degrees

        });

        document.getElementById('rotateBtn_up')?.addEventListener('click', () => {
            this.targetRotationX += Math.PI / 2; // Add 90 degrees

        });
        document.getElementById('rotateBtn_down')?.addEventListener('click', () => {
            this.targetRotationX -= Math.PI / 2; // Add 90 degrees

        });







        // bgIndex = (bgIndex + 1) % bgColors.length;
        //this.scene.background = new THREE.Color(bgColors[bgIndex]);





        document.getElementById('centerBtn')?.addEventListener('click', () => {

            if (!this.modelRoot) return;

            const box = new THREE.Box3().setFromObject(this.modelRoot);
            const size = new THREE.Vector3();
            const center = new THREE.Vector3();
            box.getSize(size);
            box.getCenter(center);

            const maxDim = Math.max(size.x, size.y, size.z);
            const fov = this.camera.fov * (Math.PI / 180);
            const distance = maxDim / (2 * Math.tan(fov / 2.5)) * 1.2;

            const newCamPos = center.clone().add(new THREE.Vector3(0, 0, distance));
            this.cameraTargetPos = newCamPos;
            this.controlsTarget = center.clone();
        });
        // Toggle wireframe overlays by name
        document.getElementById('toggleWireBtn')?.addEventListener('click', () => {
            this.scene.traverse((child) => {
                if (child.isMesh && child.name.includes('_wireframe')) {
                    child.visible = !child.visible;
                }
            });
        });
    }




    mat_normal() {
        const loader = new THREE.TextureLoader();
        this.material = new THREE.MeshStandardMaterial({
            map: loader.load(this.config.textures.normal),
            normalMap: loader.load(this.config.textures.normal),
            metalness: 0,
            roughness: 1.0
        }); this.mat_update();

    }





    mat_color() {
        const loader = new THREE.TextureLoader();
        this.material = new THREE.MeshStandardMaterial({
            map: loader.load(this.config.textures.albedo),
            metalness: 0,
            roughness: 1.0
        }); this.mat_update();

    }


    mat_metal() {
        const loader = new THREE.TextureLoader();
        this.material = new THREE.MeshStandardMaterial({
            map: loader.load(this.config.textures.metallic),
            normalMap: loader.load(this.config.textures.normal),
            metalness: 0,
            roughness: 1.0
        }); this.mat_update();

    }



    mat_roughness() {
        const loader = new THREE.TextureLoader();
        this.material = new THREE.MeshStandardMaterial({
            map: loader.load(this.config.textures.roughness),
            metalness: 0,
            roughness: 1.0

        }); this.mat_update();

    }






    mat() {
        const loader = new THREE.TextureLoader();
        this.material = new THREE.MeshStandardMaterial({
            map: loader.load(this.config.textures.albedo),
            normalMap: loader.load(this.config.textures.normal),
            metalnessMap: loader.load(this.config.textures.metallic),
            roughnessMap: loader.load(this.config.textures.roughness),
            metalness: 1.0,
            roughness: 1.0
        });

        this.mat_update();


    }



    mat_update() {
        ['map', 'normalMap', 'metalnessMap', 'roughnessMap'].forEach((mapType) => {
            const map = this.material[mapType];
            if (map) {
                // map.flipY = false;
                if (mapType === 'map' || mapType === 'normalMap') {
                    map.encoding = THREE.sRGBEncoding;
                }
            }
        });
    }

    playAnimation(index) {
        if (!this.mixer || !this.animations.length) return;

        if (this.currentAction) {
            this.currentAction.stop();
        }

        const clip = this.animations[index];
        this.currentAction = this.mixer.clipAction(clip);
        this.currentAction.reset().play();

        this.currentClip = clip;
    }





    /**
     * Loads the FBX model and applies PBR textures as specified in the configuration.
     */
    loadModel(fbxUrl) {
        this.mat();
        const fbxLoader = new FBXLoader();
        fbxLoader.load(fbxUrl, (fbx) => {
            fbx.scale.set(0.1, 0.1, 0.1);


            ////FBX model Antions
            // Setup animation if available
            if (fbx.animations && fbx.animations.length) {
                this.animations = fbx.animations;
                this.mixer = new THREE.AnimationMixer(fbx);

                // Populate animation dropdown
                const list = document.getElementById('animList');
                list.innerHTML = ''; // Clear any existing options
                fbx.animations.forEach((clip, index) => {
                    const opt = document.createElement('option');
                    opt.value = index;
                    opt.textContent = clip.name || `Animation ${index + 1}`;
                    list.appendChild(opt);
                });

                // Auto-play first animation
                this.playAnimation(0);
            }


            fbx.traverse((child) => {
                if (child.isMesh) {
                    this.obj = child;

                    child.material = this.material;

                    if (this.config.wireframe) {
                        child.material.wireframe = true;
                    }

                    // Apply environment map and intensity
                    if (this.envMap) {
                        child.material.envMap = this.envMap;
                        child.material.envMapIntensity = this.envIntensity ?? 1;
                        child.material.needsUpdate = true;
                    }
                }
            });

            this.modelRoot = fbx;
            this.scene.add(this.modelRoot);
        });
    }

    /**
     * Sets up post-processing effects based on the configuration.
     */
    setupPostProcessing() {
        this.composer = new EffectComposer(this.renderer);
        this.composer.addPass(new RenderPass(this.scene, this.camera));

        const filters = this.config.filters;

        if (filters.bloom?.enabled) {
            const { strength, radius, threshold } = filters.bloom;
            const bloomPass = new UnrealBloomPass(
                new THREE.Vector2(window.innerWidth, window.innerHeight),
                strength,
                radius,
                threshold
            );
            this.composer.addPass(bloomPass);
        }

        if (filters.film?.enabled) {
            const { noiseIntensity, scanlinesIntensity, scanlinesCount } = filters.film;
            const filmPass = new FilmPass(noiseIntensity, scanlinesIntensity, scanlinesCount, false);
            this.composer.addPass(filmPass);
        }

        if (filters.sharpen?.enabled) {
            const sharpenPass = new ShaderPass(ConvolutionShader);
            sharpenPass.uniforms['uImageIncrement'].value = new THREE.Vector2(0, 0);
            sharpenPass.uniforms['cKernel'].value = filters.sharpen.kernel;
            this.composer.addPass(sharpenPass);
        }

        if (filters.gammaCorrection) {
            this.composer.addPass(new ShaderPass(GammaCorrectionShader));
        }








        if (filters.colorBalance?.enabled) {


            const ColorBalanceShader = {
                uniforms: {
                    tDiffuse: { value: null },
                    shadows: { value: new THREE.Vector3(1.0, 0.9, 0.9) },
                    midtones: { value: new THREE.Vector3(1.0, 1.0, 1.0) },
                    highlights: { value: new THREE.Vector3(1.1, 1.1, 1.2) }
                },
                vertexShader: `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
                fragmentShader: `
    uniform sampler2D tDiffuse;
    uniform vec3 shadows;
    uniform vec3 midtones;
    uniform vec3 highlights;
    varying vec2 vUv;

    void main() {
      vec4 color = texture2D(tDiffuse, vUv);
      float luminance = dot(color.rgb, vec3(0.2126, 0.7152, 0.0722));

      vec3 result = color.rgb;
      if (luminance < 0.33) {
        result *= shadows;
      } else if (luminance < 0.66) {
        result *= midtones;
      } else {
        result *= highlights;
      }

      gl_FragColor = vec4(result, color.a);
    }
  `
            };


            const pass = new ShaderPass(ColorBalanceShader);
            pass.uniforms.shadows.value = new THREE.Vector3(...filters.colorBalance.shadows);
            pass.uniforms.midtones.value = new THREE.Vector3(...filters.colorBalance.midtones);
            pass.uniforms.highlights.value = new THREE.Vector3(...filters.colorBalance.highlights);
            this.composer.addPass(pass);
        }



        if (filters.vignette?.enabled) {

            const VignetteShader = {
                uniforms: {
                    tDiffuse: { value: null },
                    offset: { value: 1.0 },
                    darkness: { value: 1.2 }
                },






                vertexShader: `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
                fragmentShader: `
    uniform sampler2D tDiffuse;
    uniform float offset;
    uniform float darkness;
    varying vec2 vUv;

    void main() {
      vec4 texel = texture2D(tDiffuse, vUv);
      float dist = distance(vUv, vec2(0.5, 0.5));
      texel.rgb *= smoothstep(0.8, offset * 0.799, dist * (darkness + offset));
      gl_FragColor = texel;
    }
  `
            };


            const vignettePass = new ShaderPass(VignetteShader);
            vignettePass.uniforms['offset'].value = filters.vignette.offset;
            vignettePass.uniforms['darkness'].value = filters.vignette.darkness;
            this.composer.addPass(vignettePass);
        }



        if (filters.chromaticAberration?.enabled) {

            const ChromaticAberrationShader = {
                uniforms: {
                    tDiffuse: { value: null },
                    offset: { value: new THREE.Vector2(0.0015, 0.001) }
                },
                vertexShader: `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
                fragmentShader: `
    uniform sampler2D tDiffuse;
    uniform vec2 offset;
    varying vec2 vUv;

    void main() {
      vec2 uv = vUv;
      vec4 color;
      color.r = texture2D(tDiffuse, uv + offset).r;
      color.g = texture2D(tDiffuse, uv).g;
      color.b = texture2D(tDiffuse, uv - offset).b;
      color.a = 1.0;
      gl_FragColor = color;
    }
  `
            };


            const caPass = new ShaderPass(ChromaticAberrationShader);
            caPass.uniforms.offset.value = new THREE.Vector2(...filters.chromaticAberration.offset);
            this.composer.addPass(caPass);
        }







        const toneType = this.config.filters?.toneMapping?.type || 'ACESFilmic';
        const exposure = this.config.filters?.toneMapping?.exposure ?? 1.0;

        this.renderer.toneMappingExposure = exposure;

        // Choose tone mapping type
        switch (toneType) {
            case 'ACESFilmic':
                this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
                break;
            case 'Reinhard':
                this.renderer.toneMapping = THREE.ReinhardToneMapping;
                break;
            case 'Linear':
                this.renderer.toneMapping = THREE.LinearToneMapping;
                break;
            case 'None':
            default:
                this.renderer.toneMapping = THREE.NoToneMapping;
                break;
        }

    }






    //  const blob = new Blob([decryptedBuffer], { type: 'image/png' }); // or image/jpeg
    async decryptAndLoadFBX(url, password, callback, type = "application/octet-stream") {
        const response = await fetch(url);
        const encryptedData = await response.arrayBuffer();
        const encryptedArray = new Uint8Array(encryptedData);

        const iv = encryptedArray.slice(0, 16); // first 16 bytes
        const data = encryptedArray.slice(16); // rest is encrypted content

        const enc = new TextEncoder();
        const keyMaterial = await window.crypto.subtle.importKey(
            'raw', enc.encode(password), { name: 'PBKDF2' }, false, ['deriveKey']
        );

        const key = await window.crypto.subtle.deriveKey(
            {
                name: 'PBKDF2',
                salt: enc.encode('salt'),
                iterations: 100000,
                hash: 'SHA-256'
            },
            keyMaterial,
            { name: 'AES-CBC', length: 256 },
            false,
            ['decrypt']
        );

        const decryptedBuffer = await window.crypto.subtle.decrypt(
            { name: 'AES-CBC', iv },
            key,
            data
        );


        //  const blob = new Blob([decryptedBuffer], { type: 'image/png' }); // or image/jpeg

        const blob = new Blob([decryptedBuffer], { type: type });
        const blobURL = URL.createObjectURL(blob);
        callback(blobURL);




    }



    /**
     * Handles the animation loop.
     */
    animate() {

        requestAnimationFrame(() => this.animate());

        //this.activeAction.play()

        //////////////////////////////////////////////////////////// animate file

        const odelta = this.clock.getDelta();



        if (this.mixer) {
            this.mixer.update(odelta);

            // Update progress bar
            const slider = document.getElementById('animProgress');
            if (this.currentAction && this.currentClip) {
                const time = this.currentAction.time % this.currentClip.duration;
                slider.value = time / this.currentClip.duration;
            }
        }



        // Smooth Y-axis rotation
        if (this.modelRoot) {
            const currentY = this.modelRoot.rotation.y;
            const targetY = this.targetRotationY;
            const delta = targetY - currentY;
            if (Math.abs(delta) > 0.001) {
                this.modelRoot.rotation.y += delta * 0.1; // Adjust smoothness here
            }
        }


        // Smooth Y-axis rotation
        if (this.modelRoot) {
            const currentX = this.modelRoot.rotation.x;
            const targetX = this.targetRotationX;
            const deltax = targetX - currentX;
            if (Math.abs(deltax) > 0.001) {
                this.modelRoot.rotation.x += deltax * 0.1; // Adjust smoothness here
            }
        }

        // Animate camera position
        if (this.cameraTargetPos) {
            this.camera.position.lerp(this.cameraTargetPos, 0.1);
            if (this.camera.position.distanceTo(this.cameraTargetPos) < 0.01) {
                this.camera.position.copy(this.cameraTargetPos);
                this.cameraTargetPos = null;
            }
        }

        // Animate controls target
        if (this.controlsTarget) {
            this.controls.target.lerp(this.controlsTarget, 0.1);
            if (this.controls.target.distanceTo(this.controlsTarget) < 0.01) {
                this.controls.target.copy(this.controlsTarget);
                this.controlsTarget = null;
            }
            this.controls.update();
        }

        this.composer.render();

    }

    /**
     * Handles window resize events to maintain aspect ratio and renderer size.
     */
    onResize() {
        const width = window.innerWidth;
        const height = window.innerHeight;
        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(width, height);
        this.composer.setSize(width, height);
    }
}







var p = "/ins_web/ins_uploads/v/"

const config = {
    obj: p + 'models/aa.insya',
    textures: {
        albedo: p + 'textures/albedo.png',
        normal: p + 'textures/normal.png',
        metallic: p + 'textures/metallic.png',
        roughness: p + 'textures/roughness.png'
    },


    wireframe: false,
    camera: {
        fov: 45,
        near: 0.1,
        far: 100,
        position: [2, 2, 4],
        target: [0, 1, 0]
    },


        background_color: 0x292f34,

    lighting: {
        ambient: { color: 0xffffff, intensity: 0.1 },
        directional: { color: 0xffffff, intensity: 0.1, position: [5, 10, 7.5] },



        lightmap: {
            enabled: true,
            url: p + 'textures/env.exr',
            applyAs: 'environment',// environment  or 'background', or 'both'
            intensity: 1
            // this is the environment light strength

        },

    },
    filters: {
        bloom: { enabled: false, strength: 0.6, radius: 0.4, threshold: 0.85 },
        film: { enabled: false, noiseIntensity: 0.35, scanlinesIntensity: 0.025, scanlinesCount: 648 },
        sharpen: {
            enabled: false,
            kernel: [
                0, -1, 0,
                -1, 5, -1,
                0, -1, 0
            ]
        },
        gammaCorrection: true,
        vignette: {
            enabled: false,
            offset: 0.1,   // how far the darkening extends from center
            darkness: 1

            // how dark the edges get
        },
        colorBalance: {
            enabled: true,
            shadows: [1.0, 1.0, 1.0],    // RGB multipliers for shadows
            midtones: [1.0, 1.0, 1.0],   // Midtone color balance
            highlights: [1.0, 1.0, 1.0]  // Highlights tint
        },
        toneMapping: {
            enabled: true,
            type: 'ACESFilmic',  // 'ACESFilmic', 'Reinhard', 'Linear', 'None'
            exposure: 1.2
        },
        chromaticAberration: {
            enabled: false,
            offset: [0.0015, 0.001] // RGB channel offset vector
        }
    }
};

const app = new ThreeScene(config);
app.init();



//encryptFileFromURL( p + 'models/sample.fbx', "123") 


//async decryptAndLoadFBX(url, password ,callback,  type ="application/octet-stream" ) {

//encryptFileFromURL("/ins_web/ins_uploads/v/textures/albedo.png", "123", (ob) => { }, "image/png")

//encryptFileFromURL("/ins_web/ins_uploads/v/models/aa.fbx", "123", (ob) => { })


async function encryptFileFromURL(url, password, callback, type = "application/octet-stream") {
    const response = await fetch(url);
    const data = new Uint8Array(await response.arrayBuffer());

    const iv = crypto.getRandomValues(new Uint8Array(16)); // 16 bytes for AES-CBC

    const enc = new TextEncoder();
    const keyMaterial = await crypto.subtle.importKey(
        'raw', enc.encode(password), { name: 'PBKDF2' }, false, ['deriveKey']
    );
    const key = await crypto.subtle.deriveKey(
        {
            name: 'PBKDF2',
            salt: enc.encode('salt'),
            iterations: 100000,
            hash: 'SHA-256'
        },
        keyMaterial,
        { name: 'AES-CBC', length: 256 },
        false,
        ['encrypt']
    );

    const encrypted = await crypto.subtle.encrypt({ name: 'AES-CBC', iv }, key, data);

    // Combine IV + encrypted data into one Blob
    const combined = new Uint8Array(iv.length + encrypted.byteLength);
    combined.set(iv, 0);
    combined.set(new Uint8Array(encrypted), iv.length);

    ////  const blob = new Blob([decryptedBuffer], { type: 'image/png' }); // or image/jpeg
    // Optionally download it
    const blob = new Blob([combined], { type: type });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = url.split('/').pop() + '.insya';
    a.click();
    callback(blob)
    return blob;
}



