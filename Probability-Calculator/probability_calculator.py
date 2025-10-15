import copy
import random


class Hat:
    def __init__(self, **kwargs):
        # kwargs holds the ball colors and their counts
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If draw more than available, return all
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn

        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Copy hat so each experiment is independent
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count drawn balls
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # Check if all expected balls are satisfied
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments


# Example usage
if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(
        hat=hat,
        expected_balls={'red': 2, 'green': 1},
        num_balls_drawn=5,
        num_experiments=2000
    )
    print("Estimated Probability:", probability)