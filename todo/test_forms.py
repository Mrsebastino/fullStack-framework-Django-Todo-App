from django.test import TestCase
# ItemForm is the class in forms.py
from .forms import ItemForm
"""
 create a class that will inherit Testcase
 and maintain all of our test for this form
 """


class TestItemForm(TestCase):
    # name our test so when they fail we can easily found the issue
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
    # this form isn't valid so we use assertfalse to make sure it's the case
        self.assertFalse(form.is_valid())
    # send a dict of field on which error and error message
        self.assertIn('name', form.errors.keys())
    # finally check if the error message is for the missing name
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # test the done field
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test todo item'})
        self.assertTrue(form.is_valid())
    """
    write a test to ensure that the only fields
    display in the form are ours
    """

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
