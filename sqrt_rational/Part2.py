from manim import *

config.background_color = BLACK
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width = 1920
config.background_opacity = 1


class Part2(Scene):
    def construct(self):
        one_neq_zero = MathTex(
            r"1 \neq 0",
            color=WHITE,
            font_size=40
        )

        self.play(FadeIn(one_neq_zero))
        self.play(FadeOut(one_neq_zero))    

        absurd_proof1part1 = MathTex(
            r"1 &= \sqrt{1} \\ &= \sqrt{(-1) \cdot (-1)} \\ &= \sqrt{-1} \cdot \sqrt{-1} \\ &= -1", 
            font_size=40, 
            color=WHITE
        )

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

        absurd_proof2 = MathTex(
            r"a, b \neq 0 \text{ and } a &= b \\ a^2 &= ab \\ a^2 - b^2 &= ab - b^2 \\ (a+b)(a-b) &= b(a-b) \\ a + b &= b \\ 2a &= a \\ 2 &= 1 \\ 1 &= 0", 
            font_size=40, 
            color=WHITE
        )

        self.play(FadeIn(absurd_proof2))

        self.play(absurd_proof2[0][28:45].animate.set_color(PURE_GREEN))
        self.play(absurd_proof2[0][45:50].animate.set_color(PURE_RED))

        self.play(FadeOut(absurd_proof2))

        contradiction_demo = MathTex(
            r"\sqrt{2} \in \mathbb{Q} \Longrightarrow A \text{ and } B?? \Longrightarrow \sqrt{2} \notin \mathbb{Q}",
            color="WHITE",
            font_size=40
        )

        self.play(Write(contradiction_demo[0][:5]))
        self.play(Write(contradiction_demo[0][5:34]))
        self.play(Write(contradiction_demo[0][34:]))

        self.play(FadeOut(contradiction_demo))
        
        assumption = Text("Assumption:", font_size=40, color=WHITE)

        assumption_latex = MathTex(r"\sqrt{2} \in \mathbb{Q}", font_size=40, color=WHITE).move_to([0, -1, 0])

        self.play(FadeIn(assumption))
        self.play(FadeIn(assumption_latex))

        rational_def = MathTex(r"\sqrt{2} = \frac{p}{q}, \text{where } p, q \in \mathbb{Z}, \gcd(p, q) = 1, \text{and } q > 0", font_size=40, color=WHITE)

        self.play(ReplacementTransform(Group(assumption, assumption_latex), rational_def))

        self.play(rational_def.animate.scale(0.5).to_corner(UL))

        irrationality_proof = MathTex(
            r"\sqrt{2} &= \frac{p}{q} \\ q\sqrt{2} &= p \\ 2q^2 &= p^2 \\ 2q^2 &= (2k)^2 \\ 2q^2 &= 4k^2 \\ q^2 &= 2k^2", 
            font_size=40, 
            color=WHITE
        ).move_to([-2, 0, 0])

        self.play(Write(irrationality_proof[0][:7]))

        self.play(Write(irrationality_proof[0][7:13]))

        self.play(Write(irrationality_proof[0][13:19]))

        self.play(irrationality_proof[0][13:14].animate.set_color(YELLOW))
        self.play(irrationality_proof[0][13:14].animate.set_color(WHITE))

        odd_int_explaination = MathTex(r"(2k + 1)^2 &= 4k^2 + 4k + 1 \\ &= 2(2k^2 + 2k) + 1", color=YELLOW_A, font_size=40).move_to([3.5, 2.5, 0])
        even_int_explaination = MathTex(r"(2k)^2 = 4k^2 = 2(2k^2)", color=YELLOW_A, font_size=40).move_to([3.5, 1.5, 0])

        p_even = MathTex(r"p = 2n, n \in \mathbb{Z}", color=WHITE, font_size=40).move_to([0.7, 0.14, 0])

        self.play(Write(odd_int_explaination))

        self.play(Write(even_int_explaination))

        self.play(Write(p_even))

        self.play(Write(irrationality_proof[0][19:28]))        

        self.play(Write(irrationality_proof[0][28:35]))
        self.wait(0.5)
        self.play(Write(irrationality_proof[0][35:]))

        q_even = MathTex(r"q = 2m, m \in \mathbb{Z}", color=WHITE, font_size=40).move_to([0.7, -1.9, 0])

        self.play(Write(q_even))
        
        self.play(FadeOut(Group(irrationality_proof, odd_int_explaination, even_int_explaination)))
        self.play(AnimationGroup(q_even.animate.move_to([1.5, 0, 0]), p_even.animate.move_to([-1.5, 0, 0])))
        self.play(rational_def.animate.move_to([0, -1, 0]).scale(2))

        result = MathTex(r"\sqrt{2} \notin \mathbb{Q}", color=WHITE, font_size=40)

        self.play(ReplacementTransform(Group(rational_def, q_even, p_even), result))

        self.wait(1)
        
        self.play(FadeOut(result))