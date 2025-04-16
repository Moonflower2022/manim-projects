from manim import *

class AllHorsesSameColorFakeProof(Scene):
    def construct(self):
        # Title
        title = Text("Fake Proof: All Horses are the Same Color", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Narration 1
        narration1 = Paragraph(
            "We will \"prove\" that all horses are the same color using mathematical induction.",
            font_size=24,
            alignment="LEFT",
            line_spacing=0.8
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(narration1))
        self.wait(3)
        self.play(FadeOut(narration1))

        # Step 1: Base Case
        base_case_text = Text("Base Case: A group with 1 horse", font_size=30).to_edge(UP, buff=1.2)
        horse1 = Square(color=BLUE).scale(0.5)
        horse1_label = Text("Horse 1", font_size=24).next_to(horse1, DOWN, buff=0.2)
        base_group = VGroup(horse1, horse1_label).move_to(ORIGIN)

        narration2 = Paragraph(
            "In a group of 1 horse, all horses clearly have the same color.",
            font_size=24,
            alignment="LEFT"
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(base_case_text))
        self.play(Create(horse1), Write(horse1_label))
        self.play(Write(narration2))
        self.wait(3)
        self.play(FadeOut(base_case_text), FadeOut(base_group), FadeOut(narration2))

        # Step 2: Inductive Hypothesis
        hypothesis_text = Text("Inductive Hypothesis: Assume true for n horses", font_size=30).to_edge(UP, buff=1.2)

        horses_n = VGroup(*[
            Square(color=BLUE).scale(0.5) for _ in range(3)
        ])
        horses_n.arrange(RIGHT, buff=0.8)
        horse_labels = VGroup(*[
            Text(f"H{i+1}", font_size=24).next_to(horses_n[i], DOWN, buff=0.2) for i in range(3)
        ])
        group_n = VGroup(horses_n, horse_labels).move_to(ORIGIN)

        narration3 = Paragraph(
            "Assume that in any group of n horses, all horses have the same color.",
            font_size=24,
            alignment="LEFT"
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(hypothesis_text))
        self.play(Create(horses_n), Write(horse_labels))
        self.play(Write(narration3))
        self.wait(3)
        self.play(FadeOut(hypothesis_text), FadeOut(group_n), FadeOut(narration3))

        # Step 3: Inductive Step
        inductive_step_text = Text("Inductive Step: Prove for n + 1 horses", font_size=30).to_edge(UP, buff=1.2)

        horses_n1 = VGroup(*[
            Square(color=BLUE).scale(0.5) for _ in range(4)
        ])
        horses_n1.arrange(RIGHT, buff=0.8)
        horse_n1_labels = VGroup(*[
            Text(f"H{i+1}", font_size=24).next_to(horses_n1[i], DOWN, buff=0.2) for i in range(4)
        ])
        group_n1 = VGroup(horses_n1, horse_n1_labels).move_to(ORIGIN)

        narration4 = Paragraph(
            "Consider a group of n + 1 horses. Remove the last horse...",
            font_size=24,
            alignment="LEFT"
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(inductive_step_text))
        self.play(Create(horses_n1), Write(horse_n1_labels))
        self.play(Write(narration4))
        self.wait(3)

        # Show subset without last horse
        subset1 = horses_n1[:3].copy()
        subset1_group = VGroup(*subset1).arrange(RIGHT, buff=0.8).shift(UP*1.5)
        label1 = Text("Subset A", font_size=24).next_to(subset1_group, UP)

        self.play(FadeIn(subset1_group), Write(label1))
        self.wait(2)

        narration5 = Paragraph(
            "Now remove the first horse. The remaining n horses also have the same color.",
            font_size=24,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeOut(narration4), Write(narration5))

        subset2 = horses_n1[1:].copy()
        subset2_group = VGroup(*subset2).arrange(RIGHT, buff=0.8).shift(DOWN*1.5)
        label2 = Text("Subset B", font_size=24).next_to(subset2_group, DOWN)

        self.play(FadeIn(subset2_group), Write(label2))
        self.wait(2)

        # Highlight the overlap (H2 and H3)
        overlap = VGroup(horses_n1[1], horses_n1[2]).copy()
        self.play(overlap.animate.set_color(RED))

        narration6 = Paragraph(
            "Since the two subsets overlap, all horses must have the same color... right?",
            font_size=24
        ).to_edge(DOWN, buff=0.5)

        self.play(FadeOut(narration5), Write(narration6))
        self.wait(3)

        # Flawed logic reveal
        flaw_text = Text("But wait... It fails for n = 1!", font_size=32, color=RED)
        flaw_text.to_edge(DOWN, buff=1.5)

        self.play(FadeOut(group_n1), FadeOut(subset1_group), FadeOut(subset2_group),
                  FadeOut(label1), FadeOut(label2), FadeOut(narration6))
        self.play(Write(flaw_text))

        final_narration = Paragraph(
            "In the base case, the subsets do not overlap. So the proof breaks at n = 1.",
            font_size=24
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(final_narration))
        self.wait(3)

        outro = Text("This is a classic example of a *fake proof* using faulty induction.", font_size=30, color=YELLOW)
        outro.to_edge(DOWN)
        self.play(FadeOut(flaw_text, final_narration))
        self.play(Write(outro))
        self.wait(3)

        # End
        self.play(FadeOut(outro, title))