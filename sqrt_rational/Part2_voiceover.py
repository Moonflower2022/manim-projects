from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

config.background_color = BLACK
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width = 1920
config.background_opacity = 1

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class Part2_voiceover(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            RecorderService()
        )

        one_neq_zero = MathTex(
            r"1 \neq 0",
            color=WHITE,
            font_size=40
        )

        with self.voiceover(text="Just kidding, one is not equal to zero. <bookmark mark='A'/> Here is where my two proofs make a mistake:") as tracker:
            self.play(FadeIn(one_neq_zero))
            self.wait_until_bookmark('A')
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
            r"\sqrt{2} \in \mathbb{Q} \Longrightarrow A \text{ and } B?? \Longrightarrow \sqrt{2} \notin \mathbb{Q}",
            color=WHITE,
            font_size=40
        )

        with self.voiceover(
            text="""in fact, the square root of 2 is irrational, and there 
            is a very common proof that exemplifies this. It is in the format 
            of a proof by contradiction, <bookmark mark='A'/> where we start by assuming something 
            about sqrt(2) <bookmark mark='B'/> and arriving to a contradiction 
            (in this case, the fact that A and B are both true, something that is impossible) 
            <bookmark mark='C'/> that shows our original assumption must be incorrect"""
        ) as tracker:
            self.wait_until_bookmark("A")
            self.play(Write(contradiction_demo[0][:5]))
            self.wait_until_bookmark("B")
            self.play(Write(contradiction_demo[0][5:14]))
            self.wait_until_bookmark("C")
            self.play(Write(contradiction_demo[0][14:]))            
    
        self.play(FadeOut(contradiction_demo))
        
        assumption = Text("Assumption:", font_size=40, color=WHITE)

        assumption_latex = MathTex(r"\sqrt{2} \in \mathbb{Q}", font_size=40, color=WHITE).move_to([0, -1, 0])

        with self.voiceover(text="Our starting assumption is that <bookmark mark='A'/> square root two is rational.") as tracker:
            self.play(FadeIn(assumption))
            self.wait_until_bookmark("A")
            self.play(FadeIn(assumption_latex))

        rational_def = MathTex(r"\sqrt{2} = \frac{p}{q}, \text{where } p, q \in \mathbb{Z}, \gcd(p, q) = 1, \text{and } q > 0", font_size=40, color=WHITE)
        with self.voiceover(
            text="""According to our rationality definition, this means 
            that sqrt(2) is equivalent to the quotient of two integers 
            that don't share any common factors (their greatest 
            common divisor is one)"""
        ) as tracker:
            self.play(ReplacementTransform(Group(assumption, assumption_latex), rational_def))

        self.play(rational_def.animate.scale(0.5).to_corner(UL))

        irrationality_proof = MathTex(
            r"\sqrt{2} &= \frac{p}{q} \\ q\sqrt{2} &= p \\ 2q^2 &= p^2 \\ 2q^2 &= (2n)^2 \\ 2q^2 &= 4n^2 \\ q^2 &= 2n^2", 
            font_size=40, 
            color=WHITE
        ).move_to([-2, 0, 0])

        with self.voiceover(
            text="""Lets start from the condition that square root two 
            has to be equal to the quotient of two integers, 
            and lets call them p and q."""
        ) as tracker:
            self.play(Write(irrationality_proof[0][:7]))

        with self.voiceover(text="Multiplying both sides by q, we get q sqrt two = p") as tracker:
            self.play(Write(irrationality_proof[0][7:13]))

        with self.voiceover(text="squaring both sides, we see that 2q^2 = p^2.") as tracker:
            self.play(Write(irrationality_proof[0][13:19]))

        with self.voiceover(
            text="""From here, we observe that p^2 is an integer 
            because p is an integer and it being represented as 
            the product of <bookmark mark='A'/> two and q^2, which is an integer becuase q is an integer. 
            This means that p^2 is even."""
        ) as tracker:
            self.wait_until_bookmark("A")
            self.play(irrationality_proof[0][13:14].animate.set_color(YELLOW))
            self.play(irrationality_proof[0][13:14].animate.set_color(WHITE))

        odd_int_explaination = MathTex(r"(2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1", color=YELLOW_A, font_size=40).move_to([3, 2.5, 0])
        even_int_explaination = MathTex(r"(2k)^2 = 4k^2 = 2(2k^2)", color=YELLOW_A, font_size=40).move_to([3.5, 1.5, 0])

        p_even = MathTex(r"p = 2n, n \in \mathbb{Z}", color=WHITE, font_size=40).move_to([0.7, 0.13, 0])

        with self.voiceover(text="Since an odd integer squared is odd, ") as tracker:
            self.play(Write(odd_int_explaination))

        with self.voiceover(text="and an even integer squared is even, ") as tracker:
            self.play(Write(even_int_explaination))

        with self.voiceover(text="the only way that p^2 can be even is if p is even. <bookmark mark='A'/> This means that p can be represented as two times some integer, which we can call n.") as tracker:
            self.wait_until_bookmark("A")
            self.play(Write(p_even))

        with self.voiceover(text="Knowing this, we can substitute,") as tracker:
            self.play(Write(irrationality_proof[0][19:28]))        

        # simplify

        with self.voiceover(text="and simplify.") as tracker:
            self.play(Write(irrationality_proof[0][28:35]))
            self.wait(0.5)
            self.play(Write(irrationality_proof[0][35:]))

        # observe that q^2 is even

        q_even = MathTex(r"q = 2m, m \in \mathbb{Z}", color=WHITE, font_size=40).move_to([0.7, -1.9, 0])

        with self.voiceover(
            text="""By the same logic as used before, <bookmark mark='A'/> 
            we see that q is even which means that q has a factor of 2."""
        ) as tracker:
            self.wait_until_bookmark('A')
            self.play(Write(q_even))
        
        with self.voiceover(
            text="""This means we have a contradiciton! <bookmark mark='A'/> 
            We have shown that p and q have a common factor: 2, since they are 
            both even integers. <bookmark mark='B'/> However, our assumption was that p and q don't 
            share any common factors."""
        ) as tracker:
            self.wait_until_bookmark('A')
            self.play(FadeOut(Group(irrationality_proof, odd_int_explaination, even_int_explaination)))
            self.play(AnimationGroup(q_even.animate.move_to([1.5, 0, 0]), p_even.animate.move_to([-1.5, 0, 0])))
            self.wait_until_bookmark('B')
            self.play(rational_def.animate.move_to([0, -1, 0]).scale(2))

        result = MathTex(r"\sqrt{2} \notin \mathbb{Q}", color=WHITE, font_size=40)

        with self.voiceover(text="Thus, we arrive at a contradiction, <bookmark mark='A'/> so we have proved our result.") as tracker:
            self.wait_until_bookmark('A')
            self.play(ReplacementTransform(Group(rational_def, q_even, p_even), result))

        self.wait(1)
        
        self.play(FadeOut(result))
