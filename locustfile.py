from locust import HttpUser, task, between
import json


# Data to be sent in JSON format
data = {
    "name": "1",
}

headers = {
    "Content-Type": "application/json",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0MiwidXNlcm5hbWUiOiJhbGljZSIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTY5NjI3MTgxN30.G5RvnHzlYBiS9WNjTYNo7sKIgcw3toeTts1MvQCzMGHZE8IBTVL30p-Q-X4Sxev9JPdEmWEb9qbVGKz1UZMakOmhuWt2uHSmAiC0J_OV2y3R-Tyibeo4aNVKI22m2C_rYgZ6IiKH1FujJobzgMZTgpUM8KTbqR9SRQFd9UafAw0aZwcvZZjSdjk0udKv7n1hWlocvTLjburpGwbVw4bRMGMEg_rGGej86h_mpZS5-VALqlG1rlW9wOsWFwE__S1inRRpQ9gDghLjvcELVvNM42yiMRM2I79I6AXm9O1UFW1LBVYbDpvNChWSv4YPxf1edNevpvfq_ZMnDLoPfGh2dA"
}


class MyLocust(HttpUser):
    wait_time = between(1, 5)

    @task
    def create_user(self):
        self.client.post('customer', json=data, headers=headers)
