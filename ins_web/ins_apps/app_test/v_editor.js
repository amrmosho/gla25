import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js';
import { TransformControls } from 'three/examples/jsm/controls/TransformControls.js';
import { EXRLoader } from 'three/examples/jsm/loaders/EXRLoader.js';




import { InsVSceneUi } from './v_editor_ui.js';
import { InsVHelper } from './v_editor_helper.js';
import { InsVPost } from './v_editor_post.js';


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
        this.isScrubbing = false;
        this.cameraTargetPos = null;
        this.controlsTarget = null;
        this.textures = {}
        this.texturesIndx = 0
        this.renderer.xr.enabled = true;
        this.matmode = "render"
        this.dir = "/ins_web/ins_uploads/v/"
        this.currentEnvFile = "";
        this.lighting_dir = "/ins_web/ins_uploads/v/hdrs/"
        this.isEnvEnabled = true; // default: environment lighting on
        this.originalEnvMap = this.scene.environment; // save it initially
        this.helper = new InsVHelper(this, THREE);

        this.ui = new InsVSceneUi(this, THREE);
        this.post = new InsVPost(this, THREE);



    }
    /**
     * Initializes the scene, including renderer, controls, lighting, model, and post-processing.
     */
    async init() {
        this.renderer.outputEncoding = THREE.sRGBEncoding;
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        this.container = document.getElementById('insv-body');
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
        this.container.appendChild(this.renderer.domElement);
        this.controls = new OrbitControls(this.camera, this.renderer.domElement);
        this.controls.target.set(0, 1, 0);

      /*  this.transformControls = new TransformControls(this.camera, this.renderer.domElement);
        this.transformControls.addEventListener('change', () => this.composer.render());

        // Optional: disable orbit while using transform
        this.transformControls.addEventListener('dragging-changed', (e) => {
            this.controls.enabled = !e.value;
        });*/

        this.scene.add(this.transformControls);

        this.controls.update();
        const grid = new THREE.GridHelper(10, 20, 0x888888, 0x444444);
        grid.material.opacity = 0.5;
        grid.material.transparent = true;





        this.scene.add(grid);
        const axisMaterial = new THREE.LineBasicMaterial({ color: 0xff0000 }); // red for X
        const xLine = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(-10, 0, 0),
            new THREE.Vector3(10, 0, 0)
        ]);
        const xAxis = new THREE.Line(xLine, axisMaterial);
        this.scene.add(xAxis);
        const zMaterial = new THREE.LineBasicMaterial({ color: 0x0000ff }); // blue for Z
        const zLine = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(0, 0, -10),
            new THREE.Vector3(0, 0, 10)
        ]);
        const zAxis = new THREE.Line(zLine, zMaterial);
        this.scene.add(zAxis);
        const axes = new THREE.AxesHelper(5);
        this.scene.add(axes);

        this.mixer = null;
        this.clock = new THREE.Clock();
        this.scene.background = new THREE.Color(this.tocolor(this.config.background_color));
        this.loadingManager = new THREE.LoadingManager();
        this.textureLoader = new THREE.TextureLoader(this.loadingManager);
        this.fbxLoader = new FBXLoader(this.loadingManager);
        // Optional: loading events
        this.loadingManager.onStart = () => console.log('Loading started...');
        this.loadingManager.onProgress = (url, itemsLoaded, itemsTotal) =>
            console.log(`Loading: ${itemsLoaded} of ${itemsTotal} (${url})`);
        this.loadingManager.onLoad = () => {
            console.log('All assets loaded!');
            this.onAssetsLoaded(); // show scene



        };
        this.preloadTextures(this.config.textures);
        this.annotations();
        this.onResize(this.container.clientWidth, this.container.clientHeight)
        window.addEventListener('resize', () => this.onResize(this.container.clientWidth, this.container.clientHeight));
    }
    annotations() {
        if (this.config.annotations != null) {
            const container = document.getElementById('annotations');
            this.config.annotations.forEach((ann, i) => {
                const el = document.createElement('div');
                el.className = 'annotation';
                el.textContent = ann.label;
                el.style.position = 'absolute';
                el.style.background = 'rgba(0,0,0,0.7)';
                el.style.color = '#fff';
                el.style.padding = '2px 6px';
                el.style.borderRadius = '4px';
                el.style.fontSize = '12px';
                el.style.pointerEvents = 'none';
                container.appendChild(el);
                this.config.annotations[i].el = el; // store ref
            });
        }
    }





/*

    gadd_remove(remove = false) {
        var t = this; console.log(t.transformControls);
        if (remove) {
            t.scene.remove(t.transformControls)
        } else {
            t.scene.add(t.transformControls);
            t.transformControls.attach(t.modelRoot);
        }
    }*/



    updateBackGoundColor() {

        this.scene.background = new THREE.Color(this.tocolor(this.config.background_color));
    }
    onAssetsLoaded() {
        document.getElementById('loaderOverlay').style.display = 'none';
        _send('/ins_ajax/home/app_test/_key/do/_area/home/_alias/test/', { userToken: 'abc123' },
            (k) => {
                this.decryptAndLoadFBX(this.dir + this.config.obj, k, (blobURL) => {
                    this.loadModel(blobURL);


                    this.setupLighting();
                    this.post.setupPostProcessing();
                    this.setupUI();
                    this.animate();
                    //this.gadd_remove()
                    document.body.classList.remove('loading');
                });
            }
        );        // uses this.textures
    }
    preloadTextures(texturePaths) {
        this.textures = {};
        for (const [key, path] of Object.entries(texturePaths)) {
            this.textures[key] = this.textureLoader.load(path);
        }
    }
    tocolor(c) {
        return parseInt(c, 16)
    }
    /**
     * Sets up ambient and directional lighting based on the configuration.
     */
    updateEnvMapIntensity() {
        this.scene.traverse((child) => {
            if (child.isMesh && child.material && 'envMapIntensity' in child.material) {
                child.material.envMapIntensity = this.config.lighting.lightmap.intensity
                child.material.needsUpdate = true;
            }
        });
    }
    //////////////////////////// lighting
    applyLightingPreset() {

        const preset = this.config.lighting.lightmap.lighting_preset;
        // 1. Clear previous lights
        if (this.lights && typeof this.lights === 'object') {
            Object.values(this.lights).forEach(light => this.scene.remove(light));
        }
        this.lights = {};
        // 2. Create lights based on preset
        switch (preset) {
            case 'threePoint':
                this.lights = {
                    key: new THREE.DirectionalLight(0xffffff, 1.2),
                    fill: new THREE.DirectionalLight(0xffffff, 0.5),
                    rim: new THREE.DirectionalLight(0xffffff, 0.8)
                };
                this.lights.key.position.set(3, 5, 2);
                this.lights.fill.position.set(-3, 2, 1);
                this.lights.rim.position.set(0, 3, -4);
                break;
            case 'lowKey':
                this.lights = {
                    spot: new THREE.SpotLight(0xffffff, 1)
                };
                this.lights.spot.position.set(0, 5, 3);
                this.lights.spot.angle = Math.PI / 8;
                this.lights.spot.penumbra = 0.3;
                break;
            case 'moonlight':
                this.lights = {
                    moon: new THREE.DirectionalLight(0x8899ff, 0.6),
                    ambient: new THREE.AmbientLight(0x223366, 0.2)
                };
                this.lights.moon.position.set(-2, 4, 1);
                break;
            case 'evil':
                this.lights = {
                    red: new THREE.PointLight(0xff0000, 1, 10),
                    blue: new THREE.PointLight(0x0000ff, 0.5, 6),
                    ambient: new THREE.AmbientLight(0x220022, 0.2)
                };
                this.lights.red.position.set(2, 3, 2);
                this.lights.blue.position.set(0, 1, -3);
                break;
            case 'fairy':
                this.lights = {
                    glow: new THREE.PointLight(0xffccaa, 1.0, 6),
                    sparkle: new THREE.PointLight(0xaaffee, 0.5, 4),
                    ambient: new THREE.AmbientLight(0x443322, 0.4)
                };
                this.lights.glow.position.set(0, 2, 2);
                this.lights.sparkle.position.set(1.5, 1.5, -2);
                break;
        }
        // 3. Add new lights to scene
        Object.values(this.lights).forEach(light => {
            this.scene.add(light);
        });
        // 4. Update light UI sliders
        this.updateLightSliders();
        // 4. Optionally reduce environment lighting
        if (this.scene.environment && this.envMapIntensity !== undefined) {
            this.scene.traverse((child) => {
                if (child.isMesh && child.material && 'envMapIntensity' in child.material) {
                    child.material.envMapIntensity = 0.2; // tone it down
                    child.material.needsUpdate = true;
                }
            });
        }
    }
    updateLightSliders() {
        const container = document.getElementById('lightControls');
        container.innerHTML = ''; // Clear previous sliders
        Object.entries(this.lights).forEach(([key, light]) => {
            const wrapper = document.createElement('div');

            wrapper.classList.add("ins-col-12", "ins-flex")

            const label = document.createElement('label');
            label.textContent = `${key.charAt(0).toUpperCase() + key.slice(1)} Intensity`;

            label.classList.add("ins-col-grow")


            const input = document.createElement('input');
            input.type = 'range';
            input.min = 0;
            input.max = 5;
            input.step = 0.1;
            input.value = light.intensity;
            input.classList.add("ins-col-12")


            const valueLabel = document.createElement('span');
            valueLabel.textContent = light.intensity;
            input.addEventListener('input', () => {
                light.intensity = parseFloat(input.value);
                valueLabel.textContent = input.value;
            });
            wrapper.appendChild(label);
            wrapper.appendChild(valueLabel);

            wrapper.appendChild(input);
            container.appendChild(wrapper);
        });
    }
    updateenv(off = false) {
        var rotationY = parseFloat(this.config.lighting.lightmap.rotation_y || 0);
        const exrLoader = new EXRLoader();
        const pmrem = new THREE.PMREMGenerator(this.renderer);
        pmrem.compileEquirectangularShader();
        exrLoader.load(this.lighting_dir + this.config.lighting.lightmap.url + ".exr", (texture) => {
            texture.mapping = THREE.EquirectangularReflectionMapping;
            /*   if (off) {
                this.scene.environment = null;
                this.scene.background = null;
                this.updateEnvMapIntensity(0)
            } else {*/
            // Create skydome for rotation
            const envScene = new THREE.Scene();
            const geo = new THREE.SphereGeometry(100, 64, 32);// larger & smoother
            geo.scale(-1, 1, 1); // inward
            const mat = new THREE.MeshBasicMaterial({ map: texture });
            const mesh = new THREE.Mesh(geo, mat);
            mesh.rotation.y = THREE.MathUtils.degToRad(rotationY);
            envScene.add(mesh);
            // LESS blurry by lowering blur param from 1 → 0.1
            const renderTarget = pmrem.fromScene(envScene, parseFloat(this.config.lighting.lightmap.env_blur || 0))

            const envMap = renderTarget.texture;
            //  if (this.config.lighting.lightmap.applyAs === 'environment' || this.config.lighting.lightmap.applyAs === 'both') {
            this.scene.environment = envMap;
            // }



            if (this.config.lighting.lightmap.background === 'env') {

                this.scene.background = envMap;


            } else if (this.config.lighting.lightmap.background === 'color') {
                this.scene.background = new THREE.Color(this.tocolor(this.config.background_color));


            }



            this.originalEnvMap = this.scene.environment;
            this.envMap = envMap;
            this.envIntensity = this.config.lighting?.lightmap?.intensity ?? 1;
            //  }
            // Clean up
            texture.dispose();
            geo.dispose();
            mat.dispose();
            // Update materials
            this.scene.traverse((child) => {
                if (child.isMesh && child.material && 'envMap' in child.material) {
                    child.material.envMap = envMap;
                    child.material.envMapIntensity = this.envIntensity;
                    child.material.needsUpdate = true;
                }
            });
        });
    }
    setupLighting() {
        const { ambient, directional, lightmap } = this.config.lighting;
        // this.scene.add(new THREE.AmbientLight(this.tocolor(ambient.color), ambient.intensity));
        // const dirLight = new THREE.DirectionalLight(this.tocolor(directional.color), directional.intensity);
        //  dirLight.position.set(...directional.position);
        //  this.scene.add(dirLight);
        // Load EXR environment map if enabled
        if (lightmap?.enabled && lightmap.url) {
            this.updateenv()
        }
    }
    //////////////////////////// lighting End
    //////////////////////////// Ui
    setupUI() {
        var t = this;
        this.ui.UI()
        document.getElementById('vrBtn')?.addEventListener('click', async () => {
            if (navigator.xr && navigator.xr.isSessionSupported) {
                const supported = await navigator.xr.isSessionSupported('immersive-vr');
                if (!supported) {
                    alert('VR not supported on this device.');
                    return;
                }
            }
            this.renderer.xr.setReferenceSpaceType('local');
            const session = await navigator.xr.requestSession('immersive-vr');
            this.renderer.xr.setSession(session);
        });
        document.getElementById('arBtn')?.addEventListener('click', async () => {
            if (navigator.xr && navigator.xr.isSessionSupported) {
                const supported = await navigator.xr.isSessionSupported('immersive-ar');
                if (!supported) {
                    alert('AR not supported on this device.');
                    return;
                }
            }
            this.renderer.xr.setReferenceSpaceType('local');
            const session = await navigator.xr.requestSession('immersive-ar', {
                requiredFeatures: ['hit-test', 'dom-overlay'],
                domOverlay: { root: document.body }
            });
            this.renderer.xr.setSession(session);
        });
        const slider = document.getElementById('animProgress');
        slider?.addEventListener('mousedown', () => this.isScrubbing = true);
        slider?.addEventListener('mouseup', () => this.isScrubbing = false);
        slider?.addEventListener('input', (e) => {
            // this.currentAction.paused = true; // pause while scrubbing
            //this.currentAction.time = newTime;
            // this.mixer.setTime(newTime);
            //  this.mixer.update(0); // refresh
            if (!this.mixer || !this.currentClip || !this.currentAction) return;
            const percent = parseFloat(e.target.value);
            const newTime = percent * this.currentClip.duration;
            // Pause all actions and stop automatic update
            this.mixer.stopAllAction();
            // Create a temp action just for preview
            const tempAction = this.mixer.clipAction(this.currentClip);
            tempAction.paused = true;
            tempAction.time = newTime;
            tempAction.reset().play(); // activate so mixer can evaluate
            this.mixer.setTime(newTime); // update the mixer
            this.mixer.update(0);
        });
        document.getElementById('playAnimBtn')?.addEventListener('click', (e) => {
            const index = parseInt(document.getElementById('animList').value);
            if (e.target.classList.contains("active")) {
                e.target.classList.remove("active");
                /* if (this.currentAction) {
                     this.currentAction.stop();
                 }*/
                if (this.currentAction && this.mixer) {
                    this.currentAction.paused = true;
                }
            } else {
                e.target.classList.add("active");
                if (this.currentAction && this.currentAction.paused) {
                    this.currentAction.paused = false;
                } else {
                    this.playAnimation(index);
                }
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
                t.matmode = e.target.dataset["rend"]
                if (e.target.dataset["rend"] == "wire") {
                    e.target.dataset["rend"] = "wireof"
                    t.update_mats(true);
                } else
                    if (e.target.dataset["rend"] == "wireof") {
                        e.target.dataset["rend"] = "wire"
                        t.update_mats();
                    } else {
                        t.update_mats();
                    }
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
        if (this.config.textures.length > 1) {
            var i = 0;
            this.config.textures.forEach(k => {
                const list = document.getElementById('insv-text-btns');
                const btn = document.createElement("div");
                const img = document.createElement("img");
                img.src = this.dir + k["th"]
                btn.appendChild(img);
                btn.classList.add("insv_txt_btn", "insv-icon_btn");
                img.dataset["i"] = i;
                btn.style.left = (k * 10) + "px";
                list.appendChild(btn);
                img.onclick = (e) => {
                    t.texturesIndx = e.target.dataset["i"];
                    t.update_mats()
                }
                i++;
            })
        }
    }
    //////////////////////////// Ui
    //////////////////////////// materials start
    update_textures(name) {
        var textures = {}
        if (this.config.textures[this.texturesIndx][name] == null) {
            var tk = this.config.textures[this.texturesIndx][1];
        } else {
            var tk = this.config.textures[this.texturesIndx][name];
        }
        Object.keys(tk).forEach(k => {
            if (typeof tk[k] == "string") {
                textures[k] = this.dir + tk[k];
            } else {
                textures[k] = tk;
            }
        });
        return textures;
    }
    mat(name, wire = false) {
        let textures = this.update_textures(name);
        const loader = new THREE.TextureLoader();
        var tc = {
            emissive: new THREE.Color(0xffffff),
            transparent: true,
            opacity: textures.opacity ? textures.opacity : 1.0,
            emissiveIntensity: textures.emissive ? textures.emissive : 0,
            metalness: textures.metalness ? textures.metalness : 1.0,
            roughness: textures.roughness ? textures.roughness : 1.0,
            aoMapIntensity: textures.ao ? textures.ao : 1.0,
        }
        var material = new THREE.MeshStandardMaterial(tc);
        material.name = name
        material.wireframe = wire;
        var albedo = loader.load(textures.color_map);
        if (this.matmode == "normal") {
            var albedo = loader.load(textures.normal_map)
            delete textures.roughness_map;
            delete textures.emissive_map;
            delete textures.opacity_map;
            material.metalness = 0;
            material.roughness = 1.0;
        } else if (this.matmode == "rough") {
            var albedo = loader.load(textures.roughness_map)
            delete textures.roughness;
            delete textures.emissive;
            delete textures.opacity;
            material.metalness = 0;
            material.roughness = 1.0;
        } else if (this.matmode == "metal") {
            var albedo = loader.load(textures.metal_map)
            delete textures.roughness_map;
            delete textures.emissive_map;
            delete textures.opacity_map;
            delete textures.metal_map;
            material.metalness = 0;
            material.roughness = 1.0;
        } else if (this.matmode == "color") {
            delete textures.roughness_map;
            delete textures.emissive_map;
            delete textures.metal_map;
            delete textures.opacity_map;
            material.metalness = 0;
            material.roughness = 1.0;
        }
        if (albedo != null) {
            material.map = albedo;
        }
        if (textures.metal_map != null)
            material.metalnessMap = loader.load(textures.metal_map);
        if (textures.normal_map != null)
            material.normalMap = loader.load(textures.normal_map);
        if (textures.roughness_map != null)
            material.roughnessMap = loader.load(textures.roughness_map);
        if (textures.emissive_map != null)
            material.emissiveMap = loader.load(textures.emissive_map);
        if (textures.opacity_map != null)
            material.alphaMap = loader.load(textures.opacity_map);
        if (textures.ao_map != null)
            material.aoMap = loader.load(textures.ao_map);
        material = this.mat_update(material);
        return material;
    }
    mat_update(material) {
        ['map', 'normalMap', 'metalnessMap', 'roughnessMap'].forEach((mapType) => {
            const map = material[mapType];
            if (map) {
                if (mapType === 'map') {
                    map.encoding = THREE.sRGBEncoding;
                }
            }
        });
        return material;
    }
    playAnimation(index) {
        if (!this.mixer || !this.animations.length) return;
        if (this.currentAction) {
            this.currentAction.stop();
        }
        const clip = this.animations[index];
        this.currentClip = clip;
        this.currentAction = this.mixer.clipAction(clip);
        this.currentAction.reset().play();
    }
    /**
     * Loads the FBX model and applies PBR textures as specified in the configuration.
     */
    update_mats(wire = false) {
        this.modelRoot.traverse((child) => {
            if (child.isMesh) {
                this.obj = child;
                if (Array.isArray(child.material)) {
                    const newMaterials = child.material.map((mat) => {
                        const newMat = this.mat(mat.name, wire)
                        return newMat;
                    });
                    child.material = newMaterials;
                    child.material.forEach((m) => m.needsUpdate = true);
                } else {
                    console.log(child.material.name);
                    child.material = this.mat(child.material.name, wire);
                    child.material.needsUpdate = true
                }
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
    }
    //////////////////////////// materials start
    loadModel(fbxUrl) {
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
            } else {
                document.getElementById('insvAnimationCont').remove();
            }
            this.modelRoot = fbx;

            this.update_mats()
         //   this.transformControls.attach(this.modelRoot);

            this.scene.add(this.modelRoot);
        });
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
        const delta = this.clock.getDelta();
        if (this.mixer && this.currentAction && this.currentClip) {
            if (!this.currentAction.paused) {
                this.mixer.update(delta);
                // Only update slider if user isn't scrubbing
                if (!this.isScrubbing) {
                    const time = this.currentAction.time % this.currentClip.duration;
                    const percent = time / this.currentClip.duration;
                    document.getElementById('animProgress').value = percent;
                }
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
        /*  if (this.modelRoot) {
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
          }*/
        if (this.config.annotations != null) {
            this.config.annotations.forEach((ann) => {
                const pos = new THREE.Vector3(ann.position[0], ann.position[1], ann.position[2]);
                pos.project(this.camera); // convert to normalized device coords
                const x = (pos.x * 0.5 + 0.5) * window.innerWidth;
                const y = (1 - (pos.y * 0.5 + 0.5)) * window.innerHeight;
                ann.el.style.transform = `translate(-50%, -50%) translate(${x}px, ${y}px)`;
                ann.el.style.display = pos.z > 1 || pos.z < -1 ? 'none' : 'block'; // hide if behind camera
            });
        }
        this.composer.render();
    }
    /**
     * Handles window resize events to maintain aspect ratio and renderer size.
     */
    onResize(width, height) {
        console.log(width);
        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(width * 2, height * 2, false);
        this.composer.setSize(width, height);
        this.renderer.setPixelRatio(2); // or even higher if GPU allows
    }
}
var p = "/ins_web/ins_uploads/v/"
p += "apple/"
//p += "samsung/"
fetch(p + 'data.json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    }) // Parse JSON
    .then(config => {
        config.path = p + 'data.json'
        const app = new ThreeScene(config);
        app.init();
    }) // Work with JSON data
    .catch(error => console.error('Error fetching JSON:', error));
const config = {
    obj: p + 'models/aa.insya',
    textures: {
        albedo: p + 'textures/albedo.png',
        normal: p + 'textures/normal.png',
        metallic: p + 'textures/metallic.png',
        roughness: p + 'textures/roughness.png',
        opacity: p + 'textures/opacity.png',
        emissive: p + 'textures/emissive.png',
        ao: p + 'textures/ao.png',
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
        ambient: { color: 0xffffff, intensity: 0.01 },
        directional: { color: 0xffffff, intensity: 0.01, position: [5, 10, 7.5] },
        lightmap: {
            enabled: true,
            url: p + 'textures/env.exr',
            applyAs: 'environment',// environment  or 'background', or 'both'
            intensity: 0.8
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
            exposure: 1
        },
        chromaticAberration: {
            enabled: false,
            offset: [0.0015, 0.001] // RGB channel offset vector
        }
    }
};
//encryptFileFromURL( p + 'models/test.fbx', "123") 
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
