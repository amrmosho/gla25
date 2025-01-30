from ins_gla.ins_apps.app_users.app_users_orders import AppUsersOrders
from ins_kit._engine._bp import App
from ins_gla.ins_kit._elui import ELUI


class AppUsers(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def u(self, mode):

        return self.ins._server._url({"mode": mode},)

    def header(self, g):

        hc = ""
        pc = ""
        oc = ""
        sc = ""

        if g.get("mode") == "profile":
            pc = " ins-gold-bg "
        elif g.get("mode") == "settings":
            sc = " ins-gold-bg "
        elif g.get("mode") == "order":
            oc = " ins-gold-bg "
        else:
            hc = " ins-gold-bg "

        ui = [{"start": "true", "class": "ins-col-6 ins-flex-end"},
              {"_data": "<i class='lni ins-font-l lni-home-2'></i>Home",
                  "class": f"ins-button-s  ins-text-upper {hc}  ins-flex", "_type": "a", "href": self.u("")},
              {"_data": "/", "class": " "},
              {"_data": "<i class='lni ins-font-l lni-user-4'></i>My Profile",
                  "class": f"ins-button-s ins-text-upper {pc}  ins-flex", "_type": "a", "href": self.u("profile")},
              {"_data": "/", "class": " "},
              {"_data": "<i class='lni ins-font-l lni-basket-shopping-3'></i>My Orders",
                  "class": f"ins-button-s  ins-text-upper {oc} ins-flex ", "_type": "a", "href": self.u("order")},
              {"_data": "/", "class": "  "},
              {"_data": "<i class='lni ins-font-l lni-gears-3'></i>Settings",
                  "class": f"ins-button-s ins-text-upper   {sc} ins-flex ", "_type": "a", "href": self.u("settings")},
              {"end": "true"}

              ]
        return ELUI(self.ins).page_title("Users Panel", [{"_data": "Users Panel / ", "href": "/puser"}, {"_data": "Profile"}], ui)

    def orders(self, g):
        return AppUsersOrders(self.app).orders(self.ins)

    def profile(self, g):
        return "profile"

    def home(self, g):
        user = self.ins._db._get_row("kit_user")
        uidata = [
            {"start": "true", "class": "ins-col-12  "},


            {"start": "true", "class": "gla-container ins-flex-start "},



            {"start": "true", "class": "  ins-flex-start  ins-padding-2xl  ins-col-7"},

            {"_data": f'<i class="lni ins-font-2xl lni-user-4"></i>  Welcome {
                user.get("title")}', "class": "ins-title-m ins-col-12"},
            {"_data": f' <i class="lni ins-font-l lni-phone"></i>  +0215555202408',
                "class": " ins-col-12"},




            {"start": "true", "class": "  ins-col-12 ins-card ins-gap-20  ins-flex ins-white   "},


            {"start": "true", "class": "  ins-col-12 ins-border ins-radius-xl   ins-flex   ins-padding-l"},
            {"_data": f' Last Order  details ',
                "class": " ins-col-12  ins-grey-d-color ins-title-s	 ins-strong-l "},
            {"_data": f' Orders Count ',
                "class": " ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"},
            {"_data": f' 15 ',
             "class": " ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"},
            {"_data": f' Items Count ',
                "class": " ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"},
            {"_data": f' 15 ',
                "class": " ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"},
            {"class": "ins-line ins-col-12"},
            
            
            {"_data": f' Orders Total ',
                "class": " ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"},
            {"_data": f'EGP 3000 ',
                "class": " ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"},



            {"end": "true"},
            
             {"start": "true", "class": "  ins-col-12 ins-border ins-radius-xl   ins-flex   ins-padding-l"},
            {"_data": f' Orders details ',
                "class": " ins-col-12  ins-grey-d-color ins-title-s	 ins-strong-l "},
            {"_data": f' Orders Count ',
                "class": " ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"},
            {"_data": f' 15 ',
             "class": " ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"},
            {"_data": f' Items Count ',
                "class": " ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"},
            {"_data": f' 15 ',
                "class": " ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"},
            {"class": "ins-line ins-col-12"},
            
            
            {"_data": f' Orders Total ',
                "class": " ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"},
            {"_data": f'EGP 3000 ',
                "class": " ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"},



            {"end": "true"},
            
            
            
            
            {"_data": f' <i class="lni ins-font-l ins-danger-color lni-share-2"></i>  Logout',
                "class": " ins-col-12 ins-button ins-danger-color"},


            {"end": "true"},


            {"end": "true"},


            {"start": "true", "class": "  ins-col-5  ins-flex ins-white   ins-padding-2xl"},



            {"start": "true", "class": "  ins-col- 12 ins-primary-w   ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a",  "_data": f'<i class="lni ins-font-l lni-home-2"></i>  Home ',
                "class": " ins-title-s ins-col-12"},
            {"_data": f'Users Panel home des Users Panel home des Users Panel home des ',
                "class": "ins-col-12 ins-padding-xl   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},





            {"start": "true", "class": "  ins-col- 12 ins-primary-w    ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a",  "_data": f'<i class="lni ins-font-l lni-user-4"></i>  My Profile ',
                "class": " ins-title-s ins-col-12"},
            {"_data": f'Users Panel home des Users Panel home des Users Panel home des ',
                "class": "ins-col-12 ins-padding-xl   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},



            {"start": "true", "class": "  ins-col- 12    ins-primary-w  ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a",  "_data": f'<i class="lni ins-font-l lni-basket-shopping-3"></i>  My Orders ',
                "class": " ins-title-s ins-col-12"},
            {"_data": f'Users Panel home des Users Panel home des Users Panel home des ',
                "class": "ins-col-12 ins-padding-xl   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},




            {"start": "true", "class": "  ins-col- 12  ins-primary-w   ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a",  "_data": f'<i class="lni ins-font-l lni-gears-3"></i>  Settings ',
                "class": " ins-title-s ins-col-12"},
            {"_data": f'Users Panel home des Users Panel home des Users Panel home des ',
                "class": "ins-col-12 ins-padding-xl   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},





            {"end": "true"},


            {"end": "true"},
            {"end": "true"},




        ]

        return self.ins._ui._render(uidata)

    def settings(self, g):
        return "settings"

    def out(self):
        g = self.ins._server._get()

        r = self.header(g)

        if g.get("mode") == "profile":
            r += self.profile(g)
        elif g.get("mode") == "settings":
            r += self.settings(g)
        elif g.get("mode") == "order":
            r += self.orders(g)
        else:
            r += self.home(g)
        return r
