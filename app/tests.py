from django.test import TestCase,Client
from django.contrib.auth.models import User
from .models import Puzzle
class DefaultPageCase(TestCase):
 def test_home(self):
   response = self.client.get('/')
   self.assertEqual(response.status_code, 200)
 def test_create_puzzle(self):
   response = self.client.get('/createpuzzle/')
   self.assertEqual(response.status_code, 200)
 def test_album(self):
   response = self.client.get('/r^album/')
   self.assertEqual(response.status_code, 200)
 def test_album_admin(self):
   response = self.client.get('/album_admin/')
   self.assertEqual(response.status_code, 200)
 def test_admin_page(self):
   response = self.client.get('/admin')
   self.assertEqual(response.status_code, 302)
class CRUDTestCase(TestCase):
 def setUp(self) -> None:
   self.client = Client()
 def test_create_puzzle(self):
        response = self.client.post(
            '/createpuzzle/',
            {'name': 'Test_Puzzle', 'number_of_details': '1000', 
			 'age': 100, 'ifalldetails': True, 'description': 'Test_description',
			 'imagepath': 'Test_imagepath','category': 1, 'manufacturer': 1 },
            follow=True
        )
        self.assertTrue(Puzzle.objects.all())
 def test_edit_and_save_puzzle(self):
       response = self.client.post(
            '/createpuzzle/',
            {'name': 'Test_Puzzle', 'number_of_details': '1000', 
			 'age': 100, 'ifalldetails': True, 'description': 'Test_description',
			 'imagepath': 'Test_imagepath','category': 1, 'manufacturer': 1 },
            follow=True
        )
       response = self.client.post(
            '/editpuzzle/',
            {'name': 'Test_Puzzle', 'number_of_details': '4000', 
			 'age': 100, 'ifalldetails': True, 'description': 'Test_description',
			 'imagepath': 'Test_imagepath','category': 1, 'manufacturer': 1 },
            follow=True
        )
       self.assertTrue(Puzzle.objects.all())
 def test_create_and_view_puzzle(self):
        response = self.client.post(
            '/createpuzzle/',
            {'name': 'Test_Puzzle', 'number_of_details': '1000', 
			 'age': 100, 'ifalldetails': True, 'description': 'Test_description',
			 'imagepath': 'Test_imagepath','category': 1, 'manufacturer': 1 },
            follow=True
        )
        self.assertTrue(Puzzle.objects.all())
        response = self.client.get('/puzzleinfo_<1>/')
        self.assertEqual(response.status_code, 404)
 def test_edit_puzzle(self):
        response = self.client.get('/editpuzzle/{self.puzzle.PK_Puzzle}')
        self.assertEqual(response.status_code, 404)
 def test_delete_puzzle(self):
        response = self.client.get('/puzzleinfo_{self.puzzle.PK_Puzzle}')
        self.assertEqual(response.status_code, 404)
 def test_puzzle_info(self):
        response = self.client.get('/deletepuzzle_{self.puzzle.PK_Puzzle}')
        self.assertEqual(response.status_code, 404)
 def test_template_used(self):
   response = self.client.get('/')
   self.assertTemplateUsed(response, 'app/index.html')



