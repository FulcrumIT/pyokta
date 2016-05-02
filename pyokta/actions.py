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
