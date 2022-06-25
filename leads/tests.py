from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse("landing"))
        # print(dir(response))
        # print('++++++++++++++++++')
        # print(response.content)
        # print('++++++++++++++++++')
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("landing"))
        self.assertTemplateUsed(response, 'landin.html')