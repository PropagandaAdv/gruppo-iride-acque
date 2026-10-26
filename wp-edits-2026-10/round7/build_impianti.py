import json, os, sys, urllib.parse
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'impianti')
os.makedirs(OUT, exist_ok=True)

def tag(id_, name, settings=None):
    s = urllib.parse.quote(json.dumps(settings or {}, separators=(',', ':')), safe='')
    return '[elementor-tag id="%s" name="%s" settings="%s"]' % (id_, name, s)

def field(id_, key):
    return tag(id_, 'post-custom-field', {"key": "", "custom_key": key})

MONT = {"typography_typography": "custom", "typography_font_family": "Montserrat"}

def te(id_, dyn, color, size, weight, cls, lh=1.6, msize=None):
    s = dict(MONT, **{"editor": "", "__dynamic__": {"editor": dyn}, "text_color": color,
         "typography_font_weight": weight, "typography_font_size": {"unit": "px", "size": size},
         "typography_line_height": {"unit": "em", "size": lh}, "_css_classes": cls})
    if msize: s["typography_font_size_mobile"] = {"unit": "px", "size": msize}
    return {"id": id_, "elType": "widget", "widgetType": "text-editor", "settings": s, "elements": []}

def box(v): return {"unit": "px", "top": str(v[0]), "right": str(v[1]), "bottom": str(v[2]), "left": str(v[3]), "isLinked": False}

LOOP_CSS = """selector{overflow:hidden;height:100%;}
selector .iah-imp-img img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block;}
selector .iah-imp-lbl p{margin:0;text-transform:uppercase;letter-spacing:.12em;}
selector .iah-imp-sub p{margin:10px 0 0;}
selector .iah-imp-txt p{margin:14px 0 0;}
selector .iah-imp-tag p{margin:18px 0 0;padding-top:16px;border-top:1px solid rgba(9,23,31,.12);}
selector .iah-imp-lbl p:empty,selector .iah-imp-sub p:empty,selector .iah-imp-tag p:empty{display:none;}
selector .elementor-heading-title{margin:12px 0 0;}"""

loop_item = [{
    "id": "1a2b3c4d", "elType": "container", "isInner": False,
    "settings": {"content_width": "full", "flex_direction": "column", "flex_gap": {"unit": "px", "size": 0, "column": "0", "row": "0"},
                 "background_background": "classic", "background_color": "#FFFFFF",
                 "border_radius": {"unit": "px", "top": "28", "right": "28", "bottom": "28", "left": "28", "isLinked": True},
                 "border_border": "solid", "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
                 "border_color": "rgba(9,23,31,.10)",
                 "box_shadow_box_shadow_type": "yes",
                 "box_shadow_box_shadow": {"horizontal": 0, "vertical": 24, "blur": 60, "spread": -28, "color": "rgba(9,23,31,.28)"},
                 "padding": box((0, 0, 0, 0)), "custom_css": LOOP_CSS},
    "elements": [
        {"id": "1a2b3c01", "elType": "widget", "widgetType": "image", "elements": [],
         "settings": {"image": {"url": "", "id": ""}, "__dynamic__": {"image": tag("1a2b3c11", "post-featured-image")},
                      "image_size": "large", "width": {"unit": "%", "size": 100}, "_css_classes": "iah-imp-img"}},
        {"id": "1a2b3c02", "elType": "container", "isInner": True,
         "settings": {"content_width": "full", "flex_direction": "column", "flex_gap": {"unit": "px", "size": 0, "column": "0", "row": "0"},
                      "padding": box((28, 32, 34, 32)), "padding_mobile": box((22, 22, 28, 22))},
         "elements": [
             te("1a2b3c03", field("1a2b3c13", "settore_label"), "#4AB7D5", 14, "800", "iah-imp-lbl"),
             {"id": "1a2b3c04", "elType": "widget", "widgetType": "heading", "elements": [],
              "settings": dict(MONT, **{"title": "Impianto", "__dynamic__": {"title": tag("1a2b3c14", "post-title")}, "header_size": "h3",
                                        "title_color": "#09171F", "typography_font_weight": "800",
                                        "typography_font_size": {"unit": "px", "size": 26}, "typography_font_size_mobile": {"unit": "px", "size": 22},
                                        "typography_line_height": {"unit": "em", "size": 1.25}})},
             te("1a2b3c05", field("1a2b3c15", "sottotitolo"), "#1A4D6A", 17.5, "700", "iah-imp-sub"),
             te("1a2b3c06", tag("1a2b3c16", "post-excerpt"), "#3D5A6C", 17.5, "400", "iah-imp-txt", 1.7, 16.5),
             te("1a2b3c07", field("1a2b3c17", "tag_tecnologie"), "#1A4D6A", 15, "700", "iah-imp-tag", 1.5),
         ]},
    ]}]

def section(term_ids, sec_id, css_id):
    return [{
        "id": sec_id, "elType": "container", "isInner": False,
        "settings": {"flex_direction": "column", "flex_direction_mobile": "column", "css_id": css_id, "content_width": "full",
                     "background_background": "classic", "background_color": "#EEF6FA",
                     "padding": box((110, 24, 110, 24)), "padding_mobile": box((70, 16, 70, 16)),
                     "margin": box((0, 0, 0, 0)), "_css_classes": "iah-impianti"},
        "elements": [
            {"id": sec_id[:6] + "a1", "elType": "container", "isInner": True,
             "settings": {"flex_direction": "column", "flex_direction_mobile": "column", "content_width": "boxed", "boxed_width": {"unit": "px", "size": 1240},
                          "flex_gap": {"unit": "px", "size": 18, "column": "18", "row": "18"}},
             "elements": [
                 {"id": sec_id[:6] + "a2", "elType": "widget", "widgetType": "text-editor", "elements": [],
                  "settings": dict(MONT, **{"editor": "<p>LE NOSTRE REALIZZAZIONI</p>", "text_color": "#1A4D6A", "typography_font_weight": "800",
                                            "typography_font_size": {"unit": "px", "size": 19}, "typography_font_size_mobile": {"unit": "px", "size": 17},
                                            "typography_letter_spacing": {"unit": "px", "size": 1.4}})},
                 {"id": sec_id[:6] + "a3", "elType": "widget", "widgetType": "heading", "elements": [],
                  "settings": dict(MONT, **{"title": "I nostri impianti", "header_size": "h2", "title_color": "#09171F", "typography_font_weight": "800",
                                            "typography_font_size": {"unit": "px", "size": 46}, "typography_font_size_mobile": {"unit": "px", "size": 29},
                                            "typography_line_height": {"unit": "em", "size": 1.15}})},
                 {"id": sec_id[:6] + "a4", "elType": "widget", "widgetType": "text-editor", "elements": [],
                  "settings": dict(MONT, **{"editor": "<p>Ogni impianto nasce da esigenze specifiche e viene sviluppato con un approccio su misura, combinando competenze tecniche ed esperienza applicativa per garantire soluzioni affidabili, efficienti e durature.</p>",
                                            "text_color": "#3D5A6C", "typography_font_weight": "400", "typography_font_size": {"unit": "px", "size": 21},
                                            "typography_font_size_mobile": {"unit": "px", "size": 18}, "typography_line_height": {"unit": "em", "size": 1.65},
                                            "_max_width": {"unit": "px", "size": 820}})},
             ]},
            {"id": sec_id[:6] + "b1", "elType": "container", "isInner": True,
             "settings": {"flex_direction": "column", "content_width": "boxed", "boxed_width": {"unit": "px", "size": 1240},
                          "padding": box((44, 0, 0, 0)), "padding_mobile": box((28, 0, 0, 0))},
             "elements": [
                 {"id": sec_id[:6] + "b2", "elType": "widget", "widgetType": "loop-carousel", "elements": [],
                  "settings": {"_skin": "post", "template_id": "{{LOOP_ID}}", "post_query_post_type": "post",
                               "post_query_include": ["terms"], "post_query_include_term_ids": term_ids,
                               "post_query_orderby": "post_date", "post_query_order": "asc", "post_query_posts_per_page": 12,
                               "slides_to_show": "2", "slides_to_show_tablet": "2", "slides_to_show_mobile": "1",
                               "slides_to_scroll": "1", "arrows": "yes", "pagination": "bullets", "autoplay": "no"}},
             ]},
            {"id": sec_id[:6] + "c1", "elType": "widget", "widgetType": "html", "elements": [],
             "settings": {"html": "<style>.iah-impianti:not(:has(.e-loop-item)){display:none!important;}.iah-impianti .elementor-swiper-button{color:#09171F;background:#fff;border-radius:50%;width:48px;height:48px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px -12px rgba(9,23,31,.45);}.iah-impianti .swiper-pagination-bullet-active{background:#4AB7D5;}@media(max-width:767px){.iah-impianti .elementor-swiper-button{width:40px;height:40px;}}</style>",
                          "_css_classes": "iah-global"}},
        ]}]

if __name__ == '__main__':
    json.dump(loop_item, open(os.path.join(OUT, 'loop_item.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    for name, ids, sid, cid in (('sec_tutti', [10, 11, 12, 13, 14], '5e0a11d1', 'nostri-impianti'),):
        json.dump(section(ids, sid, cid), open(os.path.join(OUT, name + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(os.listdir(OUT))
