from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

config.background_color = BLACK
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width = 1920
config.background_opacity = 1


class Part2_with_voiceover(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            RecorderService()
        )

        one_neq_zero = MathTex(
            r"1 \neq 0",
            color=WHITE,
            font_size=40
        )

        with self.voiceover(text="Just kidding, one is not equal to zero. Here is where my two proofs make a mistake:") as tracker:
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

        
        with self.voiceover(text="in the first part of the first proof,") as tracker:
            self.play(FadeIn(Group(absurd_proof1part1, multiplicative_identity, square_root_identity)))

        with self.voiceover(text="everything up to the second step is correct.") as tracker:
            self.play(absurd_proof1part1[0][5:17].animate.set_color(PURE_GREEN))

        with self.voiceover(
            text="""Hovever, the distribution of roots over multiplication 
            only holds if both values are not negative, <bookmark mark='A'/>
            so the next step is where the proof falls apart."""
        ) as tracker:
            self.wait_until_bookmark("A")
            self.play(absurd_proof1part1[0][17:27].animate.set_color(PURE_RED))

        self.play(FadeOut(Group(absurd_proof1part1, multiplicative_identity, square_root_identity)))

        # absurd proof #2

        absurd_proof2 = MathTex(
            r"a, b \neq 0 \text{ and } a &= b \\ a^2 &= ab \\ a^2 - b^2 &= ab - b^2 \\ (a+b)(a-b) &= b(a-b) \\ a + b &= b \\ 2a &= a \\ 2 &= 1 \\ 1 &= 0", 
            font_size=40, 
            color=WHITE
        )

        with self.voiceover(text="In the second proof, <bookmark mark='A'/> from the fourth step to the fifth, we divide by a - b, which unfortunately is zero, since a = b.") as tracker:
            self.play(FadeIn(absurd_proof2))
            self.wait_until_bookmark("A")
            self.play(absurd_proof2[0][28:45].animate.set_color(PURE_GREEN))
            self.play(absurd_proof2[0][45:50].animate.set_color(PURE_RED))

        self.play(FadeOut(absurd_proof2))

        contradiction_demo = MathTex(
            r"\sqrt{2} \in \mathbb{R} \Longrightarrow \gcd(p, q) = 1 \text{ and } \gcd(p, q) = 2?? \Longrightarrow \sqrt{2} \notin \mathbb{R}",
            color="WHITE",
            font_size=40
        )
        

        self.wait()

        with self.voiceover(
            text="""in fact, the square root of 2 is irrational, and there 
            is a very common proof that exemplifies this. <bookmark mark='A'/> It is in the format 
            of a proof by contradiction, where we start by assuming something 
            about sqrt(2) <bookmark mark='B'/> and arriving to a contradiction 
            <bookmark mark='B'/> that shows our original assumption has to be incorrect"""
        ) as tracker:
            self.wait_until_bookmark("A")
            self.play(Write(contradiction_demo[0][:5]))
            self.wait_until_bookmark("B")
            self.play(Write(contradiction_demo[0][5:32]))
            self.wait_until_bookmark("C")
            self.play(Write(contradiction_demo[0][32:]))
    
        self.play(FadeOut(contradiction_demo))

        n = MathTex(r"n", color=WHITE, font_size=40)

        odd_int_explaination = MathTex(r"(2n + 1)^2 = 4n^2 + 4n + 1 = 2(2n^2 + 2n) + 1", color=WHITE, font_size=40)
        int_brace1 = Brace(odd_int_explaination[0][2:3])
        int_brace2 = Brace(odd_int_explaination[0][18:26])
        odd_int_brace1 = Brace(odd_int_explaination[0][:6])
        odd_int_brace2 = Brace(odd_int_explaination[0][15:])
        
        even_int_explaination = MathTex(r"(2n)^2 = 4n^2 = 2(2n^2)", color=WHITE, font_size=40)
        int_brace3 = Brace(even_int_explaination[0][2:3])
        int_brace4 = Brace(even_int_explaination[0][9:])
        even_int_brace1 = Brace(even_int_explaination[0][:4])
        env_int_brace2 = Brace(even_int_explaination[0][10:])

        with self.voiceover(
            text="""But, before we do that, we need to quickly notice some things about integers. <bookmark mark='A'/>
            Given a generic integer n, we can see that 2n is the generic form for even integers 
            and 2n + 1 is the generic form for odd integers. This means that any integer that 
            is represented as 2 times another integer is automatically even, and any integer that 
            is represented as 2 times another integer plus one is automatically odd. """
        ) as tracker:
            self.wait_until_bookmark('A')
            
        
        assumption = Text("Assumption:", font_size=40, color=WHITE)

        assumption_latex = MathTex(r"\sqrt{2} \in \mathbb{R}", font_size=40, color=WHITE).move_to([0, -1, 0])

        with self.voiceover(text="Our starting assumption is that <bookmark mark='A'/> square root two is rational.") as tracker:
            self.wait_until_bookmark("A")
            self.play(FadeIn(Group(assumption, assumption_latex)))

        rational_def = MathTex(r"\sqrt{2} = \frac{p}{q}, \text{where } p, q \in \mathbb{Z}, \gcd(p, q) = 1, \text{and } q > 0", font_size=40, color=WHITE)
        with self.voiceover(text="According to our rationality definition, this means that sqrt(2) is equivalent to the quotient of two integers that don't share any common factors (their greatest common divisor is one)") as tracker:
            self.play(ReplacementTransform(Group(assumption, assumption_latex), rational_def))

        self.play(rational_def.animate.scale(0.5).to_corner(UL))

        irrationality_proof = MathTex(
            r"\sqrt{2} &= \frac{p}{q} \\ q\sqrt{2} &= p \\ 2q^2 &= p^2 \\ 2q^2 &= (2k)^2 \\ 2q^2 &= 4k^2 \\ q^2 &= 2k^2", 
            font_size=40, 
            color=WHITE
        )

        with self.voiceover(text="Lets start from the condition that square root two has to be equal to the quotient of two integers, and lets call them p and q.") as tracker:
            self.play(Write(irrationality_proof[0][:7]))

        with self.voiceover(text="Multiplying both sides by q, we get q sqrt two = p") as tracker:
            self.play(Write(irrationality_proof[0][7:13]))

        with self.voiceover(text="squaring both sides, we see that 2q^2 = p^2") as tracker:
            self.play(Write(irrationality_proof[0][13:19]))

        with self.voiceover(
            text="""From here, we observe that p^2 is an integer 
            because p is an integer and it being represented as 
            the product of <bookmark mark='A'/>two and q^2, which is an integer becuase q is an integer. 
            This means that p^2 is even."""
        ) as tracker:
            self.wait_until_bookmark("A")
            self.play(irrationality_proof[0][13:14].animate.set_color(YELLOW))
            self.play(irrationality_proof[0][13:14].animate.set_color(WHITE))

        with self.voiceover(text="Since an odd integer squared is odd, ") as tracker:
            self.play(Write(odd_int_explaination))
            self.play(FadeIn(Grou))

        with self.voiceover(text="and an even integer squared is even, ") as tracker:

        with self.voiceover(text="this implies that p is even.") as tracker:



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

