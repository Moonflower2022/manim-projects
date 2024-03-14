from manim import *

config.background_color = BLACK
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width = 1920
config.background_opacity = 1


class Part2(Scene):
    def construct(self):
        # explain both

        absurd_proof1part1 = MathTex(
            r"1 &= \sqrt{1} \\ &= \sqrt{(-1) \cdot (-1)} \\ &= \sqrt{-1} \cdot \sqrt{-1} \\ &= -1", 
            font_size=40, 
            color=WHITE
        )

        # in the first part of the first proof, the multiplicative identity doesnt hold for negative numbers

        multiplicative_identity = MathTex(
            r"\sqrt{a} \cdot \sqrt{b} = \sqrt{a \cdot b}", 
            font_size=40, 
            color=WHITE
        ).move_to([4, 0, 0])

        square_root_identity = MathTex(
            r"\sqrt{c} \cdot \sqrt{c} = c", 
            font_size=40, 
            color=WHITE
        ).move_to([4, -0.75, 0])

        self.play(FadeIn(Group(absurd_proof1part1, multiplicative_identity, square_root_identity)))

        self.play(absurd_proof1part1[0][5:17].animate.set_color(PURE_GREEN))

        self.play(absurd_proof1part1[0][17:27].animate.set_color(PURE_RED))

        self.play(FadeOut(Group(absurd_proof1part1, multiplicative_identity, square_root_identity)))

        # absurd proof #2

        absurd_proof2 = MathTex(
            r"a, b \neq 0 \text{ and } a &= b \\ a^2 &= ab \\ a^2 - b^2 &= ab - b^2 \\ (a+b)(a-b) &= b(a-b) \\ a + b &= b \\ 2a &= a \\ 2 &= 1 \\ 1 &= 0", 
            font_size=40, 
            color=WHITE
        )

        self.play(Write(absurd_proof2))

        self.play(absurd_proof2[0][28:45].animate.set_color(PURE_GREEN))

        self.play(absurd_proof2[0][45:50].animate.set_color(PURE_RED))

        self.play(FadeOut(absurd_proof2))

        # in fact, the square root of 2 is irrational, and there is a very common proof that exemplifies this. 
        # It is in the format of a proof by contradiction, where we start by assuming something about sqrt(2) 
        # and arriving to a contradiction that shows our original assumption has to be incorrect.

        # we start by assuming that the square root of 2 is rational. From our definition of rationality, 
        # this means that sqrt(2) is equivalent to two integers

        assumption = Text("Assumption:", font_size=40, color=WHITE)

        assumption_latex = MathTex(r"\sqrt{2} \in \mathbb{R}", font_size=40, color=WHITE).move_to([0, -1, 0])

        self.play(FadeIn(Group(assumption, assumption_latex)))

        rational_def = MathTex(r"\sqrt{2} = \frac{p}{q}, \text{where } p, q \in \mathbb{Z}, \gcd(p, q) = 1, \text{and } q > 0", font_size=40, color=WHITE)

        self.play(ReplacementTransform(Group(assumption, assumption_latex), rational_def))

        self.wait()

        self.play(rational_def.animate.scale(0.5).to_corner(UL))

        irrationality_proof = MathTex(
            r"\sqrt{2} &= \frac{p}{q} \\ q\sqrt{2} &= p \\ 2q^2 &= p^2 \\ 2q^2 &= (2k)^2 \\ 2q^2 &= 4k^2 \\ q^2 &= 2k^2", 
            font_size=40, 
            color=WHITE
        )

        self.play(Write(irrationality_proof[0][:7]))

        self.wait()

        self.play(Write(irrationality_proof[0][7:13]))

        self.wait()

        self.play(Write(irrationality_proof[0][13:19]))

        self.wait()

        # observe that p^2 is even

        # substitute and plug in

        self.play(Write(irrationality_proof[0][19:28]))

        self.wait()

        # simplify

        self.play(Write(irrationality_proof[0][28:35]))

        self.wait()

        self.play(Write(irrationality_proof[0][35:]))

        # observe that q^2 is even

        self.wait()

