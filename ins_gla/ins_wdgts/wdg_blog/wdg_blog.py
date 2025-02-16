from ins_kit._engine._bp import Widget


class WdgBlog(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        data_blog = self.ins._db._get_data("gla_blog", "*", update_lang=True)

        featured_blog = next(
            (d for d in data_blog if d.get("_order") == 1), None)
        remaining_blogs = [d for d in data_blog if d.get("_order") != 1][:4]

        data = remaining_blogs[:2]
        data3 = remaining_blogs[2:]

        p = "/ins_web/ins_uploads/"

        gstyle = "column-gap: 32px !important; row-gap: 32px !important; --flex-gap: 32px !important;"

        uidata = [
            {"start": "true", "class": "ins-flex ins-padding-2xl gla-container",
                "style": "padding-bottom:12px"},
            {"class": "ins-space-l"},
            {"_data": "Explore Our Stories", "_data-ar": "اكتشف قصصنا", "_trans": "true",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m"},
            {"class": "ins-col-grow"},
            {"_type": "a", "href": "blogs", "_data": "EXPLORE MORE <i class='lni ins-icon lni-arrow-right'></i>",
                "_data-ar": "اكتشف المزيد", "_trans": "true", "style": "width:250px",
                "class": "ins-button-l ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-start pro-blog-parent", "style": gstyle},
        ]

        if data:
            uidata.append(
                {"start": "true", "class": "ins-flex pro-blog-cont -ba"})
            for d in data:
                uidata += [
                    {"start": "true", "class": "ins-flex pro-blog-block",
                        "style": "width:100%; margin-bottom: 32px;"},
                    {"src": p + d.get("image", "style/n1.svg"),
                     "loading": "lazy", "_type": "img"},
                    {"_data": d.get("title", "Untitled"),
                     "class": "ins-col-12 ins-title-s ins-grey-color"},
                    {"end": "true"}
                ]
            uidata.append({"end": "true"})

        if featured_blog:
            uidata.append({"start": "true", "class": "ins-flex pro-blog-cont -bb",
                          "style": "height: 711px; position: relative; overflow: hidden;"})
            uidata += [
                {"start": "true", "class": "ins-flex pro-blog-block",
                    "style": "height: 100%; width: 100%; position: relative;"},
                {"src": p + featured_blog.get("image", "style/n5.svg"), "loading": "lazy",
                 "_type": "img", "style": "height: 100%; width: 100%; object-fit: cover;"},
                {"start": "true", "class": "ins-overlay",
                    "style": "position: absolute; bottom: 0; width: 100%; padding: 16px;"},
                {"_data": featured_blog.get(
                    "title", "Untitled"), "class": "ins-col-12 ins-title-s ins-white-color"},
                {"end": "true"},
                {"end": "true"}
            ]
            uidata.append({"end": "true"})

        if data3:
            uidata.append(
                {"start": "true", "class": "ins-flex pro-blog-cont -bc"})
            for d in data3:
                uidata += [
                    {"start": "true", "class": "ins-flex pro-blog-block",
                        "style": "width:100%; margin-bottom: 32px;"},
                    {"src": p + d.get("image", "style/n3.svg"),
                     "loading": "lazy", "_type": "img"},
                    {"_data": d.get("title", "Untitled"),
                     "class": "ins-col-12 ins-title-s ins-grey-color"},
                    {"end": "true"}
                ]
            uidata.append({"end": "true"})

        uidata.append({"end": "true"})
        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)
