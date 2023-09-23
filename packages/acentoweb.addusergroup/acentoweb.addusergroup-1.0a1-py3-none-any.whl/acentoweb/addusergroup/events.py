# -*- coding: utf-8 -*-
from plone import api

def add_user_to_group(event):
    """Event subscriber to add a user to specific groups after the first login."""

    # Get the user object from the event
    user = event.object
    
 
    # Get the user id
    user_id = user.getId()
    #alternatively plone.api.user.get_current()

    import pdb; pdb.set_trace()

    # Add the user to the groups
    #plone.api.group.add_user(groupname=None, group=None, username=None, user=None)
    plone.api.group.add_user(groupname='group1',, username=None, user=None)