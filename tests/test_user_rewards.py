from hypothesis import given, strategies as st
from src.user_rewards import UserRewards

# Define a strategy for generating user rewards data
reward_points_strategy = st.integers(min_value=0, max_value=1000)  # Assuming users have between 0 and 1000 reward points

# Use Hypothesis to generate test cases for checking reward points
@given(initial_points=reward_points_strategy)
def test_get_reward_points(initial_points):
    user_rewards = UserRewards(initial_points)
    assert user_rewards.get_reward_points() == initial_points

# Use Hypothesis to generate test cases for spending reward points
@given(initial_points=reward_points_strategy, spend_amount=st.integers(min_value=0, max_value=1000))
def test_spend_reward_points(initial_points, spend_amount):
    user_rewards = UserRewards(initial_points)
    remaining_points = user_rewards.get_reward_points()

    if spend_amount <= initial_points:
        assert user_rewards.spend_reward_points(spend_amount)
        remaining_points -= spend_amount
    else:
        assert not user_rewards.spend_reward_points(spend_amount)

    assert user_rewards.get_reward_points() == remaining_points
