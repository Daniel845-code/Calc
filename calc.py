#encoding: UTF-8
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class App(App):
    def build(self):
        self.new_input = ''
        self.operadores = ['/','*','+','-']
        self.ultimo_operador = None
        self.ultimo_numero = None

        main_layout = BoxLayout(orientation='vertical')
        self.resultado = TextInput(
        multiline = False,
        readonly = True,
        halign='right',
        font_size=60
        )
        main_layout.add_widget(self.resultado)

        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['.','0','c','+'],
        ]

        for line in buttons:
            teclado_layout = BoxLayout()
            for texto in line:
                button = Button(
                    text=texto,
                    pos_hint={
                    'center_x':0.5,
                    'center_y':0.5},
                )
                button.bind(on_press=self.on_button_press)
                teclado_layout.add_widget(button)
            main_layout.add_widget(teclado_layout)

        equals_button = Button(
            text='=',
            pos_hint={
                'center_x':0.5,
                'center_y':0.5,
            }
        )
        equals_button.bind(on_press=self.on_solution)

        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self,instance):
        self.new_input += instance.text
        self.resultado.text = self.new_input

        if (instance.text == 'c'):
            #clean the textinput
            self.new_input = ''
            self.resultado.text = ''
        elif (instance.text == '='):
            pass


    def find_parts(self,number):
        enum = 0
        for n in number:
            for operator in self.operadores:
                if (number[enum] == operator):
                    return enum,operator
            enum += 1

    def max_index(self,list):
        n = 0
        for i in list:
            n += 1
        return n

    def on_solution(self,instance):
        number = []
        for character in str(self.new_input):
            number.append(character)

        n,operator = self.find_parts(number)

        i = 0
        part_1 = ''
        part_2 = ''

        while i < n:
            part_1 += number[i]
            i += 1
        i = n+1
        while i < self.max_index(number):
            part_2 += number[i]
            i += 1
        try:
            if (operator == '/'):
                resultado_calc = int(part_1)/int(part_2)
            elif (operator == '*'):
                resultado_calc = int(part_1)*int(part_2)
            elif (operator == '-'):
                resultado_calc = int(part_1)-int(part_2)
            elif (operator == '+'):
                resultado_calc = int(part_1)+int(part_2)
            self.new_input = str(resultado_calc)
            self.resultado.text = str(resultado_calc)
        except:
            self.resultado.text = 'Não execute mais de um calculo por vez!'


App().run()
