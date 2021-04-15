#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from pathlib import Path
import shutil
import os
from os import path
import requests
from extensions import output, term
import git

# todo - add icon load & color changes
# get basic settings

from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import subprocess


project = "https://github.com/Michaelsafir/Yelm.ProjectX.git"
out = output()

def replace(file_path, pattern, subst):
	#Create temp file
	fh, abs_path = mkstemp()
	with fdopen(fh,'w') as new_file:
		with open(file_path) as old_file:
			for line in old_file:
				new_file.write(line.replace(pattern, subst))
	#Copy the file permissions from the old file to the new file
	copymode(file_path, abs_path)
	#Remove original file
	remove(file_path)
	#Move new file
	move(abs_path, file_path)
	out.log(term.OK, f"changed - {subst}")


def load_icon(folder_path, platform):
	# image_url = f"https://yelm.io/pre_load{platform}.png"
	image_url = f"https://yelm.io/images/design/logotype.ac3b96.png"
	filename = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/start.imageset/start.png"

	r = requests.get(image_url, stream = True)

	# Check if the image was retrieved successfully
	if r.status_code == 200:
		# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
		r.raw.decode_content = True
		
		# Open a local file with wb ( write binary ) permission.
		with open(filename,'wb') as f:
			shutil.copyfileobj(r.raw, f)
			
		out.log(term.WARNING, f"icon of application loaded - {filename}")
	else:
		out.log(term.FAIL, f"fail loading image \n- {filename}")
		exit()

from subprocess import Popen, PIPE

def run(command, platform):
	process = Popen(f"{command}", stdout=None, shell=True, cwd=f'projects/{platform}/Yelm.ProjectX')
	process.wait()
	while True:
		try:
			line = process.stdout.readline().rstrip()
			if not line:
				break
			yield line
		except Exception as e:
			break


def run_build(platform, action):
	out.log(term.WARNING, "pod install")
	for path in run("pod install", platform):
		print(path.decode('utf-8'))

	out.log(term.OKCYAN, "ready pods")



	if (action == "load_screens"):
		out.log(term.WARNING, "fastlane snapshot")

		for path in run("fastlane snapshot", platform):
			print(path.decode('utf-8'))

	if (action == "upload_beta"):
		out.log(term.WARNING, "fastlane beta")

		for path in run("fastlane beta", platform):
			print(path.decode('utf-8'))
		


	# for path in run("bundle exec fastlane snapshot", platform):
	# 	print(path.decode('utf-8'))


def assamble_project(folder_path, platform, action):

	new_platform = f'var platform : String = "{platform}"'
	new_merchant = f'var merchant : String = "merchant.{platform}.yelm.io"'

	r = requests.get(f"https://rest.yelm.io/api/mobile/published?platform={platform}", stream = True) 

	name = ""
	description = ""
	icon = ""

	theme = ""


	if r.status_code == 200:
		json = r.json()
		name = json["name"]
		icon = json["published_data"]["logotype"]
		description = json["published_data"]["description"]
		theme = json["setting"]["theme"]

	else:
		out.log(term.FAIL, f"fail loading metadata \n- {platform}")
		exit()

	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/variables.swift", 'static var theme = Color.init(hex: "5DC837")', f'static var theme = Color.init(hex: "{theme}")')
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/variables.swift", 'var platform : String = "5fd33466e17963.29052139"', new_platform)
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/Info.plist", 'Енот', name)
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/Info.plist", '<string>yelm.io.projects.Yelm-ProjectX</string>', f'<string>yelm.io.projects.{platform}</string>')
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/variables.swift", 'var merchant : String = "merchant.5fd33466e17963.29052139.yelm.io"', new_merchant)
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX.xcodeproj/project.pbxproj", 'PRODUCT_BUNDLE_IDENTIFIER = "yelm.io.projects.Yelm-ProjectX"', f'PRODUCT_BUNDLE_IDENTIFIER = "yelm.io.projects.{platform}"')


	load_icon(folder_path, platform)
	out.log(term.OKCYAN, "ready to build")

	run_build(platform, action)
	pass

def load(platform, action):
	out.log(term.OK, "git function init start")
	out.log(term.OK, "platform - " + platform)

	out.log(term.NONE, "create folder - " + platform)
	try: 

		if (path.exists(f"projects/{platform}")):
			shutil.rmtree(f"projects/{platform}")
		Path(f"projects/{platform}").mkdir(parents=True, exist_ok=True)

	except Exception as e:
		out.log(term.FAIL, f"error - {e}")
		exit()

	folder_path = f"projects/{platform}"
	out.log(term.OK, f"created {folder_path} folder for project")

	out.log(term.OKCYAN, f"download project")
	try: 
		git.Git(folder_path).clone(project)
	except Exception as e:
		out.log(term.FAIL, f"error - {e}")
		exit()

	out.log(term.OKCYAN, f"download done")
	out.log(term.WARNING, f"prepare for assamble {folder_path}")

	
	assamble_project(folder_path, platform, action)


if __name__ == '__main__':
	arguments_count = len(sys.argv)
	if (arguments_count > 0):
		if (sys.argv[1] == "load_screens"):
			load(sys.argv[2], "load_screens")
		if (sys.argv[1] == "upload_beta"):
			load(sys.argv[2], "upload_beta")
		pass
