from kivy.app import App
from kivy.uix.widget import Widget

class MyW(Widget):
    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.ids.label1.text = 'Touch is a triple tap! - The Interval is: ' + str(touch.double_tap_time)
        elif touch.is_triple_tap:
            self.ids.label1.text = 'Touch is a Triple tap! - The interval is: {0} and distance between previous is {1}'.format(touch.triple_tap_time, touch.triple_tap_distance)
            
class e7App(App):
    def build(self):
        return MyW()
        
if __name__ == '__main__':
    e7App().run()
