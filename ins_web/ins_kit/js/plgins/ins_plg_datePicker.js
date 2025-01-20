/**
 *
 * @returns {undefined}
 */
export class ins_plg_datePicker {
    options = {};
    _OInput = null;
    _OBtn = null;
    _month = 0;
    lang = {
        "ar": {
            months: [
                "يناير",
                "فبراير",
                "مارس",
                "ابريل",
                "مايو",
                "يونيو",
                "يوليو",
                "أغسطس",
                "سبتمبر",
                "أكتوبر",
                "نوفمبر",
                "ديسمبر",
            ],
            days: [
                "الاحد",
                "الاثنين",
                "الاثنين",
                "الاربعاء",
                "الخميس",
                "الجمعة",
                "السبت",
            ],
        },
        en: {
            months: [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "Novemeber",
                "Decemeber",
            ],
            days: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
        }


    }



    constructor(o) {
        this.options = o;
        this._updateDate();


    }


    _updateDate() {

        this._OInput = this.options.o;
        this._OParent = this.options.o._parent();
        this._OBtn = this._OParent._find(".ins-calendar-btn");



        this._month = 2;


    }


    _calender = null;



    _ui() {
        var _slef = this;
        var c = ""
        var cont = ins(
            ins()._ui._create(
                "div",
                "", { class: " ins-col-12 ins-input-slide-panel   ins_opend " + c }, []
            )
        );
        _slef._calender = cont;

    }

    _isOpend = false;
    _toggleShow() {
        if (this._calender == null) {
            this._ui();
            this._OInput._append_befor(this._calender);

        }





        if (this._isOpend) {


            this._OParent._removeclass("ins_opend")
        } else {

            this._OParent._addclass("ins_opend")
        }
        this._isOpend = !this._isOpend;

    }








    _actions() {
        var _slef = this;
        _slef._OBtn._on("click", function() {
            _slef._toggleShow();
        })

    }

    _out() {

        this._actions();

    }
}