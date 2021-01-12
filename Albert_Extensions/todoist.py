# -*- coding: utf-8 -*-

"""Quickly lanuch a temporary Firefox instance."""

from albert import *
import os

__title__ = "Wade Test Extention"
__version__ = "0.4.1"
__triggers__ = "wade "
__authors__ = "Wade Allen"

iconPath = os.path.dirname(__file__)+"/todoist.png"

def handleQuery(query):
    if not query.isTriggered:
        return

    results = []

    results.append(
        Item(
            id=__title__,
            icon=iconPath,
            text="Launch temporary Firefox profile",
            subtext="This will create a new temporary Firefox profile and launch an instance with it.",
            completion=query.rawString,
            actions=[
                # Command taken from: https://news.ycombinator.com/item?id=18898865
                FuncAction("Launch temporary Firefox", lambda: os.system("firefox --new-instance --profile $(mktemp -d) &"))
            ]
        )
    )

    return results