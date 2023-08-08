import pygame
import base_classes5 as baseClasses


class DemoScene(baseClasses.Stage):
    def __init__(self):
        super().__init__()

        self.layers_inspector = baseClasses.LayerInspector()
        # self.layers_inspector.layers = [self.window]
        self.ratio_buttons_inspector =  baseClasses.RatioButtonsInspector(50,50,50,150,True,(100,100,100),self.layers_inspector)
        self.rationbutton1=baseClasses.RatioButton(50,50,50,50,True,(255,255,255),self.ratio_buttons_inspector.layers_inspector)
        self.rationbutton2=baseClasses.RatioButton(50,100,50,50,True,(255,255,255),self.ratio_buttons_inspector.layers_inspector)
        self.rationbutton3=baseClasses.RatioButton(50,150,50,50,True,(255,255,255),self.ratio_buttons_inspector.layers_inspector)

        # self.window=baseClasses.Window(200,100,100,100,True,(0,255,0),self.layers_inspector)
        self.text1=baseClasses.Text(110,50,1,1,True,(1,1,1),self.layers_inspector,"за Путина")
        self.text2=baseClasses.Text(110,100,1,1,True,(1,1,1),self.layers_inspector,"за Медведева")
        self.text3=baseClasses.Text(110,150,1,1,True,(1,1,1),self.layers_inspector,"за Жириновского")

        self.layers_inspector.layers=[self.ratio_buttons_inspector,self.text1,self.text2,self.text3]
        self.ratio_buttons_inspector.layers_inspector.layers=[self.rationbutton1,self.rationbutton2,self.rationbutton3]
    def drawing(self):
        self.screen.fill((0,0,0))
        self.layers_inspector.draw(self.screen)

    def events_check(self,all_events):
        super().events_check(all_events)
        self.layers_inspector.check_actions(self)

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