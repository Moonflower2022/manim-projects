from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class AllHorsesSameColorFakeProof(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())

        # Title
        title = Text("Fake Proof: All Horses are the Same Color", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        with self.voiceover(text="Let's look at a classic fake proof that claims all horses are the same color.") as tracker:
            self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        # Base case: n = 1
        base_case_label = Text("Base Case (n = 1)", font_size=30).to_edge(UP, buff=0.5)
        horse1 = Square(color=BLUE).scale(0.5)
        horse1_label = Text("Horse 1", font_size=24).next_to(horse1, DOWN, buff=0.2)
        group1 = VGroup(horse1, horse1_label).move_to(ORIGIN)
        with self.voiceover(text="For just one horse, all horses in the group clearly have the same color.") as tracker:
            self.play(Write(base_case_label))
            self.play(FadeIn(group1))
        self.wait()
        self.play(FadeOut(base_case_label), FadeOut(group1))

        # Inductive hypothesis: assume for n horses
        hypothesis_label = Text("Inductive Hypothesis", font_size=30).to_edge(UP, buff=0.5)
        horses_n = VGroup(*[Square(color=BLUE).scale(0.5) for _ in range(3)])
        horses_n.arrange(RIGHT, buff=0.8)
        labels_n = VGroup(*[Text(f"H{i+1}", font_size=24).next_to(horses_n[i], DOWN, buff=0.2) for i in range(3)])
        group_n = VGroup(horses_n, labels_n).move_to(ORIGIN)
        with self.voiceover(text="Now, assume that in any group of n horses, they all share the same color.") as tracker:
            self.play(Write(hypothesis_label))
            self.play(FadeIn(group_n))
        self.wait()
        self.play(FadeOut(hypothesis_label), FadeOut(group_n))

        # Inductive step: n+1 horses
        step_label = Text("Inductive Step (n + 1 horses)", font_size=30).to_edge(UP, buff=0.5)
        horses_n1 = VGroup(*[Square(color=BLUE).scale(0.5) for _ in range(4)])
        horses_n1.arrange(RIGHT, buff=0.8)
        labels_n1 = VGroup(*[Text(f"H{i+1}", font_size=24).next_to(horses_n1[i], DOWN, buff=0.2) for i in range(4)])
        group_n1 = VGroup(horses_n1, labels_n1).move_to(ORIGIN)
        with self.voiceover(text="Let's try to prove the case for n plus one horses.") as tracker:
            self.play(Write(step_label))
            self.play(FadeIn(group_n1))
        self.wait()

        # Subset A: first 3 horses
        subset_A = horses_n1[:3].copy().arrange(RIGHT, buff=0.8).shift(UP*1.5)
        label_A = Text("Subset A", font_size=24).next_to(subset_A, UP)
        with self.voiceover(text="Take the first n horses as subset A.") as tracker:
            self.play(FadeIn(subset_A), Write(label_A))

        # Subset B: last 3 horses
        subset_B = horses_n1[1:].copy().arrange(RIGHT, buff=0.8).shift(DOWN*1.5)
        label_B = Text("Subset B", font_size=24).next_to(subset_B, DOWN)
        with self.voiceover(text="Now take the last n horses as subset B.") as tracker:
            self.play(FadeIn(subset_B), Write(label_B))

        # Highlight overlap
        with self.voiceover(text="These subsets overlap on some horses, so it seems all horses must be the same color.") as tracker:
            self.play(horses_n1[1].animate.set_color(RED), horses_n1[2].animate.set_color(RED))
        self.wait()

        # Remove everything
        with self.voiceover(text="But here's the problem.") as tracker:
            self.play(FadeOut(step_label, group_n1, subset_A, label_A, subset_B, label_B))

        # Show flaw
        flaw = Text("Fails at n = 1", font_size=32, color=RED).to_edge(UP)
        with self.voiceover(text="The overlap trick doesn't work when n equals one. There's no shared horse.") as tracker:
            self.play(Write(flaw))
        self.wait()

        outro = Text("This is a fake proof — a flaw in the logic of induction.", font_size=28, color=YELLOW).to_edge(DOWN)
        with self.voiceover(text="This is a fake proof — a flaw in the logic of induction.") as tracker:
            self.play(Write(outro))
        self.wait(3)
        self.play(FadeOut(flaw, outro))