

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
        return  x
    def ui(self):

        uidata = [
            {"start": "true", "class": "ins-white"},
            
            {"_data":"Gold  calculator" ,"class":"ins-title-2xl ins-padding-xl ins-strong-m ins-text-upper"},

            
            {"end":"true"}

        ]
        r = self.ins._ui._render(uidata)
        return r

    def out(self):

        return self.search()  
