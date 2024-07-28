import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyLayout(BoxLayout):
    def selected(self, filename):
        self.filename = filename
        self.ids.my_video.source = self.filename[0]
        
    def convert_to_mp3(self):
        videofile = self.filename[0]
        audiofile = 'myaudio.mp3'
        
        videoclip = VideoFileClip(videofile) # type: ignore
        audioclip = videoclip.audio
        audioclip.write_audiofile(audiofile)
        
        while True:
            self.ids.show_process.value += 1
            time.sleep(.01)
            if self.ids.show_process.value >= 100:
                break
            
            videoclip.close()
            audioclip.close()

class AniipPlayer (App):
    pass

AniipPlayer().run()