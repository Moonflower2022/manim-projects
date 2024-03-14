from manim import *

config.background_color = WHITE
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width = 1920
config.background_opacity = 1


class Part1(Scene):
    def construct(self):
        self.wait(1)
        tex = MathTex(r"\sqrt{2} \notin \mathbb{R}", font_size=100, color=BLACK)

        self.play(Write(tex))

        self.wait(1)

        other_radicals = MathTex(r"\sqrt{2}, \sqrt{3}, \sqrt{5}, \sqrt{6}, \cdots \notin \mathbb{R}", font_size=100, color=BLACK)

        self.play(ReplacementTransform(tex, other_radicals))

        self.wait(1)

        x_lines = Group(
            Line(other_radicals.get_critical_point(UL), other_radicals.get_critical_point(DR), color=RED), 
            Line(other_radicals.get_critical_point(UR), other_radicals.get_critical_point(DL), color=RED)
        )

        self.play(FadeIn(x_lines))

        self.wait()

        self.play(AnimationGroup(FadeOut(other_radicals), FadeOut(x_lines)))

        rational_def = MathTex(r"x \in \mathbb{R} \iff x = \frac{p}{q}, \text{where } p, q \in \mathbb{Z} \text{ and } \gcd(p, q) = 1", font_size=40, color=BLACK)

        self.play(Write(rational_def))

        self.wait(1)

        self.play(rational_def.animate.scale(0.5).to_corner(UL))

        self.wait(1)

        pondering = MathTex(r"\sqrt{2} = \frac{p}{q}", font_size=40, color=BLACK)

        self.play(Write(pondering))

        self.wait()

        self.play(FadeOut(pondering))

        self.wait()

        # absurd proof #1

        absurd_proof1part1 = MathTex(
            r"1 &= \sqrt{1} \\ &= \sqrt{(-1) \cdot (-1)} \\ &= \sqrt{-1} \cdot \sqrt{-1} \\ &= -1", 
            font_size=40, 
            color=BLACK
        )

        absurd_proof1part2 = MathTex(
            r"1 &= -1 \\ 2 &= 0 \\ 1 &= 0",
            font_size=40,
            color=BLACK
        )

        multiplicative_identity = MathTex(
            r"\sqrt{a} \cdot \sqrt{b} = \sqrt{a \cdot b}", 
            font_size=40, 
            color=BLACK
        ).move_to([4, 0, 0])

        square_root_identity = MathTex(
            r"\sqrt{c} \cdot \sqrt{c} = c", 
            font_size=40, 
            color=BLACK
        ).move_to([4, -0.75, 0])

        self.play(Write(absurd_proof1part1[0][:5]))

        self.wait()

        self.play(Write(absurd_proof1part1[0][5:17]))

        self.wait()

        self.play(Write(multiplicative_identity))

        self.wait()

        self.play(Write(absurd_proof1part1[0][17:27]))

        self.wait()

        self.play(Write(square_root_identity))

        self.wait()

        self.play(Write(absurd_proof1part1[0][27:]))

        self.wait()

        self.play(ReplacementTransform(Group(absurd_proof1part1, multiplicative_identity, square_root_identity), absurd_proof1part2[0][:4]))

        self.wait()
        
        self.play(Write(absurd_proof1part2[0][4:7]))

        self.wait()

        self.play(Write(absurd_proof1part2[0][7:10]))

        self.wait()

        self.play(FadeOut(absurd_proof1part2))

        meme1 = ImageMobject("meme1.png", scale_to_resolution=1920)

        self.play(FadeIn(meme1))

        # if you still dont believe me, here is another proof:

        self.wait()
        
        self.play(FadeOut(meme1))

        # absurd proof #2

        absurd_proof2 = MathTex(
            r"a, b \neq 0 \text{ and } a &= b \\ a^2 &= ab \\ a^2 - b^2 &= ab - b^2 \\ (a+b)(a-b) &= b(a-b) \\ a + b &= b \\ 2a &= a \\ 2 &= 1 \\ 1 &= 0", 
            font_size=40, 
            color=BLACK
        )

        self.play(Write(absurd_proof2[0][:12]))

        self.wait()

        self.play(Write(absurd_proof2[0][12:17]))

        self.wait()

        self.play(Write(absurd_proof2[0][17:28]))

        self.wait()

        self.play(Write(absurd_proof2[0][28:45]))

        self.wait()

        # if you don't believe that this is true, just try to multiply a+b and a-b...

        explaination1 = MathTex(r"(a+b)(a-b)", font_size=40, color=BLACK).move_to([-4.5, 0, 0])

        self.play(Write(explaination1))

        self.wait()

        explaination2 = MathTex(r"a^2 + a \cdot b - a \cdot b - b^2", font_size=40, color=BLACK).move_to([-4.5, 0, 0])

        self.play(ReplacementTransform(explaination1, explaination2))

        self.wait()

        explaination3 = MathTex(r"a^2 - b^2", font_size=40, color=BLACK).move_to([-4.5, 0, 0])

        self.play(ReplacementTransform(explaination2, explaination3))

        self.wait()

        self.play(FadeOut(explaination3))

        self.play(Write(absurd_proof2[0][45:50]))

        self.wait()

        self.play(Write(absurd_proof2[0][50:54]))

        self.wait()

        self.play(Write(absurd_proof2[0][54:57]))

        self.wait()

        self.play(Write(absurd_proof2[0][57:60]))

        self.wait()

        absurd_identity = MathTex(r"1 = 0", font_size=40, color=BLACK)

        self.play(ReplacementTransform(absurd_proof2, absurd_identity))

        self.play(absurd_identity.animate.to_corner(UR))

        rationality_proof = MathTex(
            r"\sqrt{2} &= \frac{\sqrt{2}}{1} \\ &= \frac{\sqrt{1 + 1}}{1} \\ &= \frac{\sqrt{1 + 0}}{1} \\ &= \frac{\sqrt{1}}{1} \\ &= \frac{1}{1}", 
            font_size=40, 
            color=BLACK
        )

        self.play(Write(rationality_proof[0][:9]))

        self.wait()

        self.play(Write(rationality_proof[0][9:17]))

        self.wait()

        self.play(absurd_identity.animate.move_to([2.5, 0.75, 0]))

        self.wait()

        self.play(Write(rationality_proof[0][17:25]))

        self.wait()

        self.play(Write(rationality_proof[0][25:31]))

        self.wait()

        self.play(Write(rationality_proof[0][31:]))

        self.wait(1)

        absurd_identity2 = MathTex(r"\sqrt{2} = \frac{1}{1}", font_size=40, color=BLACK)

        self.play(ReplacementTransform(Group(rationality_proof, absurd_identity), absurd_identity2))

        # bring rational def back

        self.play(rational_def.animate.move_to([0, -1, 0]).scale(2))

        self.wait(1)

        self.play(rational_def[0][5:10].animate.set_color(GREEN_C))

        self.wait(1)

        self.play(rational_def[0][16:21].animate.set_color(GREEN_C))

        self.wait()

        self.play(rational_def[0][24:].animate.set_color(GREEN_C))

        self.wait()

        absurd_identity3 = MathTex(r"\sqrt{2} \in \mathbb{R}", font_size=60, color=BLACK)

        self.play(ReplacementTransform(Group(rational_def, absurd_identity2), absurd_identity3))

        self.wait()

        meme2 = ImageMobject("meme2.png", scale_to_resolution=1920)

        self.play(FadeIn(meme2))

        self.wait()