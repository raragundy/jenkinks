#!/usr/bin/python3

"""
Imports dependencies app
"""

from crypt import methods
from distutils.log import debug
from pickle import FALSE
from flask import Flask, request, jsonify
from functools import wraps

APP = Flask(__name__)


def check_card(func):
    """
    This function validates the credit card transactions
    """
    wraps(func)

    def validation(*args, **kwargs):
        """
        This function is a decorator
        which will return the function corresponding to the respective action
        """
        data = request.get_json()
        if not data.get("status"):
            response = {
                "approved": False,
                "newLimit": data.get("limit"),
                "reason": "Blocked Card"
            }
            return jsonify(response)

        if data.get("limit") < data.get("transaction").get("amount"):
            response = {
                "approved": False,
                "newLimit": data.get("limit"),
                "reason": "Transaction above the limit"
            }
            return jsonify(response)
        return func(*args, **kwargs)
    return validation


@APP.route("/api/transaction", methods=["POST"])
@check_card
def transaction():
    """
    This function is resposible to expose the endpoint for receiving 
    the incoming transaction
    """
    card = request.get_json()
    new_limit = card.get("limit") - card.get("transaction").get("amount")
    response = {"approved": True, "newLimit": new_limit}
    return jsonify(response)


if __name__ == '__main__':
    APP.run(debug=True)
