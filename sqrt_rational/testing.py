from manim import *
from manim_voiceover import VoiceoverScene

config.background_color = BLACK
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width = 1920
config.background_opacity = 1


class Part2_voiceover(VoiceoverScene):
    def construct(self):
        contradiction_demo = MathTex(
            r"\sqrt{2} \in \mathbb{Q} \Longrightarrow A \text{ and } B \text{ where } A \text{ and } B \text{ is impossible} \Longrightarrow \sqrt{2} \notin \mathbb{Q}",
            color="WHITE",
            font_size=40
        )

        self.play(Write(contradiction_demo))

        self.add(index_labels(contradiction_demo[0]))

        self.wait(2)