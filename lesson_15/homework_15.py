class Romb:
    def __init__(self, side_a, angle_a, ):
        self.angle_b = None
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("Має бути більше 0")
        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут А повинен бути в межах 0 < кут < 180")
            object.__setattr__(self, "angle_b", 180 - value)

        object.__setattr__(self, key, value)

    def __str__(self):
        return (f"Ромб: сторона a = {self.side_a}, "
                f"кут A = {self.angle_a}, "
                f"кут B = {self.angle_b}")


romb1 = Romb(10, 60)
print(romb1)

romb2 = Romb(5, 120)
print(romb2)