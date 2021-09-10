from datetime import date, timedelta
import json
from unittest.case import expectedFailure
from statistics_api.facebook.models import PostHistory
from statistics_api.facebook.factories import UserFactory
from rest_framework.authtoken.models import Token
from django.test import TestCase
from rest_framework.test import APIClient

class CreatePostTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.token = f"Token {Token.objects.filter(user=self.user).first().key}"
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.post_endpoint = "/api/v1/posts/"
        self.post_history_endpoint = "/api/v1/posthistory/"
        self.default_payload = {
            "post_id": "ABC123",
            "user_id": "EFG098",
            "likes": 10
        }

    def test_create_post_sucessfully(self):
        result = self.client.post(self.post_endpoint, json.dumps(self.default_payload), content_type="application/json")
        assert result.json() == self.default_payload

        assert PostHistory.objects.count() == 1

    def test_create_post_sucessfully_and_update_it(self):
        result = self.client.post(self.post_endpoint, json.dumps(self.default_payload), content_type="application/json")
        assert result.json() == self.default_payload
        
        self.default_payload["likes"] = 30
        result = self.client.post(self.post_endpoint, json.dumps(self.default_payload), content_type="application/json")
        assert result.json() == self.default_payload

        assert PostHistory.objects.count() == 1

    def test_create_and_retrieve_post(self):
        result = self.client.post(self.post_endpoint, json.dumps(self.default_payload), content_type="application/json")
        assert result.json() == self.default_payload

        result = self.client.get(f"{self.post_endpoint}{self.default_payload['post_id']}/", content_type="application/json")
        assert result.json() == self.default_payload

    def test_list_average_likes_from_user(self):
        likes_post_one = [10, 7, 5, 3, 1]
        likes_post_two = [19, 12, 10, 3, 0]
        user_id = "1"
        initial_date = date(2021, 10, 1)
        expected_result = [
            {
                "user_id": "1",
                "created_at": "2021-09-27",
                "average_likes": 0.5
            },
            {
                "user_id": "1",
                "created_at": "2021-09-28",
                "average_likes": 3.0
            },
            {
                "user_id": "1",
                "created_at": "2021-09-29",
                "average_likes": 7.5
            },
            {
                "user_id": "1",
                "created_at": "2021-09-30",
                "average_likes": 9.5
            },
            {
                "user_id": "1",
                "created_at": "2021-10-01",
                "average_likes": 14.5
            }
        ]

        for i, likes in enumerate(likes_post_one):
            h = PostHistory(
                user_id=user_id,
                post_id="1",
                likes=likes,
                created_at=initial_date-timedelta(days=i)
            )
            h.save()

        for i, likes in enumerate(likes_post_two):
            h = PostHistory(
                user_id=user_id,
                post_id="2",
                likes=likes,
                created_at=initial_date-timedelta(days=i)
            )
            h.save()
        
        response = self.client.get(f"{self.post_history_endpoint}month_average/?user_id={user_id}", content_type="application/json")

        assert response.json() == expected_result
