from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

config.background_color = WHITE
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width = 1920
config.background_opacity = 1
config.max_files_cached = 200

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class Part1_with_voiceover(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())
        self.wait(1)

        tex = MathTex(r"\sqrt{2} \notin \mathbb{Q}", font_size=100, color=BLACK)
        with self.voiceover(text="So recently, I've been seeing a lot of “proofs” that the square root of two is irrational.") as tracker:
            self.play(Write(tex))
            
        other_radicals = MathTex(r"\sqrt{2}, \sqrt{3}, \sqrt{5}, \sqrt{7}, \cdots \notin \mathbb{Q}", font_size=100, color=BLACK)
        with self.voiceover(text="They also extend these proofs to square roots of other prime numbers.") as tracker:
            self.play(ReplacementTransform(tex, other_radicals))

        x_lines = Group(
            Line(other_radicals.get_critical_point(UL), other_radicals.get_critical_point(DR), color=RED), 
            Line(other_radicals.get_critical_point(UR), other_radicals.get_critical_point(DL), color=RED)
        )

        with self.voiceover(text="This really frustrated me because it is pretty obvious how the square root of two is rational.") as tracker:
            self.play(FadeIn(x_lines))


        with self.voiceover(text="Let me show you: To make things clearer, we set some ground definitions.") as tracker:
            self.play(AnimationGroup(FadeOut(other_radicals), FadeOut(x_lines)))

        rational_def = MathTex(r"x \in \mathbb{Q} \iff x = \frac{p}{q}, \text{where } p, q \in \mathbb{Z} \text{ and } \gcd(p, q) = 1", font_size=40, color=BLACK)
        with self.voiceover(text="The definition of a rational number is a number that can be written as, or in other words, is equivalent to, the quotient of two integers with no common factors.") as tracker:
            self.play(Write(rational_def))

        with self.voiceover(text="Lets save that for later.") as tracker:
            self.play(rational_def.animate.scale(0.5).to_corner(UL))

        pondering = MathTex(r"\sqrt{2} = \frac{p}{q}", font_size=40, color=BLACK)


        with self.voiceover(text="Now, all we have to do is show that the square root of two is equal to the quotient of two integers that don’t share any factors.") as tracker:
            self.play(Write(pondering))

        with self.voiceover(text="But before that, we need to quickly prove an identity.") as tracker:
            self.play(FadeOut(pondering))

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

        with self.voiceover(text="We start with one, which we know is equal to the square root of one.") as tracker:
            self.play(Write(absurd_proof1part1[0][:5]))

        with self.voiceover(text="We also know that this is equal to the square root of negative one times negative one, since negative one times negative one equals one.") as tracker:
            self.play(Write(absurd_proof1part1[0][5:17]))

        with self.voiceover(text="And since roots distribute over multiplication,") as tracker:
            self.play(Write(multiplicative_identity))

        with self.voiceover(text="this is equal to square root negative one times square root negative one."):
            self.play(Write(absurd_proof1part1[0][17:27]))

        with self.voiceover(text="We also know that the product of the square root of a number c with itself is c,"):
            self.play(Write(square_root_identity))

        with self.voiceover(text="so this is equal to negative one, and thus, one equals negative one."):
            self.play(Write(absurd_proof1part1[0][27:]))

        with self.voiceover(text="Moving on,"):
            self.play(ReplacementTransform(Group(absurd_proof1part1, multiplicative_identity, square_root_identity), absurd_proof1part2[0][:4]))        
            
        with self.voiceover(text="we can add one to both sides"):
            self.play(Write(absurd_proof1part2[0][4:7]))

        with self.voiceover(text="and divide by two to see that one equals zero."):
            self.play(Write(absurd_proof1part2[0][7:10]))
        
        self.play(FadeOut(absurd_proof1part2))

        meme1 = ImageMobject("meme1.png", scale_to_resolution=1920)
        with self.voiceover(text="If you don't believe me when I say one equals zero, I will show you another proof to hopefully convince you."):
            self.play(FadeIn(meme1))
        
        self.play(FadeOut(meme1))

        # absurd proof #2

        absurd_proof2 = MathTex(
            r"a, b \neq 0 \text{ and } a &= b \\ a^2 &= ab \\ a^2 - b^2 &= ab - b^2 \\ (a+b)(a-b) &= b(a-b) \\ a + b &= b \\ 2b &= b \\ 2 &= 1 \\ 1 &= 0", 
            font_size=40, 
            color=BLACK
        )

        
        with self.voiceover(text="We start by letting a and b, where a equals b and a and b are both not equal to zero."):
            self.play(Write(absurd_proof2[0][:12]))

        with self.voiceover(text="Then, we multiply both sides by a,"):
            self.play(Write(absurd_proof2[0][12:17]))

        with self.voiceover(text="and subtract both sides by b squared."):
            self.play(Write(absurd_proof2[0][17:28]))

        with self.voiceover(text="We can then factor."):
            self.play(Write(absurd_proof2[0][28:45]))

        # if you don't believe that this is true, just ...
            
        explaination1 = MathTex(r"(a+b)(a-b)", font_size=40, color=BLACK).move_to([-4.5, 0, 0])
        
        with self.voiceover(text="To see why the left sides are equal, you can try multipling a plus b and a minus b by distributing: "):
            self.play(Write(explaination1))

        explaination2 = MathTex(r"a^2 + a \cdot b - a \cdot b - b^2", font_size=40, color=BLACK).move_to([-4.5, 0, 0])
        self.play(ReplacementTransform(explaination1, explaination2))

        explaination3 = MathTex(r"a^2 - b^2", font_size=40, color=BLACK).move_to([-4.5, 0, 0])
        with self.voiceover(text="Since ab and negative ab cancel, we are left with a squared minus b squared. This is a famous identity called 'difference of squares'"):
            self.play(ReplacementTransform(explaination2, explaination3))

        self.play(FadeOut(explaination3))

        with self.voiceover(text="Then, we can cancel out the a minus bs on both sides"):
            self.play(Write(absurd_proof2[0][45:50]))

        with self.voiceover(text="And substitute the a for a b since we know that a equals b"):
            self.play(Write(absurd_proof2[0][50:54]))

        with self.voiceover(text="Knowing that b is nonzero (we defined it this way), we can divide by b and get two equals one."):
            self.play(Write(absurd_proof2[0][54:57]))

        with self.voiceover(text="Finally, we subtract by one on both sides to arrive at one equals zero."):
            self.play(Write(absurd_proof2[0][57:60]))

        absurd_identity = MathTex(r"1 = 0", font_size=40, color=BLACK)

        with self.voiceover(text="We will also save this for later."):
            self.play(ReplacementTransform(absurd_proof2, absurd_identity))
            self.play(absurd_identity.animate.to_corner(UR))

        rationality_proof = MathTex(
            r"\sqrt{2} &= \frac{\sqrt{2}}{1} \\ &= \frac{\sqrt{1 + 1}}{1} \\ &= \frac{\sqrt{1 + 0}}{1} \\ &= \frac{\sqrt{1}}{1} \\ &= \frac{1}{1}", 
            font_size=40, 
            color=BLACK
        )

        with self.voiceover(text="Now for the actual proof. <bookmark mark='A'/> We first observe that square root two is equal to square root two over one,"):
            self.wait_until_bookmark("A")
            self.play(Write(rationality_proof[0][:9]))

        with self.voiceover(text="which is equal to square root of one plus one all over one."):
            self.play(Write(rationality_proof[0][9:17]))

        
        with self.voiceover(text="This is where the our identity comes in."):
            self.play(absurd_identity.animate.move_to([2.5, 0.75, 0])) 


        with self.voiceover(text="Since we know that one equals zero, we can substitute and see that this is equal to square root one plus zero all over one."):
            self.play(Write(rationality_proof[0][17:25]))

        with self.voiceover(text="This is equal to square root one over one,"):
            self.play(Write(rationality_proof[0][25:31]))

        with self.voiceover(text="Which, is ultimately equal to one over one."):
            self.play(Write(rationality_proof[0][31:]))

        absurd_identity2 = MathTex(r"\sqrt{2} = \frac{1}{1}", font_size=40, color=BLACK)

        self.play(ReplacementTransform(Group(rationality_proof, absurd_identity), absurd_identity2))

        # bring rational def back
        with self.voiceover(text="Bringing back our earlier definition of rationality, "):
            self.play(rational_def.animate.move_to([0, -1, 0]).scale(2))

        with self.voiceover(text="We can see that our first condition is met, since square root two is equal to a fraction between two values."):
            self.play(rational_def[0][5:10].animate.set_color(GREEN_C))

        with self.voiceover(text="Additionally, those two values are integers,"):
            self.play(rational_def[0][16:21].animate.set_color(GREEN_C))    

        with self.voiceover(text="And lastly, those two values have no common factors other one, so in other words, their greaters common divisor is one."):
            self.play(rational_def[0][24:].animate.set_color(GREEN_C))

        absurd_identity3 = MathTex(r"\sqrt{2} \in \mathbb{Q}", font_size=60, color=BLACK)
        with self.voiceover(text="Thus, square root two is rational."):
            self.play(ReplacementTransform(Group(rational_def, absurd_identity2), absurd_identity3))


        meme2 = ImageMobject("meme2.png", scale_to_resolution=1920)
        with self.voiceover(text="If your friends tell you that sqrt(2) is irrational, you should probably get new friends. A responsible adult says no to mathematical propaganda."):
            self.play(FadeIn(meme2))