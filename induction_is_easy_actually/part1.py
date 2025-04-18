from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

config.pixel_height = 1080
config.pixel_width = 1920

class InductionVideo(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())

        ### --- TITLE --- ###
        intro_title = Text("Mathematical Induction", font_size=44, color=YELLOW)
        intro_title.to_edge(UP, buff=0.5)
        with self.voiceover(text="Have you heard of induction? Well now you have. It's a powerful mathematical proof structure, so powerful that it can be used to prove things that are counter-intuitive.") as tracker:
            self.play(Write(intro_title))

        ### --- SUM OF NATURAL NUMBERS VISUAL SETUP --- ###
        # Base Case
        base_eq = MathTex(r"1 = \frac{1(1+1)}{2}", font_size=40)
        base_eq.to_edge(LEFT, buff=1).shift(DOWN * 0.5)

        # Inductive Step
        inductive_step = MathTex(
            r"\text{assume } 1 + 2 + \cdots + k = \frac{k(k+1)}{2}",
            r"\implies 1 + 2 + \cdots + k + (k+1)", 
            r"= \frac{k(k+1)}{2} + (k+1)", 
            r"= \frac{(k+1)(k+2)}{2}",
            font_size=38
        ).arrange(DOWN, aligned_edge=LEFT).next_to(base_eq, RIGHT, buff=2).shift(UP * 0.5)

        with self.voiceover(text="The base case establishes one case where the result holds true.") as tracker:
            self.play(FadeIn(base_eq))


        with self.voiceover(text="The inductive step is a sort of bridge from one case to another.") as tracker:
            self.play(FadeIn(inductive_step))

        with self.voiceover(text="Combined, they're like a row of dominoes falling continuously, hitting every case.") as tracker:
            # Animate morphing series: 1 = ..., 1+2 = ..., 1+2+3 = ...
            series = [
                MathTex(r"1 = \frac{1(1+1)}{2}", font_size=36),
                MathTex(r"1+2 = \frac{2(2+1)}{2}", font_size=36),
                MathTex(r"1+2+3 = \frac{3(3+1)}{2}", font_size=36),
                MathTex(r"1+2+3+4 = \frac{4(4+1)}{2}", font_size=36),
            ]
            for i in range(len(series)):
                series[i].move_to(DOWN * 2.5)
            self.play(Write(series[0]))
            for i in range(1, len(series)):
                self.play(ReplacementTransform(series[i - 1], series[i]))
                self.wait(0.5)
            self.play(FadeOut(series[-1], intro_title, base_eq, inductive_step))

        ### --- EASY INDUCTION EXAMPLE --- ###
        example_title = Text("Induction Example: n³ + 2n divisible by 3 for n ≥ 1", font_size=36, color=YELLOW)
        example_title.to_edge(UP, buff=0.5)

        with self.voiceover(text="Let's look at a simpler example: prove that n cubed plus two n is divisible by three for all non-negative integers n.") as tracker:
            self.play(Write(example_title))

        base_case = MathTex(r"1^3 + 2 \cdot 1 = 3", font_size=36)
        base_case_result = MathTex(r"3 \div 3 = 1", font_size=36)
        base_group = VGroup(base_case, base_case_result).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        base_group.next_to(example_title, DOWN, buff=0.8)

        with self.voiceover(text="Start with the base case. If n equals one, then the expression is three, which is divisible by three.") as tracker:
            self.play(Write(base_group))
            self.wait()

        self.play(FadeOut(base_group))

        hypo = MathTex(
            r"\text{Assume } k^3 + 2k \text{ is divisible by } 3",
            font_size=36
        )
        hypo.next_to(example_title, DOWN, buff=0.8)

        with self.voiceover(text="Now assume it holds for some k.") as tracker:
            self.play(Write(hypo))
            self.wait()

        step_expr = MathTex(
            r"(k+1)^3 + 2(k+1)",
            r"= (k^3 + 3k^2 + 3k + 1) + (2k + 2)",
            r"= (k^3 + 2k) + 3k^2 + 3k + 3",
            r"= (k^3 + 2k) + 3(k^2 + k + 1)",
            font_size=34
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        step_expr.next_to(hypo, DOWN, buff=0.6)

        # Step 1
        with self.voiceover(text="Check the next case: k + 1. Start by expanding k plus 1 cubed and two times k plus 1.") as tracker:
            self.play(Write(step_expr[0]))
            self.play(Write(step_expr[1]))

        # Step 3
        with self.voiceover(text="We rearrange the terms by grouping k cubed and 2k together.") as tracker:
            self.play(Write(step_expr[2]))

        # Step 4
        with self.voiceover(text="Finally, factor 3 from the quadratic expression.") as tracker:
            self.play(Write(step_expr[3]))

        box = SurroundingRectangle(step_expr[3], color=GREEN)
        with self.voiceover(text="This expression is a sum of k cubed plus 2k, which is divisible by 3 due to our assumption, and a term that is also divisible by 3 due to its factor of 3.") as tracker:
            self.play(Create(box))
            self.wait()

        final_conclusion = Text("Therefore, n cubed plus two n is divisible by 3 for all n greater or equal to 1.", font_size=32, color=GREEN)
        final_conclusion.to_edge(DOWN, buff=0.5)

        with self.voiceover(text="This completes our induction, so we have shown that our expression, n cubed plus two n, is divisible by 3 for all positive integers n.") as tracker:
            self.play(Write(final_conclusion))
            self.wait()

        self.play(FadeOut(hypo, step_expr, box, example_title, final_conclusion))

        ### --- BEGIN FAKE HORSE PROOF --- ###
        title = Text("All Horses are the Same Color", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        with self.voiceover(text="Now let's use induction for something a little more questionable: a proof that all horses are the same color.") as tracker:
            self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        horse = ImageMobject("induction_is_easy_actually/horse.png")
        with self.voiceover(text="Also, because I'm lazy, just assume that all the squares on screen are horses.") as tracker:
            self.play(FadeIn(horse))
        self.wait()
        self.play(FadeOut(horse))

        # Base case
        base_case_label = Text("Base Case (n = 1)", font_size=30).to_edge(UP, buff=0.5)
        horse1 = Square(color=BLUE).scale(0.5)
        horse1_label = Text("Horse 1", font_size=24).next_to(horse1, DOWN, buff=0.2)
        group1 = VGroup(horse1, horse1_label).move_to(ORIGIN)
        with self.voiceover(text="For just one horse, all horses in the group clearly have the same color. This is our base case.") as tracker:
            self.play(Write(base_case_label))
            self.play(FadeIn(group1))
            self.play(horse1.animate.set_color(RED))
        self.wait()
        self.play(FadeOut(base_case_label), FadeOut(group1))

        # Inductive hypothesis
        hypothesis_label = Text("Inductive Hypothesis", font_size=30).to_edge(UP, buff=0.5)
        horses_n = VGroup(*[Square(color=BLUE).scale(0.5) for _ in range(3)])
        horses_n.arrange(RIGHT, buff=0.8)
        labels_n = VGroup(*[Text(f"H{i+1}", font_size=24).next_to(horses_n[i], DOWN, buff=0.2) for i in range(3)])
        group_n = VGroup(horses_n, labels_n).move_to(ORIGIN)
        with self.voiceover(text="Now, assume that any group of n horses will share the same color.") as tracker:
            self.play(Write(hypothesis_label))
            self.play(FadeIn(group_n))
            self.play(horses_n.animate.set_color(RED))
        self.wait()
        self.play(FadeOut(hypothesis_label), FadeOut(group_n))

        # Inductive step: n+1 horses
        step_label = Text("Inductive Step (assume works for n -> show works for n + 1)", font_size=30).to_edge(UP, buff=0.5)
        horses_n1 = VGroup(*[Square(color=BLUE).scale(0.5) for _ in range(4)])
        horses_n1.arrange(RIGHT, buff=0.8)
        labels_n1 = VGroup(*[Text(f"H{i+1}", font_size=24).next_to(horses_n1[i], DOWN, buff=0.2) for i in range(4)])
        group_n1 = VGroup(horses_n1, labels_n1).move_to(ORIGIN)
        with self.voiceover(text="We will use this to show that any group of n + 1 horses will all share the same color") as tracker:
            self.play(Write(step_label))
            self.play(FadeIn(group_n1))
        self.wait()

        # Draw borders instead of copying subsets
        # Get bounding rectangles for the subsets
        box_A = SurroundingRectangle(VGroup(*horses_n1[:3]), color=GREEN, buff=0.1)
        box_B = SurroundingRectangle(VGroup(*horses_n1[1:]), color=ORANGE, buff=0.1)

        label_A = Text("Subset A", font_size=24, color=GREEN).next_to(box_A, UP, buff=0.3)
        label_B = Text("Subset B", font_size=24, color=ORANGE).next_to(box_B, UP, buff=0.3)

        with self.voiceover(text="Take the first n horses as subset A.") as tracker:
            self.play(Create(box_A), Write(label_A))

        with self.voiceover(text="Now take the last n horses as subset B.") as tracker:
            self.play(Create(box_B), Write(label_B))

        # Highlight overlap
        with self.voiceover(text="These subsets overlap on some horses in the middle,") as tracker:
            self.play(horses_n1[1].animate.set_color(RED), horses_n1[2].animate.set_color(RED))
        self.wait(0.3)
        with self.voiceover(text="and since subset A, with n horses, has to all be the same color, and the same is true for subset B, the entire group needs to be of the same color."):
            self.play(horses_n1[0].animate.set_color(RED), horses_n1[3].animate.set_color(RED))

        with self.voiceover(text="Thus we have just proven that any group of horses will all be the same color."):
            self.play(FadeOut(step_label, box_A, label_A, box_B, label_B, group_n1))

        horse2 = ImageMobject("induction_is_easy_actually/horse2.jpg")

        with self.voiceover(text="Wait...(3s)...What?") as tracker:
            self.play(FadeIn(horse))
            self.wait()
            self.play(FadeIn(horse2))