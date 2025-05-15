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
        this.controls.update();

        this.scene.background = new THREE.Color(0x1e1e1e);

        this.setupLighting();

        await this.decryptAndLoadFBX('models/model.fbx.enc', '123');


        this.setupPostProcessing();
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
            console.log(lightmap)
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

    /**
     * Loads the FBX model and applies PBR textures as specified in the configuration.
     */
    loadModel() {
        const loader = new THREE.TextureLoader();
        const tex = this.config.textures;

        const material = new THREE.MeshStandardMaterial({
            map: loader.load(tex.albedo),
            normalMap: loader.load(tex.normal),
            metalnessMap: loader.load(tex.metallic),
            roughnessMap: loader.load(tex.roughness),
            metalness: 1.0,
            roughness: 1.0
        });

        // Ensure textures are correctly configured
        ['map', 'normalMap', 'metalnessMap', 'roughnessMap'].forEach((mapType) => {
            const map = material[mapType];
            if (map) {
                // map.flipY = false;
                if (mapType === 'map' || mapType === 'normalMap') {
                    map.encoding = THREE.sRGBEncoding;
                }
            }
        });

        const fbxLoader = new FBXLoader();
        fbxLoader.load(this.config.fbxUrl, (fbx) => {
            fbx.scale.set(0.1, 0.1, 0.1);
            fbx.traverse((child) => {
                if (child.isMesh) {
                    child.material = material;

                    // Apply environment map and intensity
                    if (this.envMap) {
                        child.material.envMap = this.envMap;
                        child.material.envMapIntensity = this.envIntensity ?? 1;
                        child.material.needsUpdate = true;
                    }
                }
            });
            this.scene.add(fbx);
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



async decryptAndLoadFBX(url, password) {
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

  const blob = new Blob([decryptedBuffer], { type: 'application/octet-stream' });
  const blobURL = URL.createObjectURL(blob);

  const loader = new FBXLoader();
  loader.load(blobURL, (object) => {
    object.scale.set(0.01, 0.01, 0.01);
    object.traverse((child) => {
      if (child.isMesh) {
        // Apply material and envMap just like in loadModel()
        child.material = this.buildPBRMaterial(); // you can extract this logic
        if (this.envMap) {
          child.material.envMap = this.envMap;
          child.material.envMapIntensity = this.envIntensity ?? 1;
          child.material.needsUpdate = true;
        }
      }
    });
    this.scene.add(object);
  });
}


    /**
     * Handles the animation loop.
     */
    animate() {
        requestAnimationFrame(() => this.animate());
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




