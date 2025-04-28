
from ins_kit._engine._bp import Widget


class WdgSlideshow(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        self.widget._include("shstyle.css")

        uidata = [
            {"start":"true","class":"ins-col-12 img-bg-air  ins-flex-center","style":"height: 340px;"},
            {"start":"true","class":" serch_cont ins_mod_search  ins-container","style":"position: relative;"},
            {"_type":"h2","_data":"CG Marketplace by the World's Best 3D Artists","class":"ins-strong ins-primary-color","style":"    margin-bottom: 20px;"},
            {"_type":"h4","_data":"Find the exact right 3D content for your needs, including AR/VR, gaming, advertising, entertainment and 3D printing","class":"ins-strong-m"},
            {"_type":"input","type":"text","pclass":"ins-co-12"},
            {"end":"true"},
            {"end":"true"}]
        return self.ins._ui._render(uidata)
