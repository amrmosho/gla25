from urllib.parse import parse_qs
from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
from ins_plgs.plg_comments.plg_comments import PlgComments


class AppProductDetails(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    @property
    def _uid(self):
        return "1"
        

    def _pro_jaction(self, type="prolike"):
        pid = str(self.ins._server._post("pid"))

        pros = self.ins._users._get_settings('pro', uid=self._uid)
        r = ""

        if type not in pros:
            pl = []
        else:
            pl = pros[type]
            pl = list(set(pl))

        if pid in pl:
            pl.remove(pid)
            r = "0"
        else:
            pl.append(pid)
            r = "1"

        data = {type: pl}
        self.ins._users._updat_settings('pro', data, uid=self._uid)
        return r

    def _pro_action(self):

        ps = self.ins._server._post()
        if ps.get("a") == "like":
            return self._pro_jaction()

        elif ps.get("a") == "wishlist":
            return self._pro_jaction("wishlist")

    def _show_subtypes(self, subtypes, stys="", string=False):

        subtypes = {k: v for k, v in sorted(
            subtypes.items(), key=lambda item: int(item[1].get("order", float('1'))))}

        if subtypes:
            uidata = [
                {"start": "true", "class": "ins-flex ins-col-12"},
                {"_data": "Subtype", "_data-ar": "نوع فرعي", "_trans": "true",
                    "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "}
            ]
            for v, s in subtypes.items():
                sdata = self.ins._db._get_row(
                    "gla_product_types", "title,kit_lang", f"alias='{v}'", update_lang=True)
                active = "ins-active" if v == stys else ""
                uidata += [{"_data": sdata["title"], "name": "type", "data-name": v, "data-tid": s["id"],
                            "class": f"ins-button-s  -subtype-inner-btn ins-flex-center ins-strong-m -product-filter-input {active}"}]
            uidata.append({"end": "true"})
            if string:
                return self.ins._ui._render(uidata)
            else:
                return uidata

    def _slide_show_data(self, data):
        return "xxxxx"

    def _slide_show(self, data):

        if data["images"] != None:

            images = self.ins._json._decode(data["images"])
            a = "aaa"

        uidata = [
            {"start": "true", "class": "ins-flex ins-col-12  -side-mimg-cont "}
        ]

        uidata.append({"start": "true", "style": "    height: 555px; overflow: hidden;",
                      "class": "ins-flex ins-col-12  ins-m-col-12 ins-m-flex -main-img-cont"})

        uidata.append({"src": data["image_path"] + images[0]["url"], "loading": "lazy", "_type": "img",
                      "class": "  ins-radius-m ins-col-grow -main-img ins-m-col-12", "style": "max-width:100%;"})

        uidata.append({"end": "true"})

        uidata.append(
            {"start": "true", "class": "   ins-col-12 -th-bar"})

        uidata.append(
            {"start": "true", "class": "ins-flex ins-col-12  ins-m-col-12 ins-m-flex -small-imgs-cont"})

        aclass = "ins-active"

        if data["sketchfab"] != "":
            images.insert(2, {"url": data["sketchfab"], "type": "sketchfab"})

        if data["youtube"] != "":
            images.insert(2, {"url": data["youtube"], "type": "youtube"})

        for i in images:

            uidata.append(
                {"start": "true", "class": f"-side-img-cont ins-flex-center ins-text-center ins-radius-l  {aclass}"})

            if "type" in i and i["type"] == 'youtube':
                uidata.append({"src": "/ins_web/ins_images/icons/youtube.svg", "loading": "lazy", "_type": "img",
                               "data-src": i["url"], "data-type": i["type"],  "class": f" ins-radius-m -side-img {aclass}", "style": "height:85px"})

            elif "type" in i and i["type"] == 'sketchfab':
                uidata.append({"src": "/ins_web/ins_images/sketchfab-logo.svg", "loading": "lazy", "_type": "img",
                               "data-src": i["url"], "data-type": i["type"], "class": f" ins-radius-m -side-img {aclass}", "style": "height:85px;"})

            else:
                u = data["image_path"] + i["url"]

                uidata.append({"src": u, "loading": "lazy", "_type": "img",
                               "data-src": u, "data-type": "img",  "class": f" ins-radius-m  ins-radius-l -side-img {aclass}", "style": "width:100%;"})

            uidata.append({"end": "true"})
            aclass = ""

        uidata.append({"end": "true"})
        uidata.append({"end": "true"})

        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)

    def _tags(sel, data):
        tags = data.get("tags")
        tags = tags.split(",")
        r = []
        for t in tags:
            r.append(
                {"_data": t, "class": "ins-tag ins-grey-d-color ins-border ins-flex-center "})
        return r

    def update_view(self, id, views):

        sv = self.ins._server._get_session("us_views")
        if not sv:
            sv = []
        if id not in sv:
            sv.append(id)
            self.ins._server._set_session("us_views", sv)
            self.ins._db._update(
                "gla_product", {"views":  str(views+1)}, f"id={id}")

    def _user(self):

        u = self.ins._db._get_row("kit_user", "*", "id=1")

        uidata = [
            {"start":  "true", "class": "ins-col-12 ins-flex"},
            {"_data":  u["title"], "_trans": "true",
                "class": "ins-col-12  ins-m-col-12  ins-grey-d-color ins-title-20	 ins-strong-l"},
            {"class": "ins-line ins-col-12"},
            {"start":  "true", "class": "ins-col-4"},

            {"src":  self.ins._map.UPLOADS_FOLDER +
                u["image"], "_type": "img", "class": "ins-col-12  ins-m-col-12  "},
            {"end":  "true"},

            {"start":  "true", "class": "ins-col-8"},

            {"_data": "294 Products",
                "class": "ins-col-12 ins-font-m     ins-grey-color "},
            {"_data": "Since 2022",
                "class": "ins-col-12   ins-font-m  ins-grey-color "},

            {"end":  "true"},

            {"class": "ins-line ins-col-12"},


            {"start":  "true", "class": "ins-col-12 ins-flex-xenter"},


            {"start":  "true", "class": "ins-col-8"},
            {"_data": "Reputation", "class": "ins-col-12  ins-title-m  ins-grey-color "},

            {"_data": "Level: 3D Master",
                "class": "ins-col-12  ins-font-m  ins-grey-color ins-strong-m"},
            {"end":  "true"},



            {"_data": str(u["points"]), "class": " ins-border  ins-text-center  ins-rounded  ins-title-m  ins-primary-w ins-grey-color ",
             "style": "    height: 80px;width: 80px !important;line-height: 80px;"},
            {"end":  "true"},

            {"_data": "Positive", "class": "ins-col-6   ins-font-m   ins-grey-color "},
            {"_data": "7", "class": "ins-col-6  ins-success-color ins-font-l  i "},
            {"_data": "Negative", "class": "ins-col-6  ins-font-m    ins-grey-color "},
            {"_data": "2", "class": "ins-col-6   ins-danger-color ins-font-l  "},




            {"end":  "true"}
        ]

        return uidata

    def reviews(self):
        
        return "reviewsreviewsreviewsreviews"

    def comments(self ,data):
        
        return  PlgComments(self).out("_product" ,data["id"])

    def _ui(self, rq):
        data = self.ins._db._get_row("gla_product", "*", f"id={rq['id']}")

        self.update_view(rq['id'], data["views"])

        filter_data = {}
        stys = ""
        tys = ""
        if rq.get("type") and rq["type"]:
            parsed_data = parse_qs(rq["type"])
            filter_data = {key: value[0] for key, value in parsed_data.items()}
            stys = filter_data.get("subtypes", "")
            tys = filter_data.get("types", "")

        if not stys:
            if data["fk_product_category_id"] == 2:
                stys = "george"
            else:
                stys = "standard"

        if not tys:
            if data["fk_product_category_id"] == 2:
                tys = "royal"
            else:
                tys = "standard"

        if not data:
            return self.ins._ui._error("Product not found")
        uidata = [
            {"start": "true", "class": "ins-flex-start  gla-container ins-col-12 ins-padding-2xl ins-gap-m"},
        ]
        home_url = self.ins._server._url({}, ["mode", "id", "alias"])
        product_url = self.ins._server._url({}, ["mode", "id"])

        path = [
            {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
            {"_type": "a", "href": home_url, "_data": "Home /", "_data-ar": "الرئيسية /",
                "_trans": "true", "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_type": "a", "href": product_url, "_data": "Product /", "_data-ar": "منتجات /",
                "_trans": "true", "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": data["title"],
                "class": " ins-title-12	ins-grey-color ins-strong-m"},
            {"end": "true"}
        ]

        uidata += path

    # Images Container

        data["image_path"] = self.ins._map.UPLOADS_FOLDER
        p = data["image_path"]
        url = self.ins._server._url()
        self.ins._tmp._data_social_tags(
            {"title": data["title"], "des": data["title"], "img": data["image_path"]+data["th_main"], "url": url})
        self.ins._tmp._set_page_title(data["title"])

        # slide show
        uidata.append(
            {"start": "true", "class": "ins-flex ", "style": "width: calc(100% - 370px);"})
        uidata.append({"_data": self._slide_show(
            data), "class": "ins-flex ins-col-grow ins-padding ins-card", "style": ""})
        uidata.append({"class": "ins-space-s"})

        # title

        uidata.append(
            {"_data": data["title"], "class": "ins-col-12 ins-title-l ins-grey-d-color  ins-text-upper "})

        pros = self.ins._users._get_settings('pro', uid="1")
        lc = ""
        wl = ""
        if str(data["id"]) in pros["prolike"]:
            lc = " ins-success "

        if str(data["id"]) in pros["wishlist"]:
            wl = " ins-success "

        # actions
        uidata += [
            {"class": "ins-space-m"},
            {"_data": "<i class='ins-icons-bookmark ins-font-m'></i>  Add to wishlist",
                "class": f"ins-button  ins-button  ins-font-s -pro-action {wl}  ins-flex-center ", "data-a": "wishlist", "data-pid": data["id"]},
            {"class": "ins-col-grow"},
            {"_data": "<i class='ins-icons-eye ins-font-m'></i> " + str(data["views"]),
                "class": "ins-button ins-font-s  ins-flex-center "},
            {"_data": "<i class='ins-icons-heart ins-font-m'></i> 3",
                "class": f"ins-button  ins-font-s  -pro-action ins-flex-center {lc}", "data-a": "like", "data-pid": data["id"]},
            {"_data": "<i class='ins-icons-share-1 ins-font-m'></i> Share",
                "class": "ins-button  ins-font-s ins-flex-center"},
            {"_data": "<i  style='--color:#fff' class='ins-icons-info  ins-font-l'></i> Report",
                "class": "ins-button ins-danger  ins-font-s ins-flex-center  "},
            {"class": "ins-space-s"}
        ]

       # tabs
       
        com_count =self.ins._db._get_row("plg_comments" ,"count(id) as c" ,f"obj_id='{data["id"]}' and obj_type='_product'").get("c")
        uidata += [
            {"start": "true", "class": "ins-flex ins-card", "style": "width: 100%"},
            {"start": "true", "class": "ins-flex-center ins-bg-2",
                "style": "width: 100%"},
            
            
            
            {"_data": "details", "class": "ins-button -pro-d-tabs  ins-col-3 ins-primary",
                "data-s": "-details-cont"},
            
            
            
            {"_data": f"Comments ({com_count})", "class": "ins-button -pro-d-tabs  ins-col-3",
             "data-s": "-comments-cont"},
            
            
            
            {"_data": "Reviews (0)", "class": "ins-button   -pro-d-tabs ins-col-3",
             "data-s": "-reviews-cont"},



            {"end": "true"},




            {"_data": self.comments(data),  "class": "ins-col-12 -comments-cont ins-hidden  ins-flex   -pro-d-cont"},

            
            {"start": "true", "class": "ins-col-12 -pro-d-cont  ins-hidden  -reviews-cont"},
            {"_data": self.reviews() , "class": "ins-col-12 ins-flex "},

            {"end": "true"},



            {"start": "true", "class": "ins-col-12 -pro-d-cont -details-cont"},
            {"class": "ins-space-m"},
            {"_data": "Description", "class": " ins-title-m ins-strong-m "},
            {"class": "ins-space-m"},
            {"_data": data["des"], "class": "ins-col-12"},
            {"class": "ins-space-m"},            
            {"class": "ins-space-m"},

            {"_data": "Tags", "class": " ins-title-m ins-strong-m "},

            {"class": "ins-space-m"},

            {"_data": self._tags(data), "class": "ins-col-12 ins-flex"},

            {"class": "ins-space-m"},
            {"end": "true"},
            {"class": "ins-space-m"},
            {"end": "true"},


        ]

        uidata.append({"end": "true"})

        # Data Container
        uidata.append(
            {"start": "true", "class": "ins-flex ins-card ins-padding-l", "style": "width:350px"})

        uidata.append({"class": "ins-space-xs"})

        uidata.append({"_data":  str(data.get("buy_price", 9000)), "_view": "currency", "_currency_symbol": " EGP",
                      "_currency_symbol_ar": " جنيه",  "class": "ins-col-12   ins-title-l  ins-primary-d-color"})
        uidata.append({"class": "ins-space-s"})
        uidata.append({"class": "ins-line ins-col-12"})

        uidata.append(
            {"start": "true", "class": "ins-flex ins-col-12 ins-gap-o"})

        # Add to cart button
        lbtitle = "Cart"
        if self.ins._langs._this_get()["name"] == "ar":
            lbtitle = "السلة"

        uidata.append({"_data": "<img src='"+p+"style/cart.svg'></img> ADD TO CART", "_data-ar": "أضف إلى السلة", "_trans": "true", "data-lbtitle": lbtitle, "data-pid": str(
            data["id"]), "data-subtype": stys, "data-type": tys, "class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn", "style": "    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"end": "true"})

        # files FORMATS

        uidata.append({"start": "true", "class": "ins-flex ins-col-12 ins-card ins-primary-w",
                      "style": "border-radius:8px 8px 0 0 !important;"})

        uidata.append({"_data": "FORMATS", "_data-ar": "FORMATS", "_trans": "true",
                      "class": "ins-col-12  ins-grey-d-color ins-title-s	 ins-strong-l "})

        files = data.get("files", "[]")
        files = self.ins._json._decode(files)
        for f in files:
            uidata.append(
                {"start": "true", "class": "ins-tag ins-grey-d-color ins-border ins-flex-center "})
            if "native" in f:
                uidata.append(
                    {"_data": "Native", "class": "	 ins-primary ins-tag  "})
            uidata.append({"_data": f["type"], "class": ""})
            if "version" in f:
                uidata.append(
                    {"_data": "| " + f["version"], "class": "	 ins-strong-m "})
            if "renderer" in f:
                uidata.append(
                    {"_data": "| " + f["renderer"], "class": "	 ins-strong-m "})
            uidata.append({"end": "true"})

        uidata.append({"end": "true"})

        # Buy Card

        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-active ins-card ins-primary-bg  -open-panel",
                      "style": "border-radius: 0 0 8px 8px !important;position: relative;top: -8px;height: 65px;overflow: hidden;    border-top: 1px solid var(--primary-l)"})

        uidata.append({"_data": self._user(),
                      "class": "ins-col-12 ins-flex-end ins-m-col-12 "})

        uidata.append({"end": "true"})

        uidata.append({"class": "ins-space-s"})

        uidata.append({"class": "ins-space-s"})

        # Terms area
        uidata.append({"_data": "<img class=' icon-text-area' src='"+p +
                      "style/truck.svg '></img> non-overlapping Unwrapped UVs ",  "class": "ins-col-12 ins-grey-color ins-title-14"})
        uidata.append({"_data": "<img class=' icon-text-area'  src='"+p+"style/gift.svg'></img> UV Mapped",
                      "class": "ins-col-12 ins-grey-color ins-title-14 ins-m-col-11"})
        uidata.append({"_data": "<img class=' icon-text-area'  src='"+p+"style/gift.svg'></img> Polygonal Quads only Geometry",
                      "class": "ins-col-12 ins-grey-color ins-title-14 ins-m-col-11"})

        uidata.append({"class": "ins-space-s"})

        # Product Description

        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space-4xl"})
        # Related Products
        uidata.append({"start": "true", "class": "ins-flex  ins-col-12"})
        uidata.append({"_data": "Related Products", "_data-ar": "المنتجات ذات الصلة", "_trans": "true",
                      "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-text-upper", "style": "font-size:36px"})
        uidata.append({"class": "ins-space-l"})
        rpdata = self.ins._db._get_data(
            "gla_product", "*", f"   fk_product_category_id={data['fk_product_category_id']} and id <>{data['id']} limit 0,4 ", update_lang=True)
        uidata.append(
            {"start": "true", "class": "ins-flex-space-between ins-flex-valign-start ins-col-12"})
        for d in rpdata:
            uidata += ELUI(self.ins).shop_pro_block(d,
                                                    self.ins._server._url({"id": d["id"]}, ["filter", "type"]))

        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space-4xl"})
        return self.ins._ui._render(uidata)

    def out(self):

        self.app._include("style.css")
        self.app._include("script.js")
        self.app._include("slide_show.js")

        rq = self.ins._server._req()
        return self._ui(rq)
