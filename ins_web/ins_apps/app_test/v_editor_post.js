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
        this.parent.composer.passes = [this.renderPass];

        const fxaaPass = new ShaderPass(FXAAShader);

        fxaaPass.material.uniforms['resolution'].value.set(1 / window.innerWidth, 1 / window.innerHeight);
        this.parent.composer.addPass(fxaaPass);







        this.parent.composer.addPass(new ShaderPass(GammaCorrectionShader));





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




        if (this.parent.config.filters.bloom.enabled) {
            this.parent.composer.addPass(this.bloomPass);
        }
        if (this.parent.config.filters.vignette.enabled) {
            this.parent.composer.addPass(this.vignettePass);
        }
        if (this.parent.config.filters.film.enabled) {
            this.parent.composer.addPass(this.filmPass);
        }
        if (this.parent.config.filters.chromaticAberration.enabled) {
            this.parent.composer.addPass(this.caPass);
        }
        if (this.parent.config.filters.colorBalance.enabled) {
            this.parent.composer.addPass(this.colorBalancePass);
        }

        if (this.parent.config.filters.sharpen.enabled) {
            this.parent.composer.addPass(this.sharpenPass);
        }



    }
    postUpdateUI() {


        var b = this.items;
        var self = this;
        Object.keys(b).forEach((t) => {
            Object.keys(b[t]).forEach((k) => {
                var sk = b[t][k]
                var attr = "value"
                if (sk.includes("enabled")) {
                    attr = "checked"

                }
                self.parent.helper._updateAttr(k, attr, this.parent.config.filters[t][sk]);




            })
        });






        ['shadows', 'midtones', 'highlights'].forEach((tone) => {
            ['R', 'G', 'B'].forEach((channel) => {
                this.parent.helper._on(`#${tone}${channel}`, "input", (e) => {
                    this.parent.helper._updateAttr(`#${tone}${channel}`, "value", this.parent.config.filters.colorBalance[idPrefix][channel.toLowerCase]);
                });
            });
        });
    }


    postUpdateUIActions() {


        var b = this.items;
        var self = this;
        Object.keys(b).forEach((t) => {
            Object.keys(b[t]).forEach((k) => {
                var sk = b[t][k]
                if (sk.includes("enabled")) {
                    this.parent.helper._on(k, "change", (e) => {
                        this.parent.config.filters[t][sk] = e.checked
                        this.refreshPostProcessing();
                    });
                }
            })
        });






        ['shadows', 'midtones', 'highlights'].forEach((tone) => {
            ['R', 'G', 'B'].forEach((channel) => {
                this.parent.helper._on(`#${tone}${channel}`, "input", (e) => {
                    this.parent.helper._updateAttr(`#${tone}${channel}`, "value", this.parent.config.filters.colorBalance[idPrefix][channel.toLowerCase]);
                });
            });
        });
    }





    chromaticAberration() {
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
        this.caPass = new ShaderPass(ChromaticAberrationShader);
        this.caPass.uniforms.offset.value = new this.three.Vector2(this.parent.config.filters.chromaticAberration.offsetx, this.parent.config.filters.chromaticAberration.offsetx);
        // this.parent.composer.addPass(caPass);
        this.parent.helper._on('#chromaOffsetX', "input", (e) => {
            this.parent.config.filters.chromaticAberration.offsetx = parseFloat(e.value);
            this.caPass.uniforms.offset.value.x = parseFloat(e.value);
        })
        this.parent.helper._on('#chromaOffsetY', "input", (e) => {
            this.parent.config.filters.chromaticAberration.offsety = parseFloat(e.value);
            this.caPass.uniforms.offset.value.y = parseFloat(e.value);
        })
        /* this.parent.helper._on('#enableChroma', "change", (e) => {
             this.parent.config.filters.chromaticAberration.enabled = e.checked
             this.refreshPostProcessing()
         })*/
    }
    film() {
        const filters = this.parent.config.filters;
        const { noiseIntensity, scanlinesIntensity, scanlinesCount } = this.parent.config.filters.film;
        this.filmPass = new FilmPass(noiseIntensity, this.parent.config.filters.film.gray_enabled);
        this.parent.config.filters.film.scanlinesIntensity = scanlinesIntensity;
        this.parent.helper._on('#filmNoise', "input", (e) => {
            this.parent.config.filters.film.noiseIntensity = parseFloat(e.value);
            this.filmPass.uniforms.nIntensity.value = this.parent.config.filters.film.noiseIntensity;
        })
        this.parent.helper._on('#filmScanlines', "input", (e) => {
            this.parent.config.filters.film.scanlinesIntensity = parseFloat(e.value);
            this.filmPass.uniforms.sIntensity.value = this.parent.config.filters.film.scanlinesIntensity;
        })


        this.parent.helper._on('#enableGrayFilm', "change", (e) => {
            this.parent.config.filters.film.gray_enabled = e.checked
            this.filmPass.uniforms.grayscale.value = this.parent.config.filters.film.gray_enabled;
        })
    }
    Vignette() {
        const VignetteShader = {
            uniforms: {
                tDiffuse: { value: null },
                offset: { value: 0.75 },    // where fade starts
                darkness: { value: 0.6 }
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
        this.vignettePass = new ShaderPass(VignetteShader);
        this.parent.helper._on('#vignetteOffset', "input", (e) => {
            this.parent.config.filters.vignette.offset = parseFloat(e.value);
            this.vignettePass.uniforms['offset'].value = this.parent.config.filters.vignette.offset;
        })
        this.parent.helper._on('#vignetteDarkness', "input", (e) => {
            this.parent.config.filters.vignette.darkness = parseFloat(e.value);
            this.vignettePass.uniforms['darkness'].value = this.parent.config.filters.vignette.darkness;
        })

    }
    bloom() {
        const filters = this.parent.config.filters;
        const { strength, radius, threshold } = filters.bloom;
        this.bloomPass = new UnrealBloomPass(
            new this.three.Vector2(window.innerWidth, window.innerHeight),
            strength,
            radius,
            threshold
        );
        this.parent.helper._on('#bloomStrength', "input", (e) => {
            this.parent.config.filters.bloom.strength = parseFloat(e.value);
            this.bloomPass.strength = this.parent.config.filters.bloom.strength;
        })
        this.parent.helper._on('#bloomRadius', "input", (e) => {
            this.parent.config.filters.bloom.radius = parseFloat(e.value);
            this.bloomPass.radius = this.parent.config.filters.bloom.radius;
        })
        this.parent.helper._on('#bloomThreshold', "input", (e) => {
            this.parent.config.filters.bloom.threshold = parseFloat(e.value);
            this.bloomPass.threshold = this.parent.config.filters.bloom.threshold;
        })

    }
    updateColorUniform(idPrefix, uniformVec3) {
        this.parent.config.filters.colorBalance[idPrefix]["r"] = parseFloat(document.getElementById(`${idPrefix}R`).value);
        this.parent.config.filters.colorBalance[idPrefix]["g"] = parseFloat(document.getElementById(`${idPrefix}G`).value);
        this.parent.config.filters.colorBalance[idPrefix]["b"] = parseFloat(document.getElementById(`${idPrefix}B`).value);
        uniformVec3.set(this.parent.config.filters.colorBalance[idPrefix]["r"], this.parent.config.filters.colorBalance[idPrefix]["g"], this.parent.config.filters.colorBalance[idPrefix]["b"]);
    }
    ColorBalance() {
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
        this.colorBalancePass = new ShaderPass(ColorBalanceShader);
        this.colorBalancePass.uniforms.shadows.value = new this.three.Vector3(this.filters.colorBalance.shadows.r, this.filters.colorBalance.shadows.g, this.filters.colorBalance.shadows.b);
        this.colorBalancePass.uniforms.midtones.value = new this.three.Vector3(this.filters.colorBalance.midtones.r, this.filters.colorBalance.midtones.g, this.filters.colorBalance.midtones.b);
        this.colorBalancePass.uniforms.highlights.value = new this.three.Vector3(this.filters.colorBalance.highlights.r, this.filters.colorBalance.highlights.g, this.filters.colorBalance.highlights.b);



        this.parent.helper._on('.cbitem-btn', "click", (e) => {

            this.parent.helper.updateActive(".cbitem-btn", e);
            document.querySelectorAll(".cbitem-tab-body").forEach(p => {
                p.classList.add("ins-hidden");
            });

            document.querySelectorAll(".cbitem-tab-body." + e.dataset["p"]).forEach(p => {
                p.classList.remove("ins-hidden");
            });
        });


        ['shadows', 'midtones', 'highlights'].forEach((tone) => {
            ['R', 'G', 'B'].forEach((channel) => {
                this.parent.helper._on(`#${tone}${channel}`, "input", (e) => {
                    this.updateColorUniform(tone, this.colorBalancePass.uniforms[tone].value);
                });
            });
        });
    }

    sharpen() {

        const SharpenShader = {
            uniforms: {
                tDiffuse: { value: null },
                resolution: { value: new this.three.Vector2(1, 1) },
                strength: { value: 0.3 } // ⬅️ adjustable in UI
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
    uniform vec2 resolution;
    uniform float strength;
    varying vec2 vUv;

    void main() {
      vec2 texel = 1.0 / resolution;

      vec3 color = texture2D(tDiffuse, vUv).rgb * (1.0 + 4.0 * strength);
      color -= texture2D(tDiffuse, vUv + vec2(-texel.x, 0.0)).rgb * strength;
      color -= texture2D(tDiffuse, vUv + vec2(texel.x, 0.0)).rgb * strength;
      color -= texture2D(tDiffuse, vUv + vec2(0.0, -texel.y)).rgb * strength;
      color -= texture2D(tDiffuse, vUv + vec2(0.0, texel.y)).rgb * strength;

      gl_FragColor = vec4(color, 1.0);
    }
  `
        };



        this.sharpenPass = new ShaderPass(SharpenShader);
        this.sharpenPass.uniforms.resolution.value.set(window.innerWidth, window.innerHeight);


        this.parent.helper._on('#sharpensStrength', "input", (e) => {
            this.parent.config.filters.sharpen.strength = parseFloat(e.value);
            this.sharpenPass.uniforms.strength.value = parseFloat(e.value);

        })

    }



    setupPostProcessing() {

        this.items = {
            "bloom": { "#bloomStrength": "strength", "#bloomRadius": "radius", "#bloomThreshold": "radius", "#enableBloom": "enabled" },
            "vignette": { "#vignetteOffset": "offset", "#vignetteDarkness": "darkness", "#enableVignette": "enabled" },
            "film": { "#filmNoise": "noiseIntensity", "#filmRadius": "scanlinesIntensity", "#filmScanlines": "scanlinesCount", "#enableFilm": "enabled", "#enableGrayFilm": "gray_enabled" },
            "chromaticAberration": { "#chromaOffsetX": "offsetx", "#chromaOffsetY": "offsety", "#enableChroma": "enabled" },
            "colorBalance": { "#enableColorBalance": "enabled" },
            "sharpen": { "#sharpensStrength": "strength", "#enableSharpen": "enabled" }

        }

        this.filters = this.parent.config.filters;

        this.parent.composer = new EffectComposer(this.parent.renderer);
        this.renderPass = new RenderPass(this.parent.scene, this.parent.camera);
        this.parent.composer.addPass(this.renderPass);
        this.bloom();
        this.Vignette()
        this.film()
        this.chromaticAberration()
        this.ColorBalance()
        this.sharpen()

        this.postUpdateUIActions()
        this.refreshPostProcessing();
    }
   
   
}
