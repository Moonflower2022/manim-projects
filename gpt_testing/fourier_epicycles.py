from manim import *
import numpy as np

class FourierEpicycleScene(Scene):
    def construct(self):
        # Title
        title = Text("Fourier Epicycles Drawing a Goofy Smiley", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Narration text
        narration = Paragraph(
            "Each rotating circle (epicycle) represents a frequency component.",
            "Together, they recreate a goofy smiley face!",
            font_size=24, alignment="left", line_spacing=0.8
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(narration))

        # Simulated complex path (a goofy smiley face made from hand-picked points)
        # You can replace this with a real Fourier path if you import from SVG etc.
        points = [
            # Face outline
            *[0.7 * np.exp(2j * np.pi * t / 100) for t in range(100)],
            # Left eye
            *[0.1 * np.exp(2j * np.pi * t / 30) + 0.25 + 0.2j for t in range(30)],
            # Right eye
            *[0.1 * np.exp(2j * np.pi * t / 30) - 0.25 + 0.2j for t in range(30)],
            # Smiley mouth
            *[0.4 * np.exp(1j * np.pi * t / 50) - 0.0 - 0.3j for t in range(51)]
        ]

        N = len(points)
        # Discrete Fourier Transform
        def dft(x):
            N = len(x)
            X = []
            for k in range(N):
                re = 0
                im = 0
                for n in range(N):
                    angle = 2 * np.pi * k * n / N
                    re += x[n] * np.cos(-angle)
                    im += x[n] * np.sin(-angle)
                X.append(re + 1j * im)
            return X

        X = dft(points)
        freqs = list(range(-N//2, N//2))
        X = np.fft.fftshift(X)
        epicycles = sorted(
            [(freqs[i], X[i]/N) for i in range(N)],
            key=lambda x: abs(x[1]),
            reverse=True
        )

        origin = ORIGIN
        path = VMobject(color=WHITE)
        path.set_points_as_corners([origin])

        # Group for drawing all epicycles and vectors
        epicycle_group = VGroup()

        # Update function
        def get_epicycle_path(t):
            vectors = []
            prev_point = origin
            for freq, coeff in epicycles[:100]:  # Limit to top 100 components
                angle = 2 * np.pi * freq * t
                vec = coeff * np.exp(1j * angle)
                end_point = prev_point + complex_to_vector(vec)
                circle = Circle(radius=abs(vec), color=BLUE_D, stroke_opacity=0.3)
                circle.move_to(prev_point)
                line = Line(prev_point, end_point, color=BLUE)
                vectors.append(circle)
                vectors.append(line)
                prev_point = end_point
            return prev_point, VGroup(*vectors)

        # Convert complex number to 2D vector
        def complex_to_vector(z):
            return np.array([z.real, z.imag, 0])

        drawn_path = VMobject(color=YELLOW)
        drawn_path.set_points_as_corners([origin])

        # Animation
        path_points = []
        def update_drawn_path(mob, dt):
            t = update_drawn_path.t
            t += dt / 6  # control drawing speed
            if t > 1:
                return
            point, new_group = get_epicycle_path(t)
            path_points.append(point)
            mob.set_points_as_corners(path_points)
            update_drawn_path.t = t

            # Update epicycles
            epicycle_group.become(new_group)

        update_drawn_path.t = 0
        self.add(drawn_path, epicycle_group)
        self.add(path)

        drawn_path.add_updater(update_drawn_path)
        self.wait(12)
        drawn_path.remove_updater(update_drawn_path)

        # Fade out everything
        self.play(FadeOut(drawn_path), FadeOut(epicycle_group), FadeOut(narration), FadeOut(title))

        # Ending message
        end_text = Text("Fourier magic complete!", font_size=36, color=GREEN).to_edge(UP, buff=0.5)
        self.play(Write(end_text))
        self.wait(2)