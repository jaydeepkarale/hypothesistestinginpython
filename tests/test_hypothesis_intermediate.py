from hypothesis import given, strategies as st
from datetime import datetime, timedelta

# Function to generate an alert for expiry date within 45 days
def generate_expiry_alert(expiry_date):
    current_date = datetime.now().date()
    days_until_expiry = (expiry_date - current_date).days
    return days_until_expiry <= 45

# Define a strategy for generating expiry dates within a range
expiry_date_strategy = st.dates(min_value=datetime.now().date(), max_value=datetime.now().date() + timedelta(days=365))

# Use Hypothesis to generate test cases for expiry alerts
@given(expiry_date=expiry_date_strategy)
def test_expiry_alert_generation(expiry_date):
    alert_generated = generate_expiry_alert(expiry_date)
    
    # Check if the alert is generated correctly based on the expiry date
    days_until_expiry = (expiry_date - datetime.now().date()).days
    expected_alert = days_until_expiry <= 45

    assert alert_generated == expected_alert

# Run the test
test_expiry_alert_generation()
