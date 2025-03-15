from json import dump, load
from UI import initiateMainUI, QMainWindow, QFileDialog, QFrame, QPushButton, QWidget, QLabel, QLineEdit, BTSize, Qt, QIcon

#? Load The Style Sheet & Start Main Window UI
if __name__ == '__main__':
    from cssutils import parseString
    def readStyle():
        button_style = list()
        with open('UI_styles.css', 'r') as styleFile:
            readStyle = parseString(styleFile.read())
            for index, rule in enumerate (readStyle):
                style_rules = { 'Css-Ids': [ "#add_button", "#universal_button", "#searchbox", ".label_texts" ],
                                'Qt-Ids': [ "QPushButton", "QPushButton", "QLineEdit", "QLabel" ] }

                css_index_length = int(len(style_rules['Css-Ids']))
                if index < css_index_length:
                    if rule.type == rule.STYLE_RULE and rule.selectorText == style_rules['Css-Ids'][index]:
                        buttonStyle = rule.cssText.replace(style_rules['Css-Ids'][index], style_rules['Qt-Ids'][index])
                        button_style.append(str(buttonStyle.replace("\n", "")))

                else:
                    if rule.type == rule.STYLE_RULE and rule.selectorText == style_rules['Css-Ids'][index-css_index_length]+":hover":
                        buttonStyle_hover = rule.cssText.replace(style_rules['Css-Ids'][index-css_index_length]+":hover", style_rules['Qt-Ids'][index-css_index_length]+":hover")
                        button_style.append(str(buttonStyle_hover.replace("\n", "")))

        return button_style

    STYLE_OWNER = {
                    "Add_BT": readStyle()[0]+readStyle()[4],
                    "Default_BT": readStyle()[1]+readStyle()[5],
                    "Search_BT": readStyle()[1]+readStyle()[5],
                    "Search_Box": readStyle()[2]+readStyle()[6],
                    "Labels_Txt": [ readStyle()[3], readStyle()[7] ]
                  }

    initiateMainUI(STYLE_OWNER)
