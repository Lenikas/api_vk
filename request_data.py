class RequestFormat:
    def __init__(self, method, optional_params="", your_id=""):
        self.id = your_id
        self.token = "ваш токен тут"
        self.base = "https://api.vk.com/method/"
        self.method = f"{method}/"
        self.version_token = f"?{optional_params}v=5.52&access_token="

    def format_request(self):
        return self.base + self.method + self.version_token + self.token
