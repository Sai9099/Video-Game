class Sprite:
    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter

    def display_info(self):
        print(f"Position: ({self.x}, {self.y})")
        print(f"Image File: {self.img_file}")
        print(f"Speed: {self.speed}")
        print(f"Life Counter: {self.life_counter}")


class Enemy(Sprite):
    def __init__(self, x, y, img_file, speed):
        super().__init__(x, y, img_file, speed, 5)
        self.message = "I'm here to protect my master"

    def display_info(self):
        super().display_info()
        print(f"Message: {self.message}")


class Player(Enemy):
    def __init__(self, x, y, img_file, speed):
        super().__init__(x, y, img_file, speed)
        self.speed = 56  # Override the speed

    def display_info(self):
        super().display_info()
        print("This is the Player.")


class DifficultEnemy(Enemy):
    def __init__(self, x, y, img_file):
        super().__init__(x, y, img_file, 80)

    def display_info(self):
        super().display_info()
        print("This is a Difficult Enemy.")


class EasyEnemy(Enemy):
    def __init__(self, x, y, img_file):
        super().__init__(x, y, img_file, 40)
        self.life_counter = 1  # Override life counter

    def display_info(self):
        super().display_info()
        print("This is an Easy Enemy.")


# Example usage
if __name__ == "__main__":
    print("=== Sprite ===")
    sprite = Sprite(0, 0, "sprite.png", 10, 3)
    sprite.display_info()

    print("\n=== Enemy ===")
    enemy = Enemy(5, 5, "enemy.png", 20)
    enemy.display_info()

    print("\n=== Player ===")
    player = Player(10, 10, "player.png", 30)
    player.display_info()

    print("\n=== DifficultEnemy ===")
    difficult_enemy = DifficultEnemy(15, 15, "difficult_enemy.png")
    difficult_enemy.display_info()

    print("\n=== EasyEnemy ===")
    easy_enemy = EasyEnemy(20, 20, "easy_enemy.png")
    easy_enemy.display_info()
