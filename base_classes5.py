import pygame

class Widget:
    '''координаты объективные, а не относительно окна'''
    def __init__(self,x,y,width,height,is_shown,bg_color,layer_parent):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.is_shown=is_shown
        self.bg_color=bg_color
        self.layers_inspector = None
        self.ismoving=False
        self.isactive=False
        self.layer_parent=layer_parent
        '''holding time - время(в фрэймах) через которое включится holdown_action'''
        self.holding_time=1000
        self.holding_frame=0
        self.keys_inspector = KeysInspector(self)
        activate_combination =  CombinationCheckers(self.layer_parent.change_active)
        activate_combination.checkers=[IntersectionChecker(), TouchChecker(1), UnActiveChecker()]
        self.keys_inspector.checkers = [activate_combination
                                        ]

    def is_mouse_intersection(self,x,y):
        if self.x<x<self.x+self.width and self.y < y < self.y + self.height:
            return True
        else:
            return False

    def is_mouse_touched(self,app):
        for event in app.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("Asdas")
                # print(type(event.button))
                if event.button == 1:
                    return 1
                elif event.button == 2:
                    return 2
        return 0

    def is_mouse_hold(self,app):
        if self.holding_frame<self.holding_time:
            if app.mouse_holdown[0] or app.mouse_holdown[1] or app.mouse_holdown[2]:
                self.holding_frame+=1
                return False
        else:
            if app.mouse_holdown[0]:
                return 1
            elif app.mouse_holdown[1]:
                return 2
            elif app.mouse_holdown[2]:
                return 3
        # else:
        #     return 0

    def is_mouse_up(self,app):
        for event in app.events:
            if event.type == pygame.MOUSEBUTTONUP:
                return True
        return False

    def touch_rmb_action(self,widget,app):
        pass
    def touch_lmb_action(self,widget,app):
        pass
    def holdown_lmb_action(self,widget,app):
        pass
    def intersection_action(self,widget,app):
        pass

    def mouse_up_action(self,widget,app):
        # print("_____________")
        self.ismoving=False
        self.holding_frame=0
        # self.keys_inspector.

    def hide_widget(self,app=None):
        self.is_shown=False
    def make_widget_visible(self,app=None):
        self.is_shown=True
    def make_active(self,app=None):
        self.isactive=True
    def make_unactive(self,app=None):
        self.isactive=False

    def draw(self, screen):
        if self.is_shown:
            pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
    def move(self,app):
        if not self.ismoving:
            self.dx, self.dy = app.mouse_pos[0] - self.x, app.mouse_pos[1] - self.y
            self.ismoving=True
        else:
            # self.x += self.dx
            # self.y += self.dy
            self.x = app.mouse_pos[0] - self.dx
            self.y = app.mouse_pos[1] - self.dy
            if self.layers_inspector:
                for widget in self.layers_inspector.layers:
                    widget.move(app)
        # for widget in self.widgets:
        #     widget.x+=dx
        #     widget.y+=dy

class Window(Widget):
    def __init__(self,x,y,width,height,is_shown,bg_color,layer_parent):
        super().__init__(x,y,width,height,is_shown,bg_color,layer_parent)
        self.widgets=[]

    def holdown_lmb_action(self,widget,app):
        self.move(app)
        # print("----------")
    # def mouse_up_action(self,app):
    #     self.ismoving=False

        # print(self.x,self.y)



class Button(Widget):
    def __init__(self,x,y,width,height,is_shown,bg_color,layer_parent,text="",text_color=(0,255,0)):
        super().__init__(x,y,width,height,is_shown,bg_color,layer_parent)
        self.text=Text(x,y,width,height,is_shown,bg_color,layer_parent,text,text_color)
    def draw(self, screen):
        super().draw(screen)
        self.text.draw(screen)
    def touch_lmb_action(self,widget,app):
        # print("________")
        app.number+=1
    def holdown_lmb_action(self,widget,app):
        app.number=100
    def mouse_up_action(self, widget,app):
        super().mouse_up_action(app)
        app.number =100
    def minus_one(self,widget,app):
        app.number-=1
    # def draw(self, screen):


class LayerInspector:
    '''класс отвечает за порядок наслоения виджетов
        область его действия в глубину - 1 слой
        все плэйсхолдеры(как окно) должны содержать LayerInspector
        базовый layerInspector смотрит свою зону действия - окна
        затем зона дествия - внутри окна
        сравниваются, допустим, виджеты
        (этот подход позволяет создавать окна внутри окон)
        зы
        чем раньше слой в списке, тем он ниже
        '''
    def __init__(self):
        self.layers=[]

    def draw(self,screen):
        for obj in self.layers:
            obj.draw(screen)
            if obj.layers_inspector:
                obj.layers_inspector.draw(screen)

    def lift_object_up(self,obj):
        self.layers.pop(self.layers.index(obj))
        self.layers.append(obj)

    def check_actions(self,app):
        '''идея такова: есть только 1 виджет, с которым можно одновременно взаимодействовать
            это самый верхний(дальний) элемент списка
            поэтому если мы взамодействуем с ним нажатием кнопки, то мы поднимаем его наверх списка
            и вызываем действие'''

        #
        # x = app.mouse_pos[0]
        # y = app.mouse_pos[1]

        # print("________________")
        # for event in app.events:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         print("зарубите меня топором")
            # print(event)
        active_objects=[]
        # if self.widget.is_mouse_intersection(app.mouse_pos[0],app.mouse_pos[1]):
        # if 600<app.mouse_pos[0] <620 and 500<app.mouse_pos[1] <520:
        #     print("_____________")
        #     if  app.number == -1:
        #         print(app.events)
        #         for event in app.events:
        #             if event.type == pygame.MOUSEBUTTONDOWN:
        #                 breakpoint()
        for widget in range(len(self.layers)-1,-1,-1):
            self.layers[widget].keys_inspector.check_keys(app)
        for widget in range(len(self.layers)-1,-1,-1):
            if self.layers[widget].isactive:
                active_objects.append(self.layers[widget])
                # break
        # for widget in range(len(self.layers)):
        #     widget.make_unactive(app)

        for widget in active_objects:
            # widget.make_active(app)
            if widget.layers_inspector:
                widget.layers_inspector.check_actions(app)

    def change_active(self,widget,app):
        for obj in self.layers:
            # if obj == widget:
            #     breakpoint()
            obj.make_unactive()
        widget.make_active()

class RatioButtonsInspector(Widget):
    def __init__(self,x,y,width,height,is_shown,bg_color,layer_parent):
        super().__init__(x,y,width,height,is_shown,bg_color,layer_parent)
        self.layers_inspector = RatioButtonsLayer()
    def draw(self,screen):
        pass

class RatioButtonsLayer(LayerInspector):
    def __init__(self):
        super().__init__()
    def change_button(self,widget,app):
        for i in range(len(self.layers)):
            self.layers[i].state=False
        widget.state=True

class RatioButton(Widget):
    def __init__(self,x,y,width,height,is_shown,bg_color,layer_parent):
        super().__init__(x,y,width,height,is_shown,bg_color,layer_parent)
        self.border = 10
        self.state=False
        activate_combination = CombinationCheckers(self.layer_parent.change_button)
        activate_combination.checkers = [IntersectionChecker(), TouchChecker(1), UnStateChecker()]
        self.keys_inspector.checkers.append(activate_combination)
    def draw(self,screen):
        # pygame.draw.circle(screen,self.bg_color,)
        pygame.draw.ellipse(screen,self.bg_color,(self.x,self.y,self.width,self.height))
        if self.state:
            pygame.draw.ellipse(screen,(125,125,125),(self.x+self.border,self.y+self.border,
                                                      self.width-2*self.border,self.height-2*self.border))
class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.process_running = True
        self.stages=[Stage()]
        self.now_stage=0

    def mainloop(self):
        # while self.process_running:
        self.events_check()
        # print(len(self.all_events),self.all_events[0])
        self.stages[self.now_stage].mainloop(self.all_events)

    def events_check(self):
        self.events = pygame.event.get()
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_holdown = pygame.mouse.get_pressed()
        self.keys_holdown = pygame.key.get_pressed()
        # print(type(self.mouse_holdown))
        # print(type(pygame.K_w))
        # if type(self.keys_holdown) == pygame.key.ScancodeWrapper:
            # print("asdasdasdassasa")
        # print(type(self.events.but)
        # print(self.keys_holdown, pygame.K_w,self.keys_holdown[119])
        self.all_events=[self.events,self.mouse_pos,self.mouse_holdown,self.keys_holdown]
        # a = pygame.K_w
        # print(a)
        # if pygame.K_w in self.events:
        #     print("____________")
        # if len(self.events)>0:
        #     print(self.events[0], pygame.MOUSEBUTTONDOWN)
        # for event in self.events:
        #     if event.type==pygame.KEYUP:
        #         print(event.key)
        # print(self.keys_holdown)
        for event in self.events:
            if event.type == pygame.QUIT:
                self.process_running = False


class Stage:
    def __init__(self,width=1280,height=720):
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))


    def mainloop(self,all_events):

        self.events_check(all_events)
        self.drawing()
        self.updating()

    def drawing(self):
        self.screen.fill((0, 0, 0))

    def updating(self):
        pygame.display.update()


    def events_check(self,all_events):
        self.events = all_events[0]
        self.mouse_pos = all_events[1]
        self.mouse_holdown = all_events[2]
        self.keys_holdown = all_events[3]
        # print(self.mouse_holdown)
        # self.events = pygame.event.get()
        # self.mouse_pos = pygame.mouse.get_pos()
        # self.mouse_holdown = pygame.mouse.get_pressed()
        # for event in self.events:
        #     # if event.type == pygame.QUIT:
        #     #     self.process_running = False
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_ESCAPE:
        #             self.process_running = False

class Text(Widget):
    def __init__(self,x,y,width,height,is_shown,bg_color,layer_parent,text,text_color=(0,255,0)):
        super().__init__(x,y,width,height,is_shown,bg_color,layer_parent)
        self.text=text
        self.font = pygame.font.SysFont("Times New Roman", 50)
        self.text_color = text_color
    def draw(self,screen):
        surface = self.font.render(self.text, False, self.text_color)
        screen.blit(surface, (self.x, self.y))

class Checker:
    def __init__(self, key,func=None):
        '''keys представлены ввиде кодов клавиш, представленных
                    для клавиатуры pygame.K_<нужная клавиша>
                    для мыши число от 1 до 5'''
        self.func = func
        # self.alternative_func=widget.make_unactive()
        self.alternative_func=None
        self.key = key
        # self.widget=widget
    def check_action(self,widget,app):
        pass

class TouchChecker(Checker):
    def __init__(self, key,func=None):
        super().__init__(key,func)

    def check_action(self,widget,app):
        '''возможен баг- если в keydown event.key==1..5
            то прога может спутать их с клавишами мыши'''

        for event in app.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button  == self.key:
                    return True
            elif event.type==pygame.KEYDOWN:
                if event.key ==self.key:
                    return True
        return False

class EventUpChecker(Checker):
    def __init__(self, key,func=None):
        super().__init__(key,func)

    def check_action(self,widget,app):
        '''возможен баг- если в keydown event.key==1..5
            то прога может спутать их с клавишами мыши'''

        for event in app.events:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == self.key:
                    return True
            elif event.type==pygame.KEYUP:
                if event.key == self.key:
                    return True
        return False

class HoldChecker(Checker):
    def __init__(self, key,func=None):
        super().__init__(key,func)
        '''holding time - время(в фрэймах) через которое включится holdown_action'''
        # self.holding_time = 1000
        # self.holding_frames = [0 for i in range(len(self.keys))]
        # self.holding_frame=0

    def check_action(self,widget,app):
        # for key in range(len(self.keys)):
        if 0< self.key <4:
            '''если число на входе от 1 до 3, значит это клавиши мыши'''
            if app.mouse_holdown[self.key-1]:
                widget.holding_frame += 1
        else:
            if app.keys_holdown[self.key]:
                widget.holding_frame += 1

        if widget.holding_frame<widget.holding_time:
            return False
        return True
    #
    # def key_hold_checker(self,key,sourse):
    #     if self.keys[key] in sourse:
    #         if self.holding_frames[key] < self.holding_time:
    #             self.holding_frames[key]+=1
    #         return True
    #     else:
    #         self.holding_frames[key] = 0
    #
    #     return False
    #
    # def hold_checker(self):
    #     for key in range(len(self.keys)):
    #         # if self.keys[key].type ==pygame.key
    #         if type(self.keys[key]) == pygame.key.ScancodeWrapper:
    #             if self.key_hold_checker(key,1):
    #                 pass

class IntersectionChecker(Checker):
    def __init__(self,func=None):
        self.func = func
        # self.widget=widget
        # self.alternative_func = widget.make_unactive()
        self.alternative_func =None
    def check_action(self,widget,app):
        if widget.x < app.mouse_pos[0] < widget.x + widget.width and \
                widget.y < app.mouse_pos[1] < widget.y + widget.height:
            return True
        else:
            return False

class CombinationCheckers(Checker):
    def __init__(self,func,checkers=[]):
        self.func=func
        self.checkers=checkers
        self.alternative_func=None

    def check_action(self,widget,app):
        for checker in self.checkers:
            if not checker.check_action(widget,app):
                # pass
                return False
        # breakpoint()
        return True

class ActiveChecker(Checker):
    def __init__(self,func=None):
        self.func=func
        # self.widget=widget
        # self.alternative_func = widget.make_unactive()
        self.alternative_func = None

    def check_action(self,widget,app):
        if widget.isactive:
            return True
        return False

class UnActiveChecker(Checker):
    def __init__(self,func=None):
        self.func=func
        # self.widget=widget
        # self.alternative_func = widget.make_unactive()
        self.alternative_func = None

    def check_action(self,widget,app):
        if widget.isactive:
            return False
        return True

class UnStateChecker(Checker):
    def __init__(self,func=None):
        self.func=func
        self.alternative_func = None
    def check_action(self,widget,app):
        if widget.state:
            return False
        return True
class KeysInspector:
    def __init__(self,widget):
        self.checkers=[]
        self.widget = widget
    def check_keys(self,app):
        # print(app.mouse_pos[0],app.mouse_pos[1])
        # print(app.number,type(app.number))

        for checker in self.checkers:
            if checker.check_action(self.widget,app):
                if checker.func:
                    checker.func(self.widget,app)
            else:
                if checker.alternative_func:
                    checker.alternative_func(app)

            # if self.is_intersection(self.widget, app):
            #
            #     if checker.check_action(self.widget, app):
            #         checker.func(app)
            # else:
            #     if self.widget.isactive:
            #         if checker.check_action(self.widget, app):
            #             checker.func(app)
        # if self.widget.isactive:
        #     return True
        # return False


    # def is_intersection(self,widget,app):
    #     if widget.x<app.mouse_pos[0]<widget.x+widget.width and \
    #             widget.y < app.mouse_pos[1] < widget.y + widget.height:
    #         return True
    #     else:
    #         return False
