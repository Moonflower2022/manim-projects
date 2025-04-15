from manim import *
import numpy as np

class LeftRiemannSqrt(Scene):
    def construct(self):
        # Title
        title = Text("Left Riemann Sum of √x from 3 to 5 (Δx = 0.1)", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Narration
        narration_1 = Paragraph(
            "We are approximating the area under f(x) = √x from x = 3 to x = 5",
            font_size=24,
            alignment="LEFT",
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(narration_1))
        self.wait(2)

        # Axes setup
        axes = Axes(
            x_range=[2.5, 5.5, 0.5],
            y_range=[0, 2.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"color": WHITE},
            tips=False
        ).to_edge(LEFT, buff=0.5)

        # Function
        graph = axes.plot(lambda x: np.sqrt(x), color=BLUE)
        func_label = axes.get_graph_label(graph, label="\\sqrt{x}", x_val=4.2, direction=UP)

        # Show axes and function
        self.play(Create(axes), Create(graph), Write(func_label))
        self.wait(1)

        # Narration
        narration_2 = Paragraph(
            "We divide the interval [3, 5] into subintervals of width 0.1.",
            font_size=24,
            alignment="LEFT",
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.5)
        self.play(Transform(narration_1, narration_2))
        self.wait(2)

        # Define Riemann rectangles
        dx = 0.1
        rects = VGroup()

        rects = axes.get_riemann_rectangles(
                graph=graph,
                x_range=[3., 5.],
                dx=dx,
                input_sample_type="left",
                color=GREEN,
                stroke_width=0.5
            )


        # Narration
        narration_3 = Paragraph(
            "Using the left endpoints, we draw rectangles whose height is √(left x).",
            font_size=24,
            alignment="LEFT",
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.5)
        self.play(Transform(narration_1, narration_3))
        self.wait(2)

        # Animate Riemann rectangles
        self.play(Create(rects))
        self.wait(2)

        # Final narration
        narration_4 = Paragraph(
            "The sum of the areas of these rectangles approximates the total area under √x.",
            font_size=24,
            alignment="LEFT",
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.5)
        self.play(Transform(narration_1, narration_4))
        self.wait(3)

        # Fade out everything
        self.play(FadeOut(rects), FadeOut(graph), FadeOut(axes), FadeOut(title), FadeOut(narration_1), FadeOut(func_label))

        # Show outro text
        outro = Text("Run this code in the Manim Jupyter notebook 👇", font_size=28)
        outro.to_edge(DOWN, buff=1)
        self.play(Write(outro))
        self.wait(2)