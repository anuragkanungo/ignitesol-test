from django.shortcuts import render
import urllib2
from xml.dom import minidom, Node

def output(request):
	return render(request, 'output.html')

def input_form(request):
	return render(request, 'input_form.html')

def input_feed(request):

	url = request.GET['q']

	""" Get the XML """
	url_info = urllib2.urlopen(url)

	if (url_info):
		""" We have the RSS XML lets try to parse it up """
		xmldoc = minidom.parse(url_info)
		if (xmldoc):
			"""We have the Doc, get the root node"""
			rootNode = xmldoc.documentElement
			""" Iterate the child nodes """
			feedList = []
			for subNode in rootNode.childNodes: #Channel Node
				for node in subNode.childNodes:
					""" We only care about "item" entries"""
					if (node.nodeName == "item"):
						tempDict = {}
						""" Now iterate through all of the <item>'s children """
						for item_node in node.childNodes:
							if (item_node.nodeName == "title"):
								title = ""
								for text_node in item_node.childNodes:
									if (text_node.nodeType == node.TEXT_NODE):
										title += text_node.nodeValue
								if (len(title)>0):
									tempDict['title'] = title

							if (item_node.nodeName == "pubDate"):
								date = ""
								for text_node in item_node.childNodes:
									if (text_node.nodeType == node.TEXT_NODE):
										date += text_node.nodeValue
								if (len(date)>0):
									tempDict['date'] = date


							if (item_node.nodeName == "description"):
								""" Loop through the description Text nodes to get
								the actual description"""
								description = ""
								for text_node in item_node.childNodes:
									if (text_node.nodeType == node.TEXT_NODE):
										description += text_node.nodeValue
								if (len(description)>0):
									tempDict['description'] = description


							if (item_node.nodeName == "link"):
								link = ""
								for text_node in item_node.childNodes:
									if (text_node.nodeType == node.TEXT_NODE):
										link += text_node.nodeValue
								if (len(link)>0):
									tempDict['link'] = link

							if (item_node.nodeName == "media:thumbnail"):
								url = item_node.getAttribute("url")
								if (len(url)>0):
									tempDict['media'] = url


						feedList.append(tempDict)

		else:
			print "Error getting XML document!"
	else:
		print "Error! Getting URL"

	return render(request, 'output.html', {'feedList':feedList})



# Create your views here.
