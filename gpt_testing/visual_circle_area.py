from manim import *

class CircleAreaProof(Scene):
    def construct(self):
        # Title
        title = Text("Why is Area of a Circle = πr²?", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Narration
        narration1 = Paragraph(
            "Let's slice the circle into sectors and rearrange them to find the area.",
            font_size=28
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(narration1))
        self.wait(2)

        # Draw circle
        r = 2
        circle = Circle(radius=r, color=YELLOW).shift(LEFT * 3)
        self.play(Create(circle))
        self.wait(1)

        # Slice into sectors
        num_sectors = 20
        angle = TAU / num_sectors
        sectors = VGroup()

        for i in range(num_sectors):
            sector = AnnularSector(
                inner_radius=0,
                outer_radius=r,
                angle=angle,
                start_angle=i * angle,
                fill_opacity=0.7,
                color=YELLOW,
                stroke_color=WHITE,
                stroke_width=1,
            ).shift(LEFT * 3)
            sectors.add(sector)

        self.play(FadeOut(circle), Create(sectors))
        self.wait(1)

        # Rearranged sectors into parallelogram-like shape
        arranged_sectors = VGroup()
        for i, sector in enumerate(sectors):
            s = sector.copy()
            # Rotate alternate sectors to form the zig-zag pattern
            if i % 2 == 0:
                s.rotate(-angle / 2)
                s.shift(RIGHT * (i // 2) * 0.4 + UP * 0.5)
            else:
                s.rotate(angle / 2)
                s.shift(RIGHT * (i // 2) * 0.4 + DOWN * 0.5)
            arranged_sectors.add(s)

        self.play(*[Transform(sectors[i], arranged_sectors[i]) for i in range(num_sectors)])
        self.wait(2)

        # Narration update
        narration2 = Paragraph(
            "This resembles a parallelogram. Base ≈ half the circumference: πr, and height = r.",
            font_size=28
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(narration1, narration2))
        self.wait(2)

        # Labels for base and height
        base = MathTex(r"\pi r", color=WHITE).scale(1.2).next_to(arranged_sectors, DOWN, buff=0.3)
        height = MathTex("r", color=WHITE).scale(1.2).next_to(arranged_sectors, LEFT, buff=0.3)
        self.play(Write(base), Write(height))
        self.wait(2)

        # Narration update
        narration3 = Paragraph(
            "Area ≈ base × height = πr × r = πr²",
            font_size=28
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(narration2, narration3))
        self.wait(2)

        # Final formula
        final_formula = MathTex(r"\text{Area} = \pi r^2", color=YELLOW).scale(1.6)
        final_formula.next_to(title, DOWN, buff=1.5)

        self.play(Write(final_formula))
        self.wait(3)

        self.play(FadeOut(narration3))

        # Outro
        outro = Paragraph(
            "You can run this animation in the Manim notebook:\n"
            "https://notebooks.gesis.org/binder/jupyter/user/manimcommunity-jupyter_examples-eraq1g2y/notebooks/First%20Steps%20with%20Manim.ipynb",
            font_size=26
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(outro))
        self.wait(4)