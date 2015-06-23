from ftw.builder.testing import BUILDER_LAYER
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID, setRoles
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.testing import z2
from zope.configuration import xmlconfig


class FtwContentnavIntegrationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, BUILDER_LAYER)

    def setUpZope(self, app, configurationContext):
        # Load ZCML        
        import ftw.contentnav
        xmlconfig.file('configure.zcml', ftw.contentnav,
                       context=configurationContext)

        # installProduct() is *only* necessary for packages outside
        # the Products.* namespace which are also declared as Zope 2 products,
        # using <five:registerPackage /> in ZCML.
        # z2.installProduct(app, 'ftw.contentnav')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        # applyProfile(portal, 'ftw.contentnav:default')

        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)


FTW_CONTENTNAV_FIXTURE = FtwContentnavIntegrationLayer()
FTW_CONTENTNAV_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FTW_CONTENTNAV_FIXTURE,), name="FtwCONTENTNAV:Integration")
FTW_CONTENTNAV_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FTW_CONTENTNAV_FIXTURE,
           set_builder_session_factory(functional_session_factory)),
    name="FtwContentnav:Functional")
