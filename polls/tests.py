import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() return True for questions whose pub_at is within the last day.
        """

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)

        recent_question = Question(pub_at=time)

        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() return False for questions whose pub_at is older than 1 day.
        """

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)

        old_question = Question(pub_at=time)

        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() return False for questions whose pub_at is in the future.
        """

        time = timezone.now() + datetime.timedelta(days=30)

        future_question = Question(pub_at=time)

        self.assertIs(future_question.was_published_recently(), False)


def create_question(text, days):
    """
    create a question with the given `text` and published the given number
    of `days`offset to now (negative for questions published in the past, possitive
    for questions that have yet to be published).
    """

    time = timezone.now() + datetime.timedelta(days=days)

    return Question.objects.create(text=text, pub_at=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "No polls are available.")

        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with pub_at in the past are displayed on the index page.
        """

        past_question = create_question(text="Past question.", days=-30)

        response = self.client.get(reverse("polls:index"))

        self.assertContains(response, past_question.text)

        self.assertQuerySetEqual(
            response.context["latest_question_list"], [past_question]
        )

    def test_future_question(self):
        """
        Questions with pub_at in the future aren't displayed on the index page.
        """

        future_question = create_question(text="Future question.", days=30)

        response = self.client.get(reverse("polls:index"))

        self.assertNotContains(response, future_question.text)

        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions are diesplayed.
        """

        past_question = create_question(text="Past question.", days=-30)
