from ftw.contentnav.interfaces import IFtwContentNavLayer
from ftw.contentnav.testing import FTW_CONTENTNAV_INTEGRATION_TESTING
from plone.browserlayer import utils
from Products.CMFCore.utils import getToolByName
from unittest2 import TestCase


class TestPackageInstall(TestCase):

    layer = FTW_CONTENTNAV_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_package_installed(self):
        pid = 'ftw.contentnav'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertIn(
            pid, installed, 'package appears not to have been installed')

    def test_browserlayer_registered(self):
        self.assertIn(IFtwContentNavLayer, utils.registered_layers())

    def test_index_getContentCategories_installed(self):
        catalog = getToolByName(self.portal, "portal_catalog")
        self.assertIn('getContentCategories', catalog.indexes())


class TestPackageUninstall(TestCase):

    layer = FTW_CONTENTNAV_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        try:
            self.qi_tool.uninstallProducts(['ftw.contentnav'])
        except:
            pass

    def test_package_is_not_installed(self):
        pid = 'ftw.contentnav'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertNotIn(
            pid, installed, 'package appears not to have been installed')

    def test_browserlayer_no_longer_registered(self):
        self.assertNotIn(IFtwContentNavLayer, utils.registered_layers())

    # def test_index_getContentCategories_is_removed(self):
    #     catalog = getToolByName(self.portal, "portal_catalog")
    #     self.assertNotIn('getContentCategories', catalog.indexes())
