from manim import *

class PythagoreanProof(Scene):
    def construct(self):
        # Title
        title = Text("Visual Proof of the Pythagorean Theorem", font_size=48, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Narration helper function
        def narrate(text_str):
            narration = Paragraph(text_str, font_size=24, alignment="left", line_spacing=0.8, width=6)
            narration.to_edge(DOWN, buff=0.5)
            self.play(Write(narration))
            self.wait(2)
            self.play(FadeOut(narration))

        # First large square with 4 triangles and two smaller squares (a² and b²)
        triangle1 = Polygon([0, 0, 0], [3, 0, 0], [0, 4, 0], color=BLUE, fill_opacity=0.5)
        triangle2 = triangle1.copy().rotate(PI/2).shift(RIGHT*3)
        triangle3 = triangle2.copy().rotate(PI/2).shift(UP*4)
        triangle4 = triangle3.copy().rotate(PI/2).shift(LEFT*3)

        # Squares a^2 and b^2
        square_a = Square(3, color=GREEN, fill_opacity=0.5).move_to([1.5, 5.5, 0])
        square_b = Square(4, color=RED, fill_opacity=0.5).move_to([5.5, 2, 0])

        group1 = VGroup(triangle1, triangle2, triangle3, triangle4, square_a, square_b)
        group1.move_to(LEFT*4).scale(0.6)

        self.play(Create(triangle1))
        self.play(Create(triangle2))
        self.play(Create(triangle3))
        self.play(Create(triangle4))
        self.wait(0.5)
        self.play(FadeIn(square_a), FadeIn(square_b))

        narrate("We start with a large square made from four identical right triangles.")

        narrate("Inside the square, two smaller squares are formed with areas a² and b².")

        # Second square with hole c^2
        triangle1b = triangle1.copy()
        triangle2b = triangle2.copy()
        triangle3b = triangle3.copy()
        triangle4b = triangle4.copy()

        square_c = Square(np.sqrt(3**2 + 4**2), color=ORANGE, fill_opacity=0.5).move_to([3, 2, 0])

        group2 = VGroup(triangle1b, triangle2b, triangle3b, triangle4b, square_c)
        group2.scale(0.6).move_to(RIGHT*4)

        self.play(Create(triangle1b))
        self.play(Create(triangle2b))
        self.play(Create(triangle3b))
        self.play(Create(triangle4b))
        self.wait(0.5)
        self.play(FadeIn(square_c))

        narrate("Now we rearrange the same four triangles.")

        narrate("This time, the empty space forms a single square with area c².")

        # Emphasize final proof
        equation = MathTex("a^2 + b^2 = c^2", font_size=48)
        equation.next_to(group2, DOWN, buff=1)
        self.play(Write(equation))
        self.wait(2)

        narrate("Since both arrangements use the same shapes and area, we conclude:")
        narrate("a² + b² = c²")

        # End note
        end_note = Paragraph(
            "You can run this animation in your browser using this notebook:\n"
            "https://notebooks.gesis.org/binder/jupyter/user/manimcommunity-jupyter_examples-eraq1g2y/notebooks/First%20Steps%20with%20Manim.ipynb",
            font_size=20, alignment="center", line_spacing=0.9, width=8
        )
        end_note.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(end_note))
        self.wait(4)