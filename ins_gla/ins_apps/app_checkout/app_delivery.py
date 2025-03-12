from ins_gla.ins_kit._elui import ELUI
from ins_gla.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
p = "/ins_web/ins_uploads/"

class AppDelivery(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user= Gusers(app.ins)

    
    @property
    def session_name(sel):
        return "glaproducts"
    


    @property
    def session_address_name(sel):
        return "glaaddress"


    
    def _store_area_ui(self,string=True):
        stores = self.ins._db._get_data("gla_address","*",update_lang=True)

        uidata=[{"start":"true","class":"ins-col-12 ins-flex  -addresses-area"}]
        uidata.append({"_data":"Our Stores","_data-ar":"متاجرنا","_trans":"true","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        asession = self.ins._server._get_session(self.session_address_name)
        if type(asession) != dict:
           asession = {"type":"store","id":"-1"}
        for a in stores:
           img = "style/radio.svg"
           if str(a["id"]) == str(asession["id"])  and asession["type"] == "store":
              img = "style/radio_checked.svg"
           uidata.append({"start":"true","class":"ins-col-12 ins-card ins-flex-valign-center ins-padding-s -address-cont","style":"    line-height: 20px;"})
           uidata.append({"_data":"<img data-aid = "+f"{a['id']}"+" class='-address-btn' data-type='store' src='"+p + img+"'></img>","class":"ins-flex ins-col-1"})
           uidata.append({"start":"true","class":"ins-col-11 ins-flex"})
           uidata.append({"_data": a["title"],"class":" ins-title-s ins-strong-m ins-grey-d-color ins-col-12","style":"line-height: 24px;"})
           uidata.append({"_data": a["address"],"class":"ins-grey-color ins-col-12 ins-title-12","style":"line-height: 16px;"})
           uidata.append({"_data": f"Phone: {a['phone']} | WhatsApp: {a['whatsapp']} | Email:  {a['email']}" ,"_data-ar": f"هاتف: {a['phone']} | واتساب: {a['whatsapp']} | بريد الكتروني:  {a['email']}" ,"_trans":"true","class":"ins-grey-d-color ins-col-12   ins-title-14"})
           uidata.append({"end":"true"})
           uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        if string == False:
            return uidata
        else:
            return self.ins._ui._render( uidata)
    
    
    def _addresses_area_ui(self,string=True):
        rsdata=  self.user._check()
        addesses = self.ins._db._get_data("gla_user_address","*",f"fk_user_id = '{rsdata['id']}' order by kit_created ASC",update_lang=True)
        uidata=[{"start":"true","class":"ins-col-12 ins-flex  -addresses-area"}]
        uidata.append({"_data":"Saved Address","_data-ar":"العناوين المحفوظة ","_trans":"true","class":"ins-col-9 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_data": "Add Address","_data-ar":" إضافة عنوان","_trans":"true","class": "ins-button-s -add-address ins-text-center ins-strong-m ins-col-3 ins-gold-bg  ins-text-upper"})
        asession = self.ins._server._get_session(self.session_address_name)
        if type(asession) != dict:
           asession = {"type":"delivery","id":"-1"}
        
        if addesses:
           for a in addesses:
              img = "style/radio.svg"
              if str(a["id"]) == str(asession["id"]) and asession["type"] == "delivery":
                 img = "style/radio_checked.svg"
              uidata.append({"start":"true","class":"ins-col-12 ins-card ins-flex-valign-center ins-padding-s -address-cont","style":"    line-height: 20px;"})
              uidata.append({"_data":"<img data-aid = "+f"{a['id']}"+" class='-address-btn' data-type='delivery' src='"+p + img+"'></img>","class":"ins-flex ins-col-1"})
              uidata.append({"start":"true","class":"ins-col-9 ins-flex"})
              uidata.append({"_data": a["title"],"class":" ins-title-s ins-strong-m ins-grey-d-color ins-col-12","style":"line-height: 24px;"})
              uidata.append({"_data": a["address"],"class":"ins-grey-color ins-col-12 ins-title-12","style":"line-height: 16px;"})
              uidata.append({"_data": "Mobile: "+a["phone"] + " | Email: "+ a["email"],"class":"ins-grey-d-color ins-col-12  ins-title-14"})
              uidata.append({"end":"true"})
              uidata.append({"start":"true","class":"ins-col-2 ins-flex-end"})
              uidata.append({"_data":"<i  class='-update-address  _a lni lni-pencil-1' data-aid = "+ str(a["id"])+"></i>","class":"ins-text-center"})
              uidata.append({"_data":"<i  class='lni lni-trash-3 _a_red'></i>","data-aid":a["id"],"class":"ins-text-center -remove-address-btn"})
              uidata.append({"end":"true"})
              uidata.append({"end":"true"})
        else:
           uidata.append({"start":"true","class":"ins-col-12 ins-card ins-padding-m ins-flex-center"})
           uidata.append({"_data":"No saved addresses yet","_data-ar":"لا يوجد عناوين محفوظة","_trans":"true"})
           uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        if string == False:
            return uidata
        else:
            return self.ins._ui._render( uidata)
    
    
    def items_area(self,string= False):
        ## Items Area
        uidata = []
        sedata=self.ins._server._get_session(self.session_name)
        rq = self.ins._server._req()
        subtotal = 0
        chargs = 0
        for k,v in sedata.items():
            subtotal+= float(v["price"]) * float(v["count"])
            uidata+= ELUI(self.ins).small_pro_block(v)
            uidata.append({"class":"ins-space-m"})
        uidata.append({"class":"ins-space-m"})
        uidata.append({"class":"ins-line ins-col-12"})
        uidata.append({"class":"ins-space-m"})
        uidata.append({"_data": "Voucher", "_data-ar":" قسيمة","_trans":"true","class": "ins-col-12  ins-grey-d-color ins-strong-m  "})
        uidata.append({"_type": "input","type":"text","placeholder":"code","placeholder-ar":" رمز","_trans":"true","name":"voucher","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"class":"ins-space-xl"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12 -fees-info ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details","_data-ar":"تفاصيلك","_trans":"true", "class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal", "_data-ar":"المجموع الفرعي","_trans":"true","class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(subtotal),"data-value" : subtotal,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -subtotal-text"})
        pclass = "ins-hidden"

        total = subtotal  
        uidata.append({"start": "true", "class": f"-online-payment-fee  ins-col-12 ins-flex {pclass}"})
        uidata.append({"_data": "Online payment fee","_data-ar": "رسوم الدفع عبر الإنترنت", "_trans":"true","class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(chargs),"data-value" : chargs,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -chargs-text"})
        uidata.append({"end": "true"})
        uidata.append({"_data": "Shipping", "_data-ar":" شحن","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        if total > 200000:
          uidata.append({"_data": "Free","_data-ar": "مجاني","_trans":"true","data-value" : 0, "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
        else:
          uidata.append({"_data": "200","data-value" : 200,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end -shipping-text"})
          total +=200
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "_data-ar":" المجموع","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":  str(total),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -total-text"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})
        back_url = self.ins._server._url({"mode":"cart"},["id"])
        lbtitle = "Change in price"
        if self.ins._langs._this_get()["name"] == "ar":
         lbtitle = "تغير في السعر"
        uidata.append({"data-lbtitle":lbtitle,"data-url":"/checkout/payment/","_data": "Procced to payment <img src='"+p+"style/right_arrow.svg'></img>", "_data-ar":" انتقل إلى الدفع","_trans":"true","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d -payment-btn  ins-text-upper","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"href":back_url,"_type":"a","_data": " <img src='"+p+"style/left_arrow.svg'></img> Back", "_data-ar":"رجوع","_trans":"true","class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   ins-col-12 ins-title-xs	","style":"    height: 46px;"})
        uidata.append({"_data": "Your info will be saved to a Shop account. By continuing, you agree to Shop’s <a>Terms of Service</a> and acknowledge the  <a>Privacy Policy</a>.", "_data-ar":"سيتم حفظ معلوماتك في حساب المتجر. من خلال الاستمرار، فإنك توافق على سياسة المتجر","_trans":"true","class": " ins-col-12 ins-grey-color ","style":"line-height:24px"})
        
        
        if string:
         return self.ins._ui._render( uidata)
        else:
         return uidata



    def ui(self):
        asession = self.ins._server._get_session(self.session_address_name)
      ## Addresses Area
        delivery_text = "Home Delivery" 
        store_text = "Pickup in Store"

        if self.ins._langs._this_get()["name"] == "ar":
            delivery_text = " توصيل الطلبات"
            store_text = "الاستلام من المتجر"
        uidata=[{"start":"true","class":"ins-col-7 ins-flex ins-padding-2xl"}]
        uidata.append({"_data":"Select delivery type","_data-ar":"حدد نوع التسليم","_trans":"true","class":"ins-col-12 ins-title-s ins-strong-m ins-grey-d-color "})
        atype_btns= [{"_data": f"<img class='-address-radio-btn' src= {p}style/radio_checked.svg></img> {delivery_text}", "data-type":"delivery","class": f"ins-button-s ins-text ins-col-6  ins-gold-bg ins-flex-center -delivery-type-btn ins-strong-m ins-gold-bg"},
                {"_data": f"<img class='-address-radio-btn' src= {p}style/radio.svg></img> {store_text}","data-type":"store","class": f"ins-button-s  ins-col-6 ins-flex ins-flex-center -delivery-type-btn ins-strong-m inactive insactive"}
                ]
        if type(asession) == dict and "type" in asession and  asession["type"] == "store":
         atype_btns= [{"_data": f"<img class='-address-radio-btn' src= {p}style/radio.svg></img> {delivery_text}", "data-type":"delivery","class": f"ins-button-s ins-text ins-col-6 ins-flex-center -delivery-type-btn ins-strong-m inactive"},
                {"_data": f"<img class='-address-radio-btn' src= {p}style/radio_checked.svg ></img>{store_text}","data-type":"store","class": f"ins-button-s  ins-col-6 ins-flex ins-flex-center -delivery-type-btn ins-strong-m  ins-gold-bg"}
                ]
        uidata+=atype_btns
        uidata.append({"class":"ins-space-l"})
        asession = self.ins._server._get_session(self.session_address_name)
        if type(asession) == dict and "type" in asession and  asession["type"] == "store":
           uidata+=self._store_area_ui(False)
        else:
           uidata+=self._addresses_area_ui(False)
        uidata.append({"end":"true"})
        ## Items Area
        uidata.append({"start":"true","class":"ins-col-5 ins-gap-o ins-flex   ins-padding-2xl","style":"background:white;   border-left: 1px solid var(--primary-l);"})
        uidata+=self.items_area()
        uidata.append({"end":"true"})
        uidata.append({"class":"ins-space-xl"})
        uidata.append({"end":"true"})
        return uidata
   
   

    def out(self):
         return self.ui()
   