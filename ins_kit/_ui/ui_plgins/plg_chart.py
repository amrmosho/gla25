from ins_kit._ui.ui import Ui


class PlgChart(Ui):

    def _ui(self, ops):

        # d= self.ins._json._encode(d)
        id = self.ins._data._unid
        o=""
        if "options" in ops:
            o= ops.get("options" ,"")
            #o= self.ins._json._encode(o)
        dss :list= ops["data"]
     
     
        return f'<div data-insaction="plgin" data-type="{ops["type"]}" data-ops="{o}"  data-j="{dss}" class="insaction {ops.get("class","")}" data-plgin="ins_plg_py_chart"  id="_{id}" style="min-width: 100px; min-height: 200px;{ops.get("style","")}">chart</div>'

    def render(self, ops):

        return self._ui(ops)
