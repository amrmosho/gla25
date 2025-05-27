import { ARButton } from 'three/examples/jsm/webxr/ARButton.js';
import { FXAAShader } from 'three/examples/jsm/shaders/FXAAShader.js';

import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { FilmPass } from 'three/examples/jsm/postprocessing/FilmPass.js';
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass.js';
import { ConvolutionShader } from 'three/examples/jsm/shaders/ConvolutionShader.js';
import { GammaCorrectionShader } from 'three/examples/jsm/shaders/GammaCorrectionShader.js';


export class InsVPost {
    constructor(t, THREE) {
        this.parent = t;
        this.three = THREE;
    }

    refreshPostProcessing() {
        this.composer.passes = [this.renderPass]; // reset

        if (document.getElementById('enableBloom').checked) {
            this.composer.addPass(this.bloomPass);
        }

        if (document.getElementById('enableVignette').checked) {
            this.composer.addPass(this.vignettePass);
        }
    }


    /**
      * Sets up post-processing effects based on the configuration.
      */
    setupPostProcessing() {
        this.parent.composer = new EffectComposer(this.parent.renderer);
        this.parent.composer.addPass(new RenderPass(this.parent.scene, this.parent.camera));
        const fxaaPass = new ShaderPass(FXAAShader);
        fxaaPass.material.uniforms['resolution'].value.set(1 / window.innerWidth, 1 / window.innerHeight);
        this.parent.composer.addPass(fxaaPass);
        const filters = this.parent.config.filters;
        if (filters.bloom?.enabled) {
            const { strength, radius, threshold } = filters.bloom;
            const bloomPass = new UnrealBloomPass(
                new this.three.Vector2(window.innerWidth, window.innerHeight),
                strength,
                radius,
                threshold
            );
            this.parent.composer.addPass(bloomPass);
        }
        if (filters.film?.enabled) {
            const { noiseIntensity, scanlinesIntensity, scanlinesCount } = filters.film;
            const filmPass = new FilmPass(noiseIntensity, scanlinesIntensity, scanlinesCount, false);
            this.parent.composer.addPass(filmPass);
        }
        if (filters.sharpen?.enabled) {
            const sharpenPass = new ShaderPass(ConvolutionShader);
            sharpenPass.uniforms['uImageIncrement'].value = new this.three.Vector2(0, 0);
            sharpenPass.uniforms['cKernel'].value = filters.sharpen.kernel;
            this.parent.composer.addPass(sharpenPass);
        }
        if (filters.gammaCorrection) {
            this.parent.composer.addPass(new ShaderPass(GammaCorrectionShader));
        }
        if (filters.colorBalance?.enabled) {
            const ColorBalanceShader = {
                uniforms: {
                    tDiffuse: { value: null },
                    shadows: { value: new this.three.Vector3(1.0, 0.9, 0.9) },
                    midtones: { value: new this.three.Vector3(1.0, 1.0, 1.0) },
                    highlights: { value: new this.three.Vector3(1.1, 1.1, 1.2) }
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
            pass.uniforms.shadows.value = new this.three.Vector3(...filters.colorBalance.shadows);
            pass.uniforms.midtones.value = new this.three.Vector3(...filters.colorBalance.midtones);
            pass.uniforms.highlights.value = new this.three.Vector3(...filters.colorBalance.highlights);
            this.parent.composer.addPass(pass);
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
            this.parent.composer.addPass(vignettePass);
        }
        if (filters.chromaticAberration?.enabled) {
            const ChromaticAberrationShader = {
                uniforms: {
                    tDiffuse: { value: null },
                    offset: { value: new this.three.Vector2(0.0015, 0.001) }
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
            caPass.uniforms.offset.value = new this.three.Vector2(...filters.chromaticAberration.offset);
            this.parent.composer.addPass(caPass);
        }
        const toneType = this.parent.config.filters?.toneMapping?.type || 'ACESFilmic';
        const exposure = this.parent.config.filters?.toneMapping?.exposure ?? 1.0;
        this.parent.renderer.toneMappingExposure = exposure;
        // Choose tone mapping type
        switch (toneType) {
            case 'ACESFilmic':
                this.parent.renderer.toneMapping = this.three.ACESFilmicToneMapping;
                break;
            case 'Reinhard':
                this.parent.renderer.toneMapping = this.three.ReinhardToneMapping;
                break;
            case 'Linear':
                this.parent.renderer.toneMapping = this.three.LinearToneMapping;
                break;
            case 'None':
            default:
                this.parent.renderer.toneMapping = this.three.NoToneMapping;
                break;
        }
    }

}



