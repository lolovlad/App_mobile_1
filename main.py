from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField


class MainApp(MDApp):

    def update_lbl(self, text):
        self.label.text = text

    def count(self, instance):

        operation = instance.text

        one_num = self.one_num.text
        two_num = self.two_num.text

        if one_num.isdigit():
            if two_num.isdigit():
                try:
                    self.update_lbl(str(eval(f"{int(one_num)} {operation} {int(two_num)}")))
                except:
                    self.update_lbl("error")

    def build(self):

        bl = MDBoxLayout(orientation='vertical')
        gl = MDGridLayout(cols=2)

        self.one_num = MDTextField(helper_text="тут могут быть только цифры", required=True)
        self.two_num = MDTextField(helper_text="тут могут быть только цифры", required=True)

        bl.add_widget(self.one_num)
        bl.add_widget(self.two_num)

        self.label = MDLabel(text="0")

        bl.add_widget(self.label)

        btn_1 = MDRectangleFlatButton(text='+', size_hint=(.5, 1), on_press=self.count)
        btn_2 = MDRectangleFlatButton(text='-', size_hint=(.5, 1), on_press=self.count)
        btn_3 = MDRectangleFlatButton(text='/', size_hint=(.5, 1), on_press=self.count)
        btn_4 = MDRectangleFlatButton(text='*', size_hint=(.5, 1), on_press=self.count)

        gl.add_widget(btn_1)
        gl.add_widget(btn_2)
        gl.add_widget(btn_3)
        gl.add_widget(btn_4)

        bl.add_widget(gl)
        return bl


MainApp().run()
