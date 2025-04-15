from manim import *

class CauchyIntegralFormula(Scene):
    def construct(self):
        # Title
        title = Text("Cauchy Integral Formula", font_size=48, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Narration 1
        narration_1 = Paragraph(
            "Let f be holomorphic inside and on a closed curve C.",
            font_size=24, alignment="LEFT", line_spacing=0.8
        )
        narration_1.to_edge(DOWN, buff=0.5)
        self.play(Write(narration_1))
        self.wait(1)

        # Circle representing contour C
        circle = Circle(radius=2, color=BLUE)
        circle.move_to(ORIGIN)

        # Point z0 inside the circle
        z0_dot = Dot(point=[0.5, 0.5, 0], color=RED)
        z0_label = MathTex("z_0", font_size=30)
        z0_label.next_to(z0_dot, RIGHT, buff=0.15)

        # Label for the contour C
        c_label = MathTex("C", font_size=30)
        c_label.next_to(circle, RIGHT, buff=0.15)

        # Group the objects
        diagram = VGroup(circle, z0_dot, z0_label, c_label)
        diagram.scale(1.2)
        self.play(Create(circle), FadeIn(z0_dot), Write(z0_label), Write(c_label))
        self.wait(1)

        # Narration 2
        self.play(FadeOut(narration_1))
        narration_2 = Paragraph(
            "The Cauchy Integral Formula states that the value of f at z₀ is given by:",
            font_size=24, alignment="LEFT", line_spacing=0.8
        )
        narration_2.to_edge(DOWN, buff=0.5)
        self.play(Write(narration_2))
        self.wait(2)

        # Show the integral formula
        formula = MathTex(
            r"f(z_0) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - z_0} \, dz",
            font_size=36
        )
        formula.next_to(diagram, DOWN, buff=0.8)
        self.play(Write(formula))
        self.wait(3)

        # Highlight each part of the formula
        self.play(formula.animate.set_color_by_tex("f(z_0)", RED))
        self.wait(1)
        self.play(formula.animate.set_color_by_tex("C", BLUE))
        self.wait(1)
        self.play(formula.animate.set_color_by_tex("z_0", RED))
        self.wait(1)

        # Final narration
        self.play(FadeOut(narration_2))
        narration_3 = Paragraph(
            "This powerful formula allows us to compute f(z₀) using only the values of f on the boundary C!",
            font_size=24, alignment="LEFT", line_spacing=0.8
        )
        narration_3.to_edge(DOWN, buff=0.5)
        self.play(Write(narration_3))
        self.wait(3)

        # Fade out
        self.play(FadeOut(VGroup(title, diagram, formula, narration_3)))
        self.wait(1)

        # Final Message
        thanks = Text("Thanks for watching!", font_size=36, color=GREEN)
        thanks.move_to(ORIGIN)
        self.play(Write(thanks))
        self.wait(2)