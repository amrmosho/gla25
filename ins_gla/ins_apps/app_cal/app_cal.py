from ins_kit._engine._bp import App


class AppCal(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def d(self):
        return self.ins._json._file_read("test/a.json")

    def step(self, ops):
        data = self.d()
        r = {}
        lt = (ops["total"]/ops["count"])
        lf = lt-(lt/ops["offset"])
        for d in data:
            if float(d["Price"]) < lt and float(d["Price"]) > lf:
                r[d["id"]] = d
        x = 0
        xr = {}
        for k, a in r.items():
            if float(a["Price"]) > x:
                x = float(a["Price"])
                xr = a
        return xr

    def level(self, total, count=5, fill=[]):
        ops = {"offset": 10, "count": count, "total": total}
        d = self.step(ops)
        fill.append(d)
        count = count - 1
        if "Price" not in d:
            return fill
        if count > 0:
            nt = total - float(d["Price"])
            self.level(nt, count, fill)
        return fill

    def search(self):
        total = 500000
        ops = {"f": 4, "t": 9}
        xl = 0
        for i in range(ops["f"], ops["t"]+1):
            l = self.level(total, i, [])
            lc = 0
            rl = {}
            for k in l:
                if "Price" in k:
                    lc += float(k["Price"])
                    if int(k["id"]) in rl:
                        rl[int(k["id"])]["count"] += 1
                    else:
                        k["count"] = 1
                        rl[int(k["id"])] = k
            if lc > xl:
                xl = lc
                x = rl
        return x

    def ui(self):
        uidata = []
        title = [
            {"start": "true", "class": "ins-white"},
            {"start": "true", "class": " ins-flex-center gla-container ins-padding-xl "},
            {"_data": "Gold calculator", "style": "position: absolute;left: 20px;",
                "class": "ins-title-l ins-padding-xl ins-strong-m ins-text-upper"},
            {"start": "true", "class": "  ins-flex  ins-border ins-padding-m ins-radius-m"},
            {"_data": "E£", "class": "ins-border-end ins-padding-m ins-padding-h",
                "style": "height: 24px;line-height: 24px;"},
            {"_type": "input", "placeholder": "0000,00",
                "type": "text", "class": "ins-input-none"},
            {"_data": "<i class='lni ins-white-color lni-arrow-right'></i>",
                "class": "ins-button-s  ins-gold"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
        ]
        uidata += title
        body = [
            {"class": "ins-space-xl"},
            {"start": "true", "class": "ins-white ins-radius-xl ins-border  gla-container "},
            {"start": "true", "class": " ins-flex ins-padding-xl  ins-col-12"},
            {"_data": " 1 - 3 items",
                "class": "ins-font-l ins-padding-xl ins-strong-l ins-text-upper"},
            {"start": "true", "class": " ins-radius-l ins-border ins-col-12 ins-flex  ",
                "style": "overflow: hidden;"},
            {"start": "true", "class": "  ins-col-grow"},
            {"end": "true"},
            {"start": "true", "class": "ins-gold-bg ", "style": "width:360px"},
            {"_data": "true"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
        ]
        uidata += body
        r = self.ins._ui._render(uidata)
        return r

    def out(self):
        return self.ui()
