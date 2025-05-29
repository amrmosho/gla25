import { InsVHelper } from './v_editor_helper.js';
import { TransformControls } from 'three/examples/jsm/controls/TransformControls.js';

export class InsVSceneUi {
    constructor(t, THREE) {
        this.parent = t;
        this.three = THREE;
        this.helper = new InsVHelper(t, THREE);
    }
    ecamera_panel() {
        const cam = this.parent.camera;
        if (document.getElementById('camFOV').value != null) {
            document.getElementById('camFOV').value = cam.fov;
            document.getElementById('camNear').value = cam.near;
            document.getElementById('camFar').value = cam.far;
            document.getElementById('camPosX').value = cam.position.x;
            document.getElementById('camPosY').value = cam.position.y;
            document.getElementById('camPosZ').value = cam.position.z;
            document.getElementById('camRotX').value = cam.rotation.x
            document.getElementById('camRotY').value = cam.rotation.y
            document.getElementById('camRotZ').value = cam.rotation.z
        }
        document.getElementById('camFOV')?.addEventListener('input', () => {
            cam.fov = parseFloat(document.getElementById('camFOV').value);
            cam.updateProjectionMatrix();
        });
        ['camNear', 'camFar'].forEach(id => {
            document.getElementById(id)?.addEventListener('input', () => {
                cam.near = parseFloat(document.getElementById('camNear').value);
                cam.far = parseFloat(document.getElementById('camFar').value);
                cam.updateProjectionMatrix();
            });
        });
        ['camPosX', 'camPosY', 'camPosZ'].forEach((id, i) => {
            document.getElementById(id)?.addEventListener('input', () => {
                if (document.getElementById('camPosX').value != null) {
                    cam.position.set(
                        parseFloat(document.getElementById('camPosX').value),
                        parseFloat(document.getElementById('camPosY').value),
                        parseFloat(document.getElementById('camPosZ').value)
                    );
                }
            });
        });
        ['camRotX', 'camRotY', 'camRotZ'].forEach((id) => {
            document.getElementById(id)?.addEventListener('input', () => {
                if (document.getElementById('camRotX').value != null) {
                    const x = THREE.MathUtils.degToRad(parseFloat(document.getElementById('camRotX').value));
                    const y = THREE.MathUtils.degToRad(parseFloat(document.getElementById('camRotY').value));
                    const z = THREE.MathUtils.degToRad(parseFloat(document.getElementById('camRotZ').value));
                    cam.rotation.set(x, y, z);
                }
            });
        });
    }
    escale_panel(t) {

        console.log(t.transformControls);
        const obj = t.transformControls.object;
        if (document.getElementById('posX').value != null) {
            document.getElementById('posX').value = obj.position.x.toFixed(2);
            document.getElementById('posY').value = obj.position.y.toFixed(2);
            document.getElementById('posZ').value = obj.position.z.toFixed(2);
            document.getElementById('rotX').value = obj.rotation.x //THREE.MathUtils.radToDeg(obj.rotation.x).toFixed(1);
            document.getElementById('rotY').value = obj.rotation.y  //THREE.MathUtils.radToDeg(obj.rotation.y).toFixed(1);
            document.getElementById('rotZ').value = obj.rotation.z //THREE.MathUtils.radToDeg(obj.rotation.z).toFixed(1);
            document.getElementById('scaleX').value = obj.scale.x.toFixed(2);
            document.getElementById('scaleY').value = obj.scale.y.toFixed(2);
            document.getElementById('scaleZ').value = obj.scale.z.toFixed(2);
        }
        this.parent.transformControls.addEventListener('change', () => {
            if (!obj) return;
            if (document.getElementById('posX').value != null) {
                document.getElementById('posX').value = obj.position.x.toFixed(2);
                document.getElementById('posY').value = obj.position.y.toFixed(2);
                document.getElementById('posZ').value = obj.position.z.toFixed(2);
                document.getElementById('rotX').value = obj.rotation.x //THREE.MathUtils.radToDeg(obj.rotation.x).toFixed(1);
                document.getElementById('rotY').value = obj.rotation.y //THREE.MathUtils.radToDeg(obj.rotation.y).toFixed(1);
                document.getElementById('rotZ').value = obj.rotation.z //THREE.MathUtils.radToDeg(obj.rotation.z).toFixed(1);
                document.getElementById('scaleX').value = obj.scale.x.toFixed(2);
                document.getElementById('scaleY').value = obj.scale.y.toFixed(2);
                document.getElementById('scaleZ').value = obj.scale.z.toFixed(2);
            }
        });
        ['posX', 'posY', 'posZ'].forEach((id, i) => {
            document.getElementById(id).addEventListener('input', () => {
                if (document.getElementById('posX').value != null) {
                    const obj = this.parent.parenttransformControls.object;
                    if (obj) obj.position.set(
                        parseFloat(document.getElementById('posX').value),
                        parseFloat(document.getElementById('posY').value),
                        parseFloat(document.getElementById('posZ').value)
                    );
                }
            });
        });
        ['rotX', 'rotY', 'rotZ'].forEach((id, i) => {
            document.getElementById(id).addEventListener('input', () => {
                const obj = this.parent.transformControls.object;
                if (document.getElementById('rotX').value != null) {
                    if (obj) obj.rotation.set(
                        parseFloat(document.getElementById('rotX').value),
                        parseFloat(document.getElementById('rotY').value),
                        parseFloat(document.getElementById('rotZ').value)
                    );
                }
            });
        });
        ['scaleX', 'scaleY', 'scaleZ'].forEach((id, i) => {
            document.getElementById(id).addEventListener('input', () => {
                const obj = this.parent.transformControls.object;
                if (document.getElementById('scaleX').value != null) {
                    if (obj) obj.scale.set(
                        parseFloat(document.getElementById('scaleX').value),
                        parseFloat(document.getElementById('scaleY').value),
                        parseFloat(document.getElementById('scaleZ').value)
                    );
                }
            });
        });
    }
    setupShadowControls() {
        const light = this.lights?.keyLight || this.lights?.spotLight;
        if (!light || !light.castShadow) return;
        // Intensity
        document.getElementById('shadowIntensity')?.addEventListener('input', (e) => {
            light.intensity = parseFloat(e.target.value);
        });
        // Radius
        document.getElementById('shadowRadius')?.addEventListener('input', (e) => {
            light.shadow.radius = parseFloat(e.target.value);
            light.shadow.needsUpdate = true;
        });
        // Bias
        document.getElementById('shadowBias')?.addEventListener('input', (e) => {
            light.shadow.bias = parseFloat(e.target.value);
        });
        // Shadow Map Size
        document.getElementById('shadowSize')?.addEventListener('change', (e) => {
            const size = parseInt(e.target.value);
            light.shadow.mapSize.set(size, size);
            light.shadow.map.dispose(); // Force refresh
            light.shadow.needsUpdate = true;
        });
    }
    updateActive(cls, actcls) {
        if (actcls != null) {
            document.querySelectorAll(cls).forEach(p => {
                if (p.classList.contains("ins-active")) {
                    p.classList.remove("ins-active");
                }
            });
            actcls.classList.add("ins-active");
        }
    }
    EUiLightin() {
        var t = this
        t.updateActive(".insv-background-btn", document.querySelectorAll('.insv-background-btn.' + t.parent.config.lighting.lightmap.background)[0])
        this.updateBackgroundBody(this);
        document.getElementById('envListTH').src = this.parent.lighting_dir + this.parent.config.lighting.lightmap.url + ".webp"
        document.getElementById('envIntensity').value = this.parent.config.lighting.lightmap.intensity
        document.getElementById('envRotation').value = this.parent.config.lighting.lightmap.rotation_y
        document.getElementById('lightingPreset').value = this.parent.config.lighting.lightmap.lighting_preset
        document.getElementById('envList').value = this.parent.config.lighting.lightmap.url;
        this.parent.applyLightingPreset(this.parent.config.lighting.lightmap.lighting_preset);
        document.getElementById('lightingPreset')?.addEventListener('change', (e) => {
            this.parent.config.lighting.lightmap.lighting_preset = e.target.value
            this.parent.applyLightingPreset(e.target.value);
        });
        document.getElementById('envList')?.addEventListener('change', async (e) => {
            this.parent.config.lighting.lightmap.url = e.target.value
            document.getElementById('envListTH').src = this.parent.lighting_dir + this.parent.config.lighting.lightmap.url + ".webp"
            this.parent.updateenv();
        })
        document.getElementById('envIntensity')?.addEventListener('input', (e) => {
            this.parent.config.lighting.lightmap.intensity = parseFloat(e.target.value);
            this.parent.updateEnvMapIntensity();
        });
        document.getElementById('envRotation')?.addEventListener('input', (e) => {
            this.parent.config.lighting.lightmap.rotation_y = e.target.value;
            this.parent.updateenv(); // make sure to track currentEnvFile
        });
        document.getElementById('envRotY')?.addEventListener('input', (e) => {
            const deg = parseFloat(e.target.value);
            const rad = THREE.MathUtils.degToRad(deg);
            if (this.parent.envSphere) this.envSphere.rotation.y = rad;
        });
        /* document.getElementById('toggleEnvBtn')?.addEventListener('click', () => {
             this.isEnvEnabled = !this.isEnvEnabled;
             if (this.isEnvEnabled) {
                 this.updateenv(true);
             } else {
                 this.updateenv(true);
             }
             document.getElementById('toggleEnvBtn').textContent =
                 this.isEnvEnabled ? 'Disable Environment' : 'Enable Environment';
         });*/
    }
    updateBackgroundBody(t) {
        var e = document.querySelectorAll('.insv-background-btn.ins-active')[0]
        _send('/ins_ajax/home/app_test/epanel_lighting_' + e.dataset["m"] + '/do/_area/home/_alias/test/', e.dataset,
            (data) => {
                const slider = document.getElementById('insv-epanel-background-body');
                slider.innerHTML = data;
                t.backgroundUi()
            })
    }
    backgroundUi() {
        if (document.getElementById('envBlur') != null) {
            document.getElementById('envBlur').value = this.parent.config.lighting.lightmap.env_blur




            document.querySelectorAll('.range_inut input').forEach(element => {
                element.parentElement.querySelectorAll("span").forEach(selement => {
                    selement.textContent = element.value
                })
            })




        }
        if (document.getElementById('insv-ebackground-color') != null) {
            document.getElementById('insv-ebackground-color').value = this.parent.config.background_color.replace("0x", "#")
        }
    }
    setupEditorUIAj(status) {
        if (status == "epanel_settins") {
            this.ecamera_panel(this.parent);
            this.escale_panel(this.parent);
        } else if (status == "epanel_lighting") {
            this.EUiLightin();
        } else if (status == "epanel_post") {

console.log(status)

            this.parent.post.postUpdateUI();


        }



        var t = this
        document.querySelectorAll('.range_inut input').forEach(element => {
            element.parentElement.querySelectorAll("span").forEach(selement => {
                selement.textContent = element.value
            })
        })


        document.querySelectorAll('.insv-translate-btn').forEach(element => {
            element.addEventListener("click", function (e) {
                e.target.classList.add("ins-active");
                t.updateActive(".insv-translate-btn", e.target);
                t.parent.transformControls.setMode(e.target.dataset["m"])
            })
        })
    }
    gadd_remove(remove = false) {
        var t = this.parent;
        if (remove) {
            t.scene.remove(t.transformControls)
        } else {
            t.transformControls = new TransformControls(t.camera, t.renderer.domElement);
            t.transformControls.setTranslationSnap(0.1);
            t.transformControls.setRotationSnap(15);
            t.transformControls.addEventListener('change', () => t.composer.render());
            t.transformControls.addEventListener('dragging-changed', (e) => {
                t.controls.enabled = !e.value;
            });
            t.scene.add(t.transformControls);
            t.transformControls.attach(t.modelRoot);
        }
    }





    Post() {

        var t = this
        /*this.helper._on('.postRangeInput', "input", (e) => {


                t.parent.config.filters[e.dataset["m"]][e.dataset["p"]] = e.value
                console.log(t.parent.config.filters)

                t.parent.post.setupPostProcessing();

        })*/



    }

    UI() {

        var t = this

        t.Post()
        this.helper._on('.range_inut input', "input", (e) => {
            e.parentElement.querySelectorAll("span").forEach(selement => {
                selement.textContent = e.value
            })
        })
        this.helper._on(".insv-background-btn", "click", (e) => {
            t.updateActive(".insv-background-btn", e);
            t.parent.config.lighting.lightmap.background = e.dataset["m"];
            t.parent.updateenv();
            t.updateBackgroundBody(t);
        })
        this.helper._on("#envBlur", "input", (e) => {
            t.parent.config.lighting.lightmap.env_blur = e.value
            t.parent.applyLightingPreset(e.value);
            t.parent.updateenv();
        });
        this.helper._on("#insv-ebackground-color", "input", (e) => {
            t.parent.config.background_color = hashToInt(e.value)
            t.parent.updateBackGoundColor();
        })
        this.helper._on("#insv-update-btn", "click", (e) => {
            update_josn_file(t.parent.config.path, t.parent.config)
        })
        this.helper._on(".insv-get-epanel", "click", (e) => {
            t.gadd_remove(true);
            if (e.dataset["p"] == "epanel_settins") {
                t.gadd_remove()
            }
            t.updateActive('.insv-get-epanel', e)
            t.helper._ajax('/ins_ajax/home/app_test/' + e.dataset["p"] + '/do/_area/home/_alias/test/', e.dataset,
                (data) => {
                    const slider = document.getElementById('insv-epanel-body');
                    slider.innerHTML = data;
                    t.setupEditorUIAj(e.dataset["p"])
                })
        })
    }
}