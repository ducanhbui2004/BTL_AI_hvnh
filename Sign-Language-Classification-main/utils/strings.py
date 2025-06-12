
class ExpressionHandler:

    MAPPING = {
        "bình_thường": "Ngồi yên 🤐",
        "cảm_ơn": "Cảm ơn 😘",
        "xin_chào": "Xin chào 🙋‍",
        "yêu": "Yêu ❤️",
        "không": "Không 🤚",    
        "có": "Có 👌",
        "Giúp": "Giúp đỡ 🆘",
        "ăn": "Ăn 🍽️",
        "đau": "Đau 😖",
        "khỏe": "khỏe 😊",
        "đi_chơi": "Đi chơi 🏃‍",
        "thích": "Thích 👍",
        "nhiều_hơn": "Nhiều hơn ➕",
    }
    
    def __init__(self):
        # Save the current message and the time received the current message
        self.current_message = ""

    def receive(self, message):
        self.current_message = message

    def get_message(self):
        return ExpressionHandler.MAPPING[self.current_message]
