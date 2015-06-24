from ftw.builder import Builder
from ftw.builder import create
from ftw.contentnav.testing import FTW_CONTENTNAV_FUNCTIONAL_TESTING
from plone.dexterity.fti import DexterityFTI
from Products.CMFCore.utils import getToolByName
from unittest2 import TestCase


class TestContentCategoriesBehavior(TestCase):

    layer = FTW_CONTENTNAV_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        # add sample fti
        self.fti = DexterityFTI('Sample')
        self.fti.schema = \
            'ftw.contentnav.tests.test_content_categorie_behavior.ISampleDX'
        self.fti.behaviors = (
            'ftw.contentnav.behaviors.content_categories.IContentCategories', )

        self.portal.portal_types._setObject('Sample', self.fti)

    def test_category_index(self):
        catalog = getToolByName(self.portal, 'portal_catalog')

        create(Builder('sample')
               .having(content_categories=(u'DEMO1', )))

        self.assertTrue(catalog({'getContentCategories': 'DEMO1'})[0])

    def test_category_index_umlauts(self):
        catalog = getToolByName(self.portal, 'portal_catalog')

        create(Builder('sample')
               .having(content_categories=(u'WITH unicode \xe4', )))

        unique_values = catalog.Indexes['getContentCategories'].uniqueValues()
        self.assertIn("WITH unicode \xc3\xa4", unique_values)
