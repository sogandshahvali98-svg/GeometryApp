import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class GeometryApp(App):
    def build(self):
        self.shape = None

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.info = Label(text="یک شکل را انتخاب کن")
        layout.add_widget(self.info)

        btn_row = BoxLayout(size_hint_y=None, height=50, spacing=5)

        square = Button(text="مربع")
        rect = Button(text="مستطیل")
        tri = Button(text="مثلث")
        circle = Button(text="دایره")

        square.bind(on_press=lambda x: self.set_shape("square"))
        rect.bind(on_press=lambda x: self.set_shape("rect"))
        tri.bind(on_press=lambda x: self.set_shape("tri"))
        circle.bind(on_press=lambda x: self.set_shape("circle"))

        btn_row.add_widget(square)
        btn_row.add_widget(rect)
        btn_row.add_widget(tri)
        btn_row.add_widget(circle)

        layout.add_widget(btn_row)

        self.inputs = TextInput(
            hint_text="ورودی‌ها را با فاصله وارد کن",
            multiline=False
        )
        layout.add_widget(self.inputs)

        btn = Button(text="محاسبه")
        btn.bind(on_press=self.calculate)
        layout.add_widget(btn)

        self.result = Label(text="")
        layout.add_widget(self.result)

        return layout

    def set_shape(self, shape):
        self.shape = shape
        self.inputs.text = ""
        self.result.text = ""

        if shape == "square":
            self.info.text = "مربع: یک ضلع"
        elif shape == "rect":
            self.info.text = "مستطیل: طول و عرض (با فاصله)"
        elif shape == "tri":
            self.info.text = "مثلث: سه ضلع (با فاصله)"
        elif shape == "circle":
            self.info.text = "دایره: شعاع"

    def calculate(self, instance):
        if not self.shape:
            self.result.text = "اول یک شکل انتخاب کن"
            return

        text = self.inputs.text.strip()
        if not text:
            self.result.text = "ورودی خالی است"
            return

        try:
            vals = list(map(float, text.split()))
        except ValueError:
            self.result.text = "لطفاً فقط عدد وارد کنید"
            return

        if self.shape == "square":
            if len(vals) < 1:
                self.result.text = "خطا: ۱ عدد نیاز است"
                return
            a = vals[0]
            self.result.text = f"مساحت: {a*a:.2f} | محیط: {4*a:.2f}"

        elif self.shape == "rect":
            if len(vals) < 2:
                self.result.text = "خطا: ۲ عدد نیاز است"
                return
            l, w = vals[0], vals[1]
            self.result.text = f"مساحت: {l*w:.2f} | محیط: {2*(l+w):.2f}"

        elif self.shape == "tri":
            if len(vals) < 3:
                self.result.text = "خطا: ۳ عدد نیاز است"
                return

            a, b, c = vals[0], vals[1], vals[2]

            if a + b <= c or a + c <= b or b + c <= a:
                self.result.text = "مثلث نامعتبر است"
                return

            p = a + b + c
            s = p / 2

            x = s * (s - a) * (s - b) * (s - c)
            if x <= 0:
                self.result.text = "خطای محاسباتی در مثلث"
                return

            area = math.sqrt(x)
            self.result.text = f"مساحت: {area:.2f} | محیط: {p:.2f}"

        elif self.shape == "circle":
            if len(vals) < 1:
                self.result.text = "خطا: ۱ عدد نیاز است"
                return
            r = vals[0]
            self.result.text = f"مساحت: {math.pi*r*r:.2f} | محیط: {2*math.pi*r:.2f}"


if __name__ == "__main__":
    GeometryApp().run()
