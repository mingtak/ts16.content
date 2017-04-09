# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from ts16.content.testing import TS16_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ts16.content is properly installed."""

    layer = TS16_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ts16.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ts16.content'))

    def test_browserlayer(self):
        """Test that ITs16ContentLayer is registered."""
        from ts16.content.interfaces import (
            ITs16ContentLayer)
        from plone.browserlayer import utils
        self.assertIn(ITs16ContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TS16_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ts16.content'])

    def test_product_uninstalled(self):
        """Test if ts16.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ts16.content'))

    def test_browserlayer_removed(self):
        """Test that ITs16ContentLayer is removed."""
        from ts16.content.interfaces import \
            ITs16ContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITs16ContentLayer, utils.registered_layers())
