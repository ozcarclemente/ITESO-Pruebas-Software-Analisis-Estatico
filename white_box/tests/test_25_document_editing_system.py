"""
Unit tests for DocumentEditingSystem classs.
"""

import unittest

from white_box.class_exercises import DocumentEditingSystem


class TestWhiteBoxDocumentEditingSystem(unittest.TestCase):
    """
    DocumentEditingSystem class unit tests.
    """

    def setUp(self):
        """Initialize document system."""
        self.doc = DocumentEditingSystem()
        self.assertEqual(self.doc.state, "Editing")

    def test_save_document_success(self):
        """Save document from Editing state."""
        output = self.doc.save_document()
        self.assertEqual(self.doc.state, "Saved")
        self.assertEqual(output, "Document saved successfully")

    def test_save_document_invalid_when_saved(self):
        """Save document when already Saved (invalid)."""
        self.doc.state = "Saved"
        output = self.doc.save_document()
        self.assertEqual(self.doc.state, "Saved")
        self.assertEqual(output, "Invalid operation in current state")

    def test_edit_document_success(self):
        """Resume editing from Saved state."""
        self.doc.state = "Saved"
        output = self.doc.edit_document()
        self.assertEqual(self.doc.state, "Editing")
        self.assertEqual(output, "Editing resumed")

    def test_edit_document_invalid_when_editing(self):
        """Edit document when already Editing (invalid)."""
        output = self.doc.edit_document()
        self.assertEqual(self.doc.state, "Editing")
        self.assertEqual(output, "Invalid operation in current state")
