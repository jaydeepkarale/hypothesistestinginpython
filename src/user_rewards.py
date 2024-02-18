class UserRewards:
    def __init__(self, initial_points):
        self.reward_points = initial_points

    def get_reward_points(self):
        return self.reward_points

    def spend_reward_points(self, amount):
        if amount <= self.reward_points:
            self.reward_points -= amount
            return True
        else:
            return False