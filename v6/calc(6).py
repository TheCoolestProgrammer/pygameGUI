import pygame
import base_classes5 as baseClasses
from scaling_space_widget import *
import datetime
import time

def save(app,message=""):
    p = open("./logs/history.txt","a",encoding="UTF-8")
    if message:
        p.write(message)
    else:
        p.write(app.equation.text)
    p.write("\n")
    p.close()
def addition(widget,app):
    if not last_sym_is_double(app,"+"):
        if last_sym_is_digit(app) or len(app.equation.text)==0:
            app.equation.text =app.equation.text[:app.equation_pointer]+"+"+app.equation.text[app.equation_pointer:]
            app.equation_pointer+=1

def subtraction(widget,app):
    if not last_sym_is_double(app,"-"):
        if last_sym_is_digit(app) or len(app.equation.text)==0:
            # app.equation.text+="-"
            app.equation.text = app.equation.text[:app.equation_pointer] + "." + app.equation.text[
                                                                                 app.equation_pointer:]
            app.equation_pointer += 1

def multiplication(widget,app):
    # if not last_sym_is_double(app,"*"):
    #     if last_sym_is_digit(app):
    # app.equation.text += "*"
    app.equation.text = app.equation.text[:app.equation_pointer] + "*" + app.equation.text[
                                                                         app.equation_pointer:]
    app.equation_pointer += 1
def division(widget,app):
    if not last_sym_is_double(app,"/"):
        if last_sym_is_digit(app):
            # app.equation.text += "/"
            app.equation.text = app.equation.text[:app.equation_pointer] + "/" + app.equation.text[
                                                                                 app.equation_pointer:]
            app.equation_pointer += 1

def del_last(widget,app):
    if len(app.equation.text)>0:
        # app.equation.text = app.equation.text[:-1]
        if app.equation_pointer > 0:
            app.equation.text = app.equation.text[:app.equation_pointer-1] + app.equation.text[app.equation_pointer:]

            app.equation_pointer -= 1
def equals(widget,app):

    try:
        save(app)
        save(app,">equals")
        print(app.equation.text)
        t1 = time.time()
        app.equation.text = str(eval(app.equation.text))
        t2 = time.time()
        print(t2-t1)
        save(app)
        app.equation_pointer=len(app.equation.text)
    except Exception:
        app.equation.text ="0"
def delete(widget,app):
    app.equation.text=""
    app.quation_pointer = 0

def plus_minus(widget,app):
    save(app, ">invert")
    app.equation.text = "-"+app.equation.text
    app.equation_pointer = len(app.equation.text)
def reciprocial(widget,app):
    if last_sym_is_digit(app):
        save(app, ">reciprocial")
        app.equation.text = str(eval("1/("+app.equation.text+")"))
        app.equation_pointer = len(app.equation.text)
def percent(widget,app):
    if not last_sym_is_double(app,"%"):
        if last_sym_is_digit(app):
            # app.equation.text +="%"
            app.equation.text = app.equation.text[:app.equation_pointer] + "%" + app.equation.text[
                                                                                 app.equation_pointer:]
            app.equation_pointer += 1
def root(widget,app):
    save(app, ">root")
    app.equation.text = str(eval(app.equation.text)**0.5)
    app.equation_pointer = len(app.equation.text)
    save(app, f"res:{app.equation.text}")
def point(widget,app):
    if "." not in app.equation.text:
        # app.equation.text = app.equation.text+"."
        app.equation.text = app.equation.text[:app.equation_pointer] + "." + app.equation.text[app.equation_pointer:]
        app.equation_pointer += 1
def add_left_bracket(widget,app):
    # app.equation.text = app.equation.text+"("
    app.equation.text = app.equation.text[:app.equation_pointer] + "(" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def add_right_bracket(widget,app):
    # app.equation.text = app.equation.text+")"
    app.equation.text = app.equation.text[:app.equation_pointer] + ")" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1

def pointer_left(widget, app):
    if app.equation_pointer > 0:
        app.equation_pointer -= 1
    print(app.equation_pointer)

def pointer_right(widget, app):
    if app.equation_pointer < len(app.equation.text):
        app.equation_pointer += 1
    print(app.equation_pointer)
def one(widget,app):
    # app.equation.text += "1"
    app.equation.text = app.equation.text[:app.equation_pointer] + "1" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1

def two(widget,app):
    # app.equation.text += "2"
    app.equation.text = app.equation.text[:app.equation_pointer] + "2" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def three(widget,app):
    # app.equation.text += "3"
    app.equation.text = app.equation.text[:app.equation_pointer] + "3" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def four(widget,app):
    # app.equation.text += "4"
    app.equation.text = app.equation.text[:app.equation_pointer] + "4" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def five(widget,app):
    # app.equation.text += "5"
    app.equation.text = app.equation.text[:app.equation_pointer] + "5" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def six(widget,app):
    # app.equation.text += "6"
    app.equation.text = app.equation.text[:app.equation_pointer] + "6" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def seven(widget,app):
    # app.equation.text += "7"
    app.equation.text = app.equation.text[:app.equation_pointer] + "7" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def eight(widget,app):
    # app.equation.text += "8"
    app.equation.text = app.equation.text[:app.equation_pointer] + "8" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def nine(widget,app):
    # app.equation.text += "9"
    app.equation.text = app.equation.text[:app.equation_pointer] + "9" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1
def zero(widget,app):
    # app.equation.text += "0"
    app.equation.text = app.equation.text[:app.equation_pointer] + "0" + app.equation.text[app.equation_pointer:]
    app.equation_pointer += 1

def mc(widget,app):
    app.memory = 0
    save(app,">memory.txt clear")
def ms(widget,app):
    save(app, ">memory.txt save")
    save(app, f"mem:{app.memory}->")
    app.memory = eval(app.equation.text)
    save(app, f"mem:{app.memory}")
    p = open("./logs/memory.txt", mode="w", encoding="UTF-8")
    p.write(str(app.memory))
    p.close()
def mr(widget,app):
    app.equation.text = str(app.memory)
    save(app, "memory read")
    app.equation_pointer=len(app.equation.text)
def mp(widget,app):
    save(app, ">memory plus")
    save(app, f"mem:{app.memory}")
    save(app, f"equation:{app.equation.text}->")
    app.equation.text= str(eval(app.equation.text)+app.memory)
    save(app, f"res:{app.equation.text}")
    app.equation_pointer = len(app.equation.text)
def mm(widget,app):
    save(app, ">memory minus")
    save(app, f"mem:{app.memory}")
    save(app, f"equation:{app.equation.text}->")
    app.equation.text= str(eval(app.equation.text)-app.memory)
    save(app, f"res:{app.equation.text}")
    app.equation_pointer = len(app.equation.text)
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
        p = open("./logs/memory.txt", mode="r", encoding="UTF-8").read().strip()
        print(p)
        self.memory = float(open("./logs/memory.txt",mode="r",encoding="UTF-8").read())
        save(self, f"________new seans at {datetime.datetime.now()}____________")
        self.layers_inspector = baseClasses.LayerInspector()
        self.window_layers_inspector = baseClasses.LayerInspector()
        self.equation_pointer=0
        # self.layers_inspector.layers = [self.window]
        self.equation = baseClasses.Text(0,50,1180,50,True,(255,255,255),self.layers_inspector,"",(0,0,0))
        # self.equation = baseClasses.Text(100,500,1180,100,True,(0,0,0),self.layers_inspector,"")
        self.cancel_button = baseClasses.Button(0, 150, 200, 50, True, (125, 125, 125), self.layers_inspector, "<=")
        self.delete_button = baseClasses.Button(200, 150, 100, 50, True, (125, 125, 125), self.layers_inspector, "CE")
        self.plus_minus_button = baseClasses.Button(300, 150, 100, 50, True, (125, 125, 125), self.layers_inspector, "+/-")
        self.root_button = baseClasses.Button(400, 150, 100, 50, True, (125, 125, 125), self.layers_inspector, "√")

        self.seven_button = baseClasses.Button(0, 200, 100, 50, True, (125, 125, 125), self.layers_inspector, "7")
        self.eight_button = baseClasses.Button(100, 200, 100, 50, True, (125, 125, 125), self.layers_inspector, "8")
        self.nine_button = baseClasses.Button(200, 200, 100, 50, True, (125, 125, 125), self.layers_inspector, "9")

        self.four_button = baseClasses.Button(0, 250, 100, 50, True, (125, 125, 125), self.layers_inspector, "4")
        self.five_button = baseClasses.Button(100, 250, 100, 50, True, (125, 125, 125), self.layers_inspector, "5")
        self.six_button = baseClasses.Button(200, 250, 100, 50, True, (125, 125, 125), self.layers_inspector, "6")

        self.one_button = baseClasses.Button(0, 300, 100, 50, True, (125, 125, 125), self.layers_inspector, "1")
        self.two_button = baseClasses.Button(100, 300, 100, 50, True, (125, 125, 125), self.layers_inspector, "2")
        self.three_button = baseClasses.Button(200, 300, 100, 50, True, (125, 125, 125), self.layers_inspector, "3")

        self.zero_button = baseClasses.Button(0, 350, 200, 50, True, (125, 125, 125), self.layers_inspector,"0")
        self.point_button = baseClasses.Button(200, 350, 100, 50, True, (125, 125, 125), self.layers_inspector,".")

        self.plus_button = baseClasses.Button(300, 200, 100, 50, True, (125, 125, 125),self.layers_inspector,"+")
        self.minus_button = baseClasses.Button(300, 250, 100, 50, True, (125, 125, 125),self.layers_inspector,"-")
        self.division_button = baseClasses.Button(300, 300, 100, 50, True, (125, 125, 125),self.layers_inspector,"/")
        self.multiply_button = baseClasses.Button(300, 350, 100, 50, True, (125, 125, 125),self.layers_inspector,"*")

        self.percent_button = baseClasses.Button(400, 200, 100, 50, True, (125, 125, 125), self.layers_inspector, "%")
        self.reciprocal_button = baseClasses.Button(400, 250, 100, 50, True, (125, 125, 125), self.layers_inspector, "1/x")
        self.equals_button = baseClasses.Button(400, 300, 100, 100, True, (125, 125, 125), self.layers_inspector, "=")

        self.mc_button = baseClasses.Button(0, 100, 100, 50, True, (125, 125, 125), self.layers_inspector, "MC")
        self.ms_button = baseClasses.Button(100, 100, 100, 50, True, (125, 125, 125), self.layers_inspector,
                                                    "MS")
        self.mr_button = baseClasses.Button(200, 100, 100, 50, True, (125, 125, 125), self.layers_inspector, "MR")
        self.mp_button = baseClasses.Button(300, 100, 100, 50, True, (125, 125, 125), self.layers_inspector, "M+")
        self.mm_button = baseClasses.Button(400, 100, 100, 50, True, (125, 125, 125), self.layers_inspector, "M-")

        self.left_bracket_button = baseClasses.Button(0, 400, 200, 50, True, (125, 125, 125), self.layers_inspector,"(")
        self.right_bracket_button = baseClasses.Button(200, 400, 100, 50, True, (125, 125, 125), self.layers_inspector,")")

        self.pointer_left_button = baseClasses.Button(300, 400, 100, 50, True, (125, 125, 125), self.layers_inspector,"<-")
        self.pointer_right_button = baseClasses.Button(400, 400, 100, 50, True, (125, 125, 125), self.layers_inspector,"->")


        self.ratio_buttons_inspector = baseClasses.RatioButtonsInspector(0, 0, 150, 50, True, (100, 100, 100),
                                                                         self.layers_inspector)
        self.rationbutton1 = baseClasses.RatioButton(0, 0, 50, 50, True, (200, 200, 200),
                                                     self.ratio_buttons_inspector.layers_inspector)
        self.rationbutton1.state=True
        self.rationbutton2 = baseClasses.RatioButton(100, 0, 50, 50, True, (200, 200, 200),
                                                     self.ratio_buttons_inspector.layers_inspector)
        self.rationbutton3 = baseClasses.RatioButton(200, 0, 50, 50, True, (200, 200, 200),
                                                     self.ratio_buttons_inspector.layers_inspector)
        self.ratio_buttons_inspector.layers_inspector.layers=[self.rationbutton1,self.rationbutton2,self.rationbutton3]

        # self.space = Scaling_space_widget(400, 400, 300, 300,  self.layers_inspector, "x^2")
        # self.window = baseClasses.Window(800,600,100,100,True,(255,255,255),self.layers_inspector)
        # self.window_multiply_button = baseClasses.Button(820, 620, 50, 50, True, (125, 125, 125),self.window_layers_inspector,"*")
        # self.window_layers_inspector.layers = [self.window_multiply_button]

        self.layers_inspector.layers=[
                                    self.cancel_button,
                                      self.delete_button,
            self.plus_minus_button,
            self.root_button,
            self.seven_button,
            self.eight_button,
            self.nine_button,
            self.four_button,
            self.five_button,
            self.six_button,
            self.one_button,
            self.two_button,
            self.three_button,
            self.zero_button,
            self.point_button,
            self.plus_button,
            self.minus_button,
            self.division_button,
            self.multiply_button,
            self.reciprocal_button,
            self.equals_button,
            self.percent_button,
            self.mc_button,
            self.ms_button,
            self.mr_button,
            self.mp_button,
            self.mm_button,
            self.left_bracket_button,
            self.right_bracket_button,
            self.pointer_left_button,
            self.pointer_right_button,
                                      self.equation,
                                      self.ratio_buttons_inspector,
                                      # self.space
                                      # self.window]
                                    ]
        touch_group=[baseClasses.IntersectionChecker(),baseClasses.TouchChecker(1),baseClasses.ActiveChecker()]
        hold_group=[baseClasses.IntersectionChecker(),baseClasses.HoldChecker(1),baseClasses.ActiveChecker()]
        up_group=[baseClasses.EventUpChecker(1)]

        plus_group = baseClasses.CombinationCheckers(addition,touch_group)
        self.plus_button.keys_inspector.checkers.append(plus_group)
        plus_group_keyboard = baseClasses.CombinationCheckers(addition, [
            baseClasses.TouchChecker(pygame.K_EQUALS)
        ])
        self.plus_button.keys_inspector.checkers.append(plus_group_keyboard)

        substraction_group = baseClasses.CombinationCheckers(subtraction,touch_group)
        self.minus_button.keys_inspector.checkers.append(substraction_group)
        substraction_group_keyboard = baseClasses.CombinationCheckers(subtraction, [
            baseClasses.TouchChecker(pygame.K_MINUS)
        ])
        self.minus_button.keys_inspector.checkers.append(substraction_group_keyboard)

        multiply_group = baseClasses.CombinationCheckers(multiplication,touch_group)
        multiply_group_keyboard = baseClasses.CombinationCheckers(multiplication, [
                                                                                   baseClasses.TouchChecker(pygame.K_8)
                                                                                   ])
        self.multiply_button.keys_inspector.checkers.append(multiply_group_keyboard)
        self.multiply_button.keys_inspector.checkers.append(multiply_group)


        division_group = baseClasses.CombinationCheckers(division,touch_group)
        self.division_button.keys_inspector.checkers.append(division_group)
        division_group_keyboard = baseClasses.CombinationCheckers(division, [baseClasses.TouchChecker(pygame.K_BACKSLASH)])
        self.division_button.keys_inspector.checkers.append(division_group_keyboard)

        del_group = baseClasses.CombinationCheckers(delete, touch_group)
        self.delete_button.keys_inspector.checkers.append(del_group)
        del_group_keyboard = baseClasses.CombinationCheckers(delete, [baseClasses.TouchChecker(pygame.K_DELETE)])
        self.delete_button.keys_inspector.checkers.append(del_group_keyboard)

        pointer_left_group = baseClasses.CombinationCheckers(pointer_left, touch_group)
        self.pointer_left_button.keys_inspector.checkers.append(pointer_left_group)
        # del_group_keyboard = baseClasses.CombinationCheckers(delete, [baseClasses.TouchChecker(pygame.K_DELETE)])
        # self.delete_button.keys_inspector.checkers.append(del_group_keyboard)

        pointer_right_group = baseClasses.CombinationCheckers(pointer_right, touch_group)
        self.pointer_right_button.keys_inspector.checkers.append(pointer_right_group)
        # del_group_keyboard = baseClasses.CombinationCheckers(delete, [baseClasses.TouchChecker(pygame.K_DELETE)])
        # self.delete_button.keys_inspector.checkers.append(del_group_keyboard)

        plus_minus_group = baseClasses.CombinationCheckers(plus_minus, touch_group)
        self.plus_minus_button.keys_inspector.checkers.append(plus_minus_group)

        reciprocial_group = baseClasses.CombinationCheckers(reciprocial, touch_group)
        self.reciprocal_button.keys_inspector.checkers.append(reciprocial_group)

        left_bracket_group = baseClasses.CombinationCheckers(add_left_bracket, touch_group)
        self.left_bracket_button.keys_inspector.checkers.append(left_bracket_group)

        right_bracket_group = baseClasses.CombinationCheckers(add_right_bracket, touch_group)
        self.right_bracket_button.keys_inspector.checkers.append(right_bracket_group)

        mc_group = baseClasses.CombinationCheckers(mc, touch_group)
        self.mc_button.keys_inspector.checkers.append(mc_group)
        ms_group = baseClasses.CombinationCheckers(ms, touch_group)
        self.ms_button.keys_inspector.checkers.append(ms_group)
        mr_group = baseClasses.CombinationCheckers(mr, touch_group)
        self.mr_button.keys_inspector.checkers.append(mr_group)

        mp_group = baseClasses.CombinationCheckers(mp, touch_group)
        self.mp_button.keys_inspector.checkers.append(mp_group)
        mm_group = baseClasses.CombinationCheckers(mm, touch_group)
        self.mm_button.keys_inspector.checkers.append(mm_group)


        percent_group = baseClasses.CombinationCheckers(percent, touch_group)
        self.percent_button.keys_inspector.checkers.append(percent_group)

        # __________numbers__________
        one_group = baseClasses.CombinationCheckers(one,touch_group)
        one_group_keyboard = baseClasses.CombinationCheckers(one,[baseClasses.TouchChecker(pygame.K_KP1)])
        self.one_button.keys_inspector.checkers.append(one_group)
        self.one_button.keys_inspector.checkers.append(one_group_keyboard)

        two_group = baseClasses.CombinationCheckers(two,touch_group)
        self.two_button.keys_inspector.checkers.append(two_group)
        two_group_keyboard = baseClasses.CombinationCheckers(two, [baseClasses.TouchChecker(pygame.K_KP2)])
        self.two_button.keys_inspector.checkers.append(two_group_keyboard)

        three_group = baseClasses.CombinationCheckers(three,touch_group)
        self.three_button.keys_inspector.checkers.append(three_group)
        three_group_keyboard = baseClasses.CombinationCheckers(three, [baseClasses.TouchChecker(pygame.K_KP3)])
        self.three_button.keys_inspector.checkers.append(three_group_keyboard)
        #
        four_group = baseClasses.CombinationCheckers(four,touch_group)
        self.four_button.keys_inspector.checkers.append(four_group)
        four_group_keyboard = baseClasses.CombinationCheckers(four, [baseClasses.TouchChecker(pygame.K_KP4)])
        self.four_button.keys_inspector.checkers.append(four_group_keyboard)

        five_group = baseClasses.CombinationCheckers(five,touch_group)
        self.five_button.keys_inspector.checkers.append(five_group)
        five_group_keyboard = baseClasses.CombinationCheckers(five, [baseClasses.TouchChecker(pygame.K_KP5)])
        self.five_button.keys_inspector.checkers.append(five_group_keyboard)

        six_group = baseClasses.CombinationCheckers(six,touch_group)
        self.six_button.keys_inspector.checkers.append(six_group)
        six_group_keyboard = baseClasses.CombinationCheckers(six, [baseClasses.TouchChecker(pygame.K_KP6)])
        self.six_button.keys_inspector.checkers.append(six_group_keyboard)

        seven_group = baseClasses.CombinationCheckers(seven,touch_group)
        self.seven_button.keys_inspector.checkers.append(seven_group)
        seven_group_keyboard = baseClasses.CombinationCheckers(seven, [baseClasses.TouchChecker(pygame.K_KP7)])
        self.seven_button.keys_inspector.checkers.append(seven_group_keyboard)

        eight_group = baseClasses.CombinationCheckers(eight,touch_group)
        self.eight_button.keys_inspector.checkers.append(eight_group)
        eight_group_keyboard = baseClasses.CombinationCheckers(eight, [baseClasses.TouchChecker(pygame.K_KP8)])
        self.eight_button.keys_inspector.checkers.append(eight_group_keyboard)

        nine_group = baseClasses.CombinationCheckers(nine,touch_group)
        self.nine_button.keys_inspector.checkers.append(nine_group)
        nine_group_keyboard = baseClasses.CombinationCheckers(nine, [baseClasses.TouchChecker(pygame.K_KP9)])
        self.nine_button.keys_inspector.checkers.append(nine_group_keyboard)

        zero_group = baseClasses.CombinationCheckers(zero, touch_group)
        self.zero_button.keys_inspector.checkers.append(zero_group)
        zero_group_keyboard = baseClasses.CombinationCheckers(zero, [baseClasses.TouchChecker(pygame.K_KP0)])
        self.zero_button.keys_inspector.checkers.append(zero_group_keyboard)

        cancel_group = baseClasses.CombinationCheckers(del_last, touch_group)
        self.cancel_button.keys_inspector.checkers.append(cancel_group)
        cancel_group_keyboard = baseClasses.CombinationCheckers(del_last, [baseClasses.TouchChecker(pygame.K_BACKSPACE)])
        self.cancel_button.keys_inspector.checkers.append(cancel_group_keyboard)

        equals_group = baseClasses.CombinationCheckers(equals, touch_group)
        self.equals_button.keys_inspector.checkers.append(equals_group)
        equals_group_keyboard = baseClasses.CombinationCheckers(equals, [baseClasses.TouchChecker(pygame.K_RETURN)])
        self.equals_button.keys_inspector.checkers.append(equals_group_keyboard)

        root_group = baseClasses.CombinationCheckers(root, touch_group)
        self.root_button.keys_inspector.checkers.append(root_group)

        point_group = baseClasses.CombinationCheckers(point, touch_group)
        self.point_button.keys_inspector.checkers.append(point_group)
        point_group_keyboard = baseClasses.CombinationCheckers(point, [baseClasses.TouchChecker(pygame.K_SLASH)])
        self.point_button.keys_inspector.checkers.append(point_group_keyboard)

        # window_holdown_group = baseClasses.CombinationCheckers(self.window.holdown_lmb_action, hold_group)
        # self.window.keys_inspector.checkers.append(window_holdown_group)
        # window_up_group = baseClasses.CombinationCheckers(self.window.mouse_up_action, up_group)
        # self.window.keys_inspector.checkers.append(window_up_group)
        #
        # self.window.layers_inspector = self.window_layers_inspector

        # window_multiply_group = baseClasses.CombinationCheckers(multiplication, touch_group)
        # self.window_multiply_button.keys_inspector.checkers.append(window_multiply_group)


    def drawing(self):
        self.screen.fill((255,255,255))

        # self.draw_text(str(self.equation),500,500,(255,255,255))

        self.layers_inspector.draw(self.screen)
        pointer_shift = self.equation.font.size(self.equation.text[:self.equation_pointer])[0]
        pygame.draw.rect(self.screen,(0,255,0),(self.equation.x+pointer_shift, self.equation.y, 10,self.equation.text_size))
        #TODO: за строчку выше надо попускать
    def events_check(self,all_events):
        super().events_check(all_events)
        self.layers_inspector.check_actions(self)
        # print(self.window_multiply_button.isactive)

class FunctionCalc(baseClasses.Stage):
    def __init__(self):
        super().__init__()

        self.layers_inspector = baseClasses.LayerInspector()
        self.window_layers_inspector = baseClasses.LayerInspector()

        self.equation = baseClasses.Text(0, 50, 1180, 50, True, (255, 255, 255), self.layers_inspector, "", (0, 0, 0))
        self.ratio_buttons_inspector = baseClasses.RatioButtonsInspector(0, 0, 150, 50, True, (100, 100, 100),
                                                                         self.layers_inspector)
        self.rationbutton1 = baseClasses.RatioButton(0, 0, 50, 50, True, (200, 200, 200),
                                                     self.ratio_buttons_inspector.layers_inspector)
        # self.rationbutton1.state
        self.rationbutton2 = baseClasses.RatioButton(100, 0, 50, 50, True, (200, 200, 200),
                                                     self.ratio_buttons_inspector.layers_inspector)
        self.ratio_buttons_inspector.layers_inspector.layers = [self.rationbutton1, self.rationbutton2]

        # self.space = Scaling_space_widget(400, 400, 300, 300, self.layers_inspector, "sin(x)")
        # self.space = Scaling_space_widget(400, 400, 300, 300, self.layers_inspector, "((x)**2)+(5*(x))")
        self.space = Scaling_space_widget(0, 100, 600, 600, self.layers_inspector, "((x)**2)+(5*((x)))")
        self.layers_inspector.layers = [
            self.equation,
            self.ratio_buttons_inspector,
            self.space
            # self.window]
        ]
        touch_group = [baseClasses.IntersectionChecker(), baseClasses.TouchChecker(1), baseClasses.ActiveChecker()]
    def drawing(self):
        self.screen.fill((255,255,255))

        # self.draw_text(str(self.equation),500,500,(255,255,255))

        self.layers_inspector.draw(self.screen)

    def events_check(self,all_events):
        super().events_check(all_events)
        self.layers_inspector.check_actions(self)
class MyApp(baseClasses.App):
    def __init__(self):
        super().__init__()
        self.stages=[DemoScene(),FunctionCalc()]

    def events_check(self):
        super().events_check()
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.process_running = False
    def check_stage(self):
        if self.now_stage==0:
            if self.stages[0].rationbutton2.state==1:
                self.now_stage=1
                self.stages[1].rationbutton2.state=1
                self.stages[1].rationbutton1.state=0
        elif self.now_stage==1:
            # print("_______")
            if self.stages[1].rationbutton1.state==1:
                self.now_stage=0
                self.stages[0].rationbutton1.state = 1
                self.stages[0].rationbutton2.state = 0
        # elif self.now_stage==2:
        #     # print("_______")
        #     if self.stages[2].rationbutton1.state==1:
        #         self.now_stage=0
        #         self.stages[0].rationbutton1.state = 1
        #         self.stages[0].rationbutton2.state = 0
if __name__=="__main__":
    a = MyApp()
    while a.process_running:
        a.mainloop()
        a.check_stage()
