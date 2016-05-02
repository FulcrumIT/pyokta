import pyokta.api as _api
import json as _json


def get_all_users():
    """Return all Okta users."""
    return _api.rest("/users")


def get_user(id):
    """Return data on one particular user.

    Parameters:
    - id: id of an Okta user.
    """
    return _api.rest("/users/" + str(id))


def get_all_groups():
    """Return all Okta groups."""
    return _api.rest("/groups")


def get_group(id):
    """Return data on one particular group.

    Parameters:
    - id: id of an Okta group.
    """

    return _api.rest("/groups/" + str(id))


def get_group_users(id):
    """Return users in a particular group.

    Parameters:
    - id: id of an Okta group.
    """

    return _api.rest("/groups/" + str(id) + "/users")
