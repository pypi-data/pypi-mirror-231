# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
from plone.supermodel import model
from plone.autoform.directives import widget

from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider
from plone.app.z3cform.widget import SelectFieldWidget

class IAcentowebAddusergroupLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""



class IUserGroupSettings(model.Schema):
    """Adds settings to medialog.controlpanel
    """

    model.fieldset(
        'usergroups',
        label=(u'User Groups'),
        fields=[
            'usergroup',
            ],
    )
 
    usergroup = schema.Tuple(
        title = u"User Group",
        required=False, 
        missing_value=(),
        value_type=schema.Choice(
            title='Group to add users to',
            vocabulary= "plone.app.vocabularies.Groups",        
        ),
    )


alsoProvides(IUserGroupSettings, IMedialogControlpanelSettingsProvider)
