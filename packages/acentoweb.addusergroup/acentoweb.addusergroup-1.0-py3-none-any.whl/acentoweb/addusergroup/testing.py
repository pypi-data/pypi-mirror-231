# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import acentoweb.addusergroup


class AcentowebAddusergroupLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=acentoweb.addusergroup)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'acentoweb.addusergroup:default')


ACENTOWEB_ADDUSERGROUP_FIXTURE = AcentowebAddusergroupLayer()


ACENTOWEB_ADDUSERGROUP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ACENTOWEB_ADDUSERGROUP_FIXTURE,),
    name='AcentowebAddusergroupLayer:IntegrationTesting',
)


ACENTOWEB_ADDUSERGROUP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ACENTOWEB_ADDUSERGROUP_FIXTURE,),
    name='AcentowebAddusergroupLayer:FunctionalTesting',
)


ACENTOWEB_ADDUSERGROUP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ACENTOWEB_ADDUSERGROUP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='AcentowebAddusergroupLayer:AcceptanceTesting',
)
