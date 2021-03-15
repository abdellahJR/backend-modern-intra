from intraApp.models import *
from django.test import TestCase




class ModelsTestCase(TestCase):
    def setUp(self):
        company = Company.objects.create(name="companyTest")
        company2 = Company.objects.create(name="companyTest2")
        # customer = CustomUse.objects.create(name='dupont', email='dupont@gmail.com', company=company)
        # customer2 = CustomUse.objects.create(name='dupont2', email='dupont2@gmail.com', company=company2)
        # customuse = CustomUse.objects.create(name='dupont', email='dupont@gmail.com', company=company)
        # customuse2 = CustomUse.objects.create(name='dupont2', email='dupont2@gmail.com', company=company2)

    def test_company(self):
        company =  Company.objects.get(name="campanyTest")
        company2 = Company.objects.get(name="campanyTest2")
        self.assertEqual(str(company), "campanyTest")
        self.assertEqual(str(company2), "campanyTest2")

    # def test_customuser(self):
    #     customer = CustomUse.objects.get(email='dupont@gmail.com')
    #     customer2 = CustomUse.objects.get(email='dupont2@gmail.com')
    #     self.assertEqual(str(customer), "dupont@gmail.com")
    #     self.assertEqual(str(customer2), "dupont2@gmail.com")

