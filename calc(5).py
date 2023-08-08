import pygame
import base_classes5 as baseClasses

def addition(widget,app):
    if not last_sym_is_double(app,"+"):
        if last_sym_is_digit(app) or len(app.equation.text)==0:
            app.equation.text +="+"

def subtraction(widget,app):
    if not last_sym_is_double(app,"-"):
        if last_sym_is_digit(app) or len(app.equation.text)==0:
            app.equation.text+="-"

def multiplication(widget,app):
    if not last_sym_is_double(app,"*"):
        if last_sym_is_digit(app):
            app.equation.text += "*"

def division(widget,app):
    if not last_sym_is_double(app,"/"):
        if last_sym_is_digit(app):
            app.equation.text += "/"

def del_last(widget,app):
    if len(app.equation.text)>0:
        app.equation.text = app.equation.text[:-1]

def equals(widget,app):
    app.equation.text = str(eval(app.equation.text))

def one(widget,app):
    app.equation.text += "1"
def two(widget,app):
    app.equation.text += "2"
def three(widget,app):
    app.equation.text += "3"
def four(widget,app):
    app.equation.text += "4"
def five(widget,app):
    app.equation.text += "5"
def six(widget,app):
    app.equation.text += "6"
def seven(widget,app):
    app.equation.text += "7"
def eight(widget,app):
    app.equation.text += "8"
def nine(widget,app):
    app.equation.text += "9"
def zero(widget,app):
    app.equation.text += "0"

def last_sym_is_double(app,sym):
    if len(app.equation.text)>0 and app.equation.text[-1]==sym:
        return True
    return False

def last_sym_is_digit(app):
    if len(app.equation.text)>0 and app.equation.text[-1].isdigit():
        return True
    else:
        return False
class DemoScene(baseClasses.Stage):
    def __init__(self):
        super().__init__()

        self.layers_inspector = baseClasses.LayerInspector()
        self.window_layers_inspector = baseClasses.LayerInspector()

        # self.layers_inspector.layers = [self.window]
        self.equation = baseClasses.Text(100,500,1180,100,True,(0,0,0),self.layers_inspector,"")
        # self.equation = baseClasses.Text(100,500,1180,100,True,(0,0,0),self.layers_inspector,"")
        self.plus_button = baseClasses.Button(100, 100, 50, 50, True, (125, 125, 125),self.layers_inspector,"+")
        self.minus_button = baseClasses.Button(160, 100, 50, 50, True, (125, 125, 125),self.layers_inspector,"-")
        self.division_button = baseClasses.Button(220, 100, 50, 50, True, (125, 125, 125),self.layers_inspector,"/")
        self.multiply_button = baseClasses.Button(280, 100, 50, 50, True, (125, 125, 125),self.layers_inspector,"*")


        self.one_button = baseClasses.Button(100, 160, 50, 50, True, (125, 125, 125), self.layers_inspector,"1")
        self.two_button = baseClasses.Button(160, 160, 50, 50, True, (125, 125, 125), self.layers_inspector,"2")
        self.three_button = baseClasses.Button(220, 160, 50, 50, True, (125, 125, 125), self.layers_inspector,"3")
        self.four_button = baseClasses.Button(100, 220, 50, 50, True, (125, 125, 125), self.layers_inspector,"4")
        self.five_button = baseClasses.Button(160, 220, 50, 50, True, (125, 125, 125), self.layers_inspector,"5")
        self.six_button = baseClasses.Button(220, 220, 50, 50, True, (125, 125, 125), self.layers_inspector,"6")
        self.seven_button = baseClasses.Button(100, 280, 50, 50, True, (125, 125, 125), self.layers_inspector,"7")
        self.eight_button = baseClasses.Button(160, 280, 50, 50, True, (125, 125, 125), self.layers_inspector,"8")
        self.nine_button = baseClasses.Button(220, 280, 50, 50, True, (125, 125, 125), self.layers_inspector,"9")
        self.zero_button = baseClasses.Button(280, 280, 50, 50, True, (125, 125, 125), self.layers_inspector,"0")
        self.delete_button = baseClasses.Button(280, 220, 50, 50, True, (125, 125, 125), self.layers_inspector,"<=")
        self.equals_button = baseClasses.Button(280, 160, 50, 50, True, (125, 125, 125), self.layers_inspector,"=")

        self.window = baseClasses.Window(800,600,100,100,True,(255,255,255),self.layers_inspector)
        self.window_multiply_button = baseClasses.Button(820, 620, 50, 50, True, (125, 125, 125),self.window_layers_inspector,"*")
        self.window_layers_inspector.layers = [self.window_multiply_button]

        self.layers_inspector.layers=[self.plus_button,
                                      self.minus_button,
                                      self.multiply_button,
                                      self.division_button,
                                      self.one_button,
                                      self.two_button,
                                      self.three_button,
                                      self.four_button,
                                      self.five_button,
                                      self.six_button,
                                      self.seven_button,
                                      self.eight_button,
                                      self.nine_button,
                                      self.zero_button,
                                      self.delete_button,
                                      self.equals_button,
                                      self.equation,
                                      self.window]

        touch_group=[baseClasses.IntersectionChecker(),baseClasses.TouchChecker(1),baseClasses.ActiveChecker()]
        hold_group=[baseClasses.IntersectionChecker(),baseClasses.HoldChecker(1),baseClasses.ActiveChecker()]
        up_group=[baseClasses.EventUpChecker(1)]

        plus_group = baseClasses.CombinationCheckers(addition,touch_group)
        self.plus_button.keys_inspector.checkers.append(plus_group)

        substraction_group = baseClasses.CombinationCheckers(subtraction,touch_group)
        self.minus_button.keys_inspector.checkers.append(substraction_group)

        multiply_group = baseClasses.CombinationCheckers(multiplication,touch_group)
        self.multiply_button.keys_inspector.checkers.append(multiply_group)

        division_group = baseClasses.CombinationCheckers(division,touch_group)
        self.division_button.keys_inspector.checkers.append(division_group)

        #__________numbers__________
        one_group = baseClasses.CombinationCheckers(one,touch_group)
        self.one_button.keys_inspector.checkers.append(one_group)

        two_group = baseClasses.CombinationCheckers(two,touch_group)
        self.two_button.keys_inspector.checkers.append(two_group)

        three_group = baseClasses.CombinationCheckers(three,touch_group)
        self.three_button.keys_inspector.checkers.append(three_group)

        four_group = baseClasses.CombinationCheckers(four,touch_group)
        self.four_button.keys_inspector.checkers.append(four_group)

        five_group = baseClasses.CombinationCheckers(five,touch_group)
        self.five_button.keys_inspector.checkers.append(five_group)

        six_group = baseClasses.CombinationCheckers(six,touch_group)
        self.six_button.keys_inspector.checkers.append(six_group)

        seven_group = baseClasses.CombinationCheckers(seven,touch_group)
        self.seven_button.keys_inspector.checkers.append(seven_group)

        eight_group = baseClasses.CombinationCheckers(eight,touch_group)
        self.eight_button.keys_inspector.checkers.append(eight_group)

        nine_group = baseClasses.CombinationCheckers(nine,touch_group)
        self.nine_button.keys_inspector.checkers.append(nine_group)

        zero_group = baseClasses.CombinationCheckers(zero, touch_group)
        self.zero_button.keys_inspector.checkers.append(zero_group)

        delete_group = baseClasses.CombinationCheckers(del_last, touch_group)
        self.delete_button.keys_inspector.checkers.append(delete_group)

        equals_group = baseClasses.CombinationCheckers(equals, touch_group)
        self.equals_button.keys_inspector.checkers.append(equals_group)

        window_holdown_group = baseClasses.CombinationCheckers(self.window.holdown_lmb_action, hold_group)
        self.window.keys_inspector.checkers.append(window_holdown_group)
        window_up_group = baseClasses.CombinationCheckers(self.window.mouse_up_action, up_group)
        self.window.keys_inspector.checkers.append(window_up_group)

        self.window.layers_inspector = self.window_layers_inspector

        window_multiply_group = baseClasses.CombinationCheckers(multiplication, touch_group)
        self.window_multiply_button.keys_inspector.checkers.append(window_multiply_group)

    def drawing(self):
        self.screen.fill((0,0,0))

        # self.draw_text(str(self.equation),500,500,(255,255,255))

        self.layers_inspector.draw(self.screen)

    def events_check(self,all_events):
        super().events_check(all_events)
        self.layers_inspector.check_actions(self)
        print(self.window_multiply_button.isactive)

class MyApp(baseClasses.App):
    def __init__(self):
        super().__init__()
        self.stages=[DemoScene()]

    def events_check(self):
        super().events_check()
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.process_running = False

if __name__=="__main__":
    a = MyApp()
    while a.process_running:
        a.mainloop()