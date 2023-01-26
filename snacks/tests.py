from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


class SnacksTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="pickle", purchaser=self.user, description="pickle description",
            image_url="http://pickel-image-url.com",
        )


    def test_home_page_status_code(self):
        url = reverse('snack_list')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')


    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "pickle")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.description, "pickle description")

    def test_Snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "apple",
                "description": "red and roundish",
                "purchaser": self.user.id,
            }, follow=True
        )
        self.assertContains(response, "apple")
    #
    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated name", "purchaser": self.user.id, "description": "test description",
             "image_url": "testimageurl.com", "reference_url": "testreferenceurl.com"}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"), target_status_code=200)
    #
    def test_snack_update_bad_url(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated name", "rating": 3, "purchaser": self.user.id, "description": "test description",
             "image_url": "badurl", "reference_url": "testreferenceurl.com"}
        )
        self.assertEqual(response.status_code, 200)

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)

    # you can also tests models directly
    def test_model(self):
        snack = Snack.objects.create(title="chip", purchaser=self.user)
        self.assertEqual(snack.title, "chip")
