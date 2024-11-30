from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.sites.models import Site

from rest_framework.test import APITestCase
from rest_framework import status


from protected657.models import ProtectedFile

User = get_user_model()

class TestMyModelSetup(APITestCase):

    USERNAME = 'testare'
    PASSWORD = 'password1234'
    UPLOADFILE = f'{settings.BASE_DIR}/protected657/door_logo43.png'
    LIST_URL = '/protected/api/protected_files/'
    

    def setUp(self):
        # Create a user to login with
        self.user = User.objects.create_user(
            username=self.USERNAME,
            email='test@example.com',
            password=self.PASSWORD,
            is_staff=True,
            is_superuser=True,
        )
        current_site = Site.objects.get_current()
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        with open(self.UPLOADFILE, 'rb') as uploadfile:
            data = {
                'title': 'API test',
                'file': uploadfile,
                'created_by': self.user.id,
                'site': current_site.id,
            }
            _ = self.client.post(self.LIST_URL, data)
        pf = ProtectedFile.objects.all()[0]
        self.uploadfile_url = f'/protected/media/{pf.file}'
        self.client.logout()

    def tearDown(self):
        for pf in ProtectedFile.objects.all():
            pf.delete()
        
    def test_list_protected_files(self):
        """
        Ensure we can list protected files.
        """
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(self.LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.client.logout()

    def test_list_protected_files_forbidden(self):
        """
        Ensure logged out can't list protected files.
        """
        response = self.client.get(self.LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_upload_protected_file(self):
        """
        Ensure we can upload a file.
        """
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        current_site = Site.objects.get_current()
        with open(self.UPLOADFILE, 'rb') as uploadfile:
            data = {
                'title': 'API test',
                'file': uploadfile,
                'created_by': self.user.id,
                'site': current_site.id,
            }
            response = self.client.post(self.LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_upload_protected_file_forbidden(self):
        """
        Ensure we can upload a file.
        """
        current_site = Site.objects.get_current()
        with open(self.UPLOADFILE, 'rb') as uploadfile:
            data = {
                'title': 'API test',
                'file': uploadfile,
                'created_by': self.user.id,
                'site': current_site.id,
            }
            response = self.client.post(self.LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_get_uploaded_file(self):
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(self.uploadfile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
    
    def test_get_uploaded_file_forbidden(self):
        response = self.client.get(self.uploadfile_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)