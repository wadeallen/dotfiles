from albert import *
import os

__title__ = "Scripture This Week"
__version__ = "0.4.2"
__triggers__ = "pa "
__authors__ = "Wade Allen"

iconPath = os.path.dirname(__file__)+"/bible.svg"

def handleQuery(query):
	if not query.isTriggered:
		return

	items = []

	for i in range(3):
		number = i
		items.append(
			Item(
				id=__title__,
				icon= iconPath,
			    text=f"Number {number}",
			    subtext="This is another test",)
			)

	return items


