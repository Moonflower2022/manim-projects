from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

class voiceover_test_scene(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService())
        self.set_speech_service(RecorderService(silence_threshold=-40.0))

        with self.voiceover(text="Hi, I am a sunflower.") as tracker:
            self.play(Create(Rectangle()))
        