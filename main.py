import UI
from json import dump, load
from UI.parent import initiateMainUI 

#? Load The Style Sheet & Start Main Window UI
if __name__ == '__main__':
    ui_style = list()
    from cssutils import parseString
    with open('UI/styles.css', 'r') as styleFile:
        readStyle = [rule for rule in parseString(styleFile.read()).cssRules if rule.type != rule.COMMENT]
        for index, rule in enumerate (readStyle):
            style_rules = { 'Css-Ids': [ "#window_bg", "#add_button", "#universal_button", "#searchbox", ".label_texts" ],
                                'Qt-Ids': [ "", "QPushButton", "QPushButton", "QLineEdit", "QLabel" ] }
            css_index_length = int(len(style_rules['Css-Ids'])) 
            try:
                if rule.type == rule.STYLE_RULE and rule.selectorText == style_rules['Css-Ids'][index]:
                    cssStyle = rule.cssText.replace(style_rules['Css-Ids'][index], style_rules['Qt-Ids'][index])
                    print(f"N={index}")
            except IndexError:
                if rule.type == rule.STYLE_RULE and rule.selectorText == style_rules['Css-Ids'][index-css_index_length]+":hover":
                    cssStyle_hover = rule.cssText.replace(style_rules['Css-Ids'][index-css_index_length]+":hover", style_rules['Qt-Ids'][index-css_index_length]+":hover")
                    print(f"H={index}")
                    continue
            ui_style.append(str(cssStyle.replace("\n", "")))
    
    STYLE_OWNER = {
            "UI_BG": ui_style[0],
                    "Add_BT": ui_style[1]+ui_style[5],
                    "Default_BT": ui_style[2]+ui_style[6],
                    "Search_BT": ui_style[2]+ui_style[6],
                    "Search_Box":ui_style[3]+ui_style[7],
                    "Labels_Txt": [ ui_style[4], ui_style[8] ]
                  }
    initiateMainUI(STYLE_OWNER)
