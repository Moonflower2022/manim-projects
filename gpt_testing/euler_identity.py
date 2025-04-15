from manim import *

class EulerIdentity(Scene):
    def construct(self):
        # Title
        title = Text("Euler's Identity", font_size=60, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Narration 1
        narration_1 = Paragraph(
            "Euler's identity is often called the most beautiful equation in mathematics.",
            font_size=28,
            alignment="LEFT",
            width=10
        )
        narration_1.to_edge(DOWN, buff=0.5)
        self.play(Write(narration_1))
        self.wait(2)

        # Euler's identity equation
        eq = MathTex("e^{i\\pi} + 1 = 0", font_size=80)
        eq.set_color_by_tex("e", BLUE)
        eq.set_color_by_tex("i", GREEN)
        eq.set_color_by_tex("\\pi", RED)
        eq.set_color_by_tex("1", ORANGE)
        eq.set_color_by_tex("0", PURPLE)
        eq.move_to(ORIGIN)
        self.play(Write(eq))
        self.wait(2)

        # Narration 2
        self.play(FadeOut(narration_1))
        narration_2 = Paragraph(
            "It brings together five fundamental constants: e, i, π, 1, and 0.",
            font_size=28,
            alignment="LEFT",
            width=10
        )
        narration_2.to_edge(DOWN, buff=0.5)
        self.play(Write(narration_2))
        self.wait(2)

        # Highlight constants individually
        highlights = VGroup()
        for tex, label_text, color in [
            ("e", "Euler's number (≈2.718)", BLUE),
            ("i", "Imaginary unit (√-1)", GREEN),
            ("\\pi", "Pi (≈3.14159)", RED),
            ("1", "Multiplicative identity", ORANGE),
            ("0", "Additive identity", PURPLE)
        ]:
            self.play(eq.animate.set_color_by_tex(tex, YELLOW))
            label = Text(label_text, font_size=30, color=color)
            label.next_to(eq, DOWN, buff=0.7)
            self.play(FadeIn(label))
            self.wait(1.5)
            self.play(FadeOut(label))
            self.play(eq.animate.set_color_by_tex(tex, color))

        # Narration 3
        self.play(FadeOut(narration_2))
        narration_3 = Paragraph(
            "Euler's identity is a deep connection between algebra, geometry, and analysis.",
            font_size=28,
            alignment="LEFT",
            width=10
        )
        narration_3.to_edge(DOWN, buff=0.5)
        self.play(Write(narration_3))
        self.wait(2)

        # Fade out all
        self.play(FadeOut(eq), FadeOut(title), FadeOut(narration_3))

        # Final message
        final_msg = Text("Mathematics is beautiful.", font_size=50, color=WHITE)
        final_msg.move_to(ORIGIN)
        self.play(Write(final_msg))
        self.wait(2)
        self.play(FadeOut(final_msg))