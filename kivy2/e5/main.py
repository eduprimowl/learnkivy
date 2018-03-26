from kivy.app import App
from kivy.uix.widget import Widget

class MyW(Widget):
    '''    
    def on_touch_move(self, touch):
        if 'pos' in touch.profile:
            self.ids.button1.pos = touch.pos
    '''           
    def on_touch_down(self, touch):
        if 'button' in touch.profile:
            self.ids.button1.text = touch.button
            
class e5App(App):
    def build(self):
        return MyW()

if __name__ == '__main__':
    e5App().run()