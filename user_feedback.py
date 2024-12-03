from datetime import datetime
from db_connection import get_db_connection
from reminder_and_notification_system import send_reminder


class UserFeedback:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.cursor = self.db_connection.cursor()
        self.rewards = 0

    def collect_feedback(self):
        try:
            food_quality = int(input("Rate the food quality (1-5): "))
            service_efficiency = int(input("Rate service efficiency (1-5): "))
            menu_variety = int(input("Rate menu variety (1-5): "))
            comments = input("Additional comments (optional): ")

            feedback = {
                'food_quality': food_quality,
                'service_efficiency': service_efficiency,
                'menu_variety': menu_variety,
                'comments': comments
            }
            self.save_feedback(feedback)
            print("✅ Feedback submitted successfully! Thank you for your input. 😊")
        except ValueError:
            print("❗ Invalid input. Please enter numbers between 1 and 5 for ratings.")

    def save_feedback(self, feedback):
        try:
            query = """
                INSERT INTO feedback (food_quality, service_efficiency, menu_variety, comments, submission_date)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                feedback['food_quality'],
                feedback['service_efficiency'],
                feedback['menu_variety'],
                feedback['comments'],
                datetime.now()
            )
            self.cursor.execute(query, values)
            self.db_connection.commit()
            self.rewards += 1  # Increase rewards for each feedback submission
        except Exception as err:
            print(f"❌ Failed to save feedback: {err}")

    def display_rewards(self):
        print(f"🎉 You have {self.rewards} reward points!") if self.rewards > 0 else print(
            "🔄 You currently have 0 reward points. Keep submitting feedback to earn rewards! 🙁"
        )

    def check_reminder(self):
        try:
            query = "SELECT submission_date FROM feedback ORDER BY submission_date DESC LIMIT 1"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result:
                last_feedback_date = result[0]
                send_reminder(last_feedback_date)
            else:
                print("❗ You haven't submitted any feedback yet. Please provide feedback to start receiving reminders. 📝")
        except Exception as err:
            print(f"❌ Failed to retrieve feedback data: {err}")

    def close_connection(self):
        self.cursor.close()
        self.db_connection.close()
