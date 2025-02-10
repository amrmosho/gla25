from ins_kit.ins_parent import ins_parent
import re


class Ui(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def __get_plgin(self, name, attrs, parent="render"):
        if "not_plgin" in attrs and attrs["not_plgin"] == True:
            del attrs["not_plgin"]
            return self.tag(attrs)
        else:
            _class_name = self.ins._map._get_class_name(name)
            _path = f"ins_kit._ui.ui_plgins.{name}"
            exec(f"from {_path} import {_class_name}")
           # _class = eval(f"{_class_name}(self.ins)")

            return eval(f"{_class_name}(self.ins).{parent}(attrs)")

    def _render(self, data):
        r = ''
        for v in data:
            r += self._item(v)
        return r

    def _item(self, attrs):

        r = ""

        if "_trans" in attrs:
            attrs = self.ins._langs._render_tags(attrs)
          
           
        plgs = ["wdgt", "input", "app", "table", "panel"]
        if "_type" in attrs:
            if "not_plgin" not in attrs or attrs["not_plgin"] != True:
                if attrs["_type"] == "textarea":
                    attrs["_type"] = "input"
                    attrs["type"] = "textarea"

            if attrs["_type"] == "select" or attrs["_type"] == "list":
                r = self.__get_plgin("plg_select", attrs)

            elif attrs["_type"] in plgs:
                r = self.__get_plgin(f"plg_{attrs["_type"]}", attrs)

            elif attrs["_type"] in "method":
                area = self.ins._this._area["url"]
                type = "ins_apps"

                if "type" in attrs:
                    type = attrs["type"]

                if "area" in attrs:
                    area = attrs["area"]
                ds = attrs["_data"].split(".")

                _path = f'{area}.{type}.{ds[0]}.{ds[0]}'
                _class_name = self.ins._map._get_class_name(ds[0])
                exec(f"from {_path} import {_class_name}")
                r = eval(f"{_class_name}.{ds[1]}(self.ins)")

            else:
                r = self.tag(attrs)

        else:
            r = self.tag(attrs)

        return r

    def clean_html(self, text: str):
        """Cleans HTML tags from a string.

        Args:
            text (str): The input string.

        Returns:
            str: The cleaned string without HTML tags.
        """

        cleaned = re.sub(r'<.*?>', '', text)
        cleaned = cleaned.replace("\n", "").replace("\r", "").replace("\t", "")
        cleaned = re.sub(r"\s+", " ", cleaned)

        return cleaned

    def _format(self, ops, data):
        if ops["_view"] == "limit":
            l = 20
            if "limit_ops" in ops:
                l = int(ops["limit_ops"])
            rv = self.clean_html(data)
            if len(rv) > l:
                rv = f"<span title='{rv}'>{rv[:l]}...</span>"
        elif ops["_view"] == "select":
            ops["value"] = str(data)
            rv = self.__get_plgin("plg_select", ops, "trans")
        elif ops["_view"] == "color":
            rv = f"<div style='color:{data}'>{data} </div>"
        elif ops["_view"] == "date":
            rv = self.ins._date._ui()._format(data, "date")
        elif ops["_view"] == "datetime":
            rv = self.ins._date._ui()._format(data)
        elif ops["_view"] == "dbdate":
            rv = self.ins._date._format(data, "date")
        elif ops["_view"] == "dbdatetime":
            rv = self.ins._date._format(data)
        elif ops["_view"] == "currency":
            if "_currency_symbol" in ops:
                n = self.ins._data._format_currency(float(data), symbol=False)
                rv = f"{n}{ops["_currency_symbol"]}"
            else:
                rv = self.ins._data._format_currency(float(data))
        elif ops["_view"] == "image":
            rv = f"<a target='_blank' href='{self.ins._map.UPLOADS_FOLDER}{
                data}'><img style='max-width:100%;max-height:250px' src='{self.ins._map.UPLOADS_FOLDER}{data}'/></a>"

        else:
            rv = data

        return rv

    def tag(self, attrs):
        if "_trans" in attrs:
            for a in attrs:
                attrs = self.ins._langs._render_tags(attrs)
           


        if "_type" in attrs:
            my_type = attrs["_type"]
            del attrs["_type"]
        else:
            my_type = "div"

        if "_data" in attrs:
            if type(attrs["_data"]) is list:
                my_data = self._render(attrs["_data"])
            elif type(attrs["_data"]) is dict:
                my_data = self._render([attrs["_data"]])
            else:
                my_data = attrs["_data"]

            if "_view" in attrs:
                my_data = self._format(attrs, my_data)

            del attrs["_data"]
        else:
            my_data = ""

        attr_str = " ".join(f"{key}='{value}'" for key, value in attrs.items())

        if attr_str:
            attr_str = f" {attr_str}"

        if my_type in ["img", "br", "hr", "meta", "link"]:
            return f"<{my_type}{attr_str} />"

        else:
            r = ""
            if "end" not in attrs or (attrs["end"] != True and attrs["end"] != "true" and attrs["end"] != "True"):
                r += f"<{my_type}{attr_str}>"
                r += my_data

            if "start" not in attrs or (attrs["start"] != True and attrs["start"] != "true" and attrs["start"] != "True"):
                r += f"</{my_type}>"
        return r
