from manim import *

class ProductRuleProof(Scene):
    def construct(self):
        # Title
        title = Text("Product Rule for Derivatives", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Narration 1
        narration1 = Paragraph(
            "We want to find the derivative of the product f(x)g(x).",
            font_size=28,
            alignment="LEFT",
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(narration1))
        self.wait(2)

        # Step 1: Start with derivative definition
        formula1 = MathTex(
            r"\frac{d}{dx}[f(x)g(x)] = \lim_{h \to 0} \frac{f(x+h)g(x+h) - f(x)g(x)}{h}"
        ).scale(0.85)
        formula1.next_to(title, DOWN, buff=1)

        self.play(Write(formula1))
        self.wait(3)

        # Narration 2
        narration2 = Paragraph(
            "Add and subtract f(x+h)g(x) in the numerator to help us break this apart.",
            font_size=28,
            alignment="LEFT"
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(narration1, narration2))
        self.wait(2)

        # Step 2: Add and subtract f(x+h)g(x)
        formula2 = MathTex(
            r"= \lim_{h \to 0} \frac{f(x+h)g(x+h) - f(x+h)g(x) + f(x+h)g(x) - f(x)g(x)}{h}"
        ).scale(0.85)
        formula2.next_to(formula1, DOWN, buff=0.75)
        self.play(Write(formula2))
        self.wait(3)

        # Narration 3
        narration3 = Paragraph(
            "Now group the terms into two fractions.",
            font_size=28,
            alignment="LEFT"
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(narration2, narration3))
        self.wait(2)

        # Step 3: Group terms
        formula3 = MathTex(
            r"= \lim_{h \to 0} \left[ \frac{f(x+h)(g(x+h) - g(x))}{h} + \frac{g(x)(f(x+h) - f(x))}{h} \right]"
        ).scale(0.8)
        formula3.next_to(formula2, DOWN, buff=0.75)
        self.play(Write(formula3))
        self.wait(3)

        # Narration 4
        narration4 = Paragraph(
            "Now take the limit of each part separately.",
            font_size=28,
            alignment="LEFT"
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(narration3, narration4))
        self.wait(2)

        # Step 4: Take the limit
        formula4 = MathTex(
            r"= f(x) \cdot \lim_{h \to 0} \frac{g(x+h) - g(x)}{h} + g(x) \cdot \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}"
        ).scale(0.8)
        formula4.next_to(formula3, DOWN, buff=0.75)
        self.play(Write(formula4))
        self.wait(3)

        # Narration 5
        narration5 = Paragraph(
            "This gives us the product rule!",
            font_size=28,
            alignment="LEFT"
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(narration4, narration5))
        self.wait(2)

        # Final result
        final_result = MathTex(
            r"\frac{d}{dx}[f(x)g(x)] = f(x)g'(x) + f'(x)g(x)",
            color=YELLOW
        ).scale(1.2)
        final_result.next_to(formula4, DOWN, buff=1)

        self.play(Write(final_result))
        self.wait(3)

        # Clean up narration
        self.play(FadeOut(narration5))
        self.wait(1)

        # Closing note
        closing_text = Paragraph(
            "You can run this animation using this notebook:\n"
            "https://notebooks.gesis.org/binder/jupyter/user/manimcommunity-jupyter_examples-eraq1g2y/notebooks/First%20Steps%20with%20Manim.ipynb",
            font_size=26,
            alignment="LEFT"
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(closing_text))
        self.wait(4)