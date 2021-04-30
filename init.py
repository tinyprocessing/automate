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

from PIL import Image
import time

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



def load_icon(folder_path, platform, icon):
	# image_url = f"https://yelm.io/pre_load{platform}.png"
	# AppIcon.appiconset
	image_url = f"{icon}"
	filename = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/start.imageset/start.png"


	icon_40 = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-40.png"
	icon_402x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-40@2x.png"
	icon_403x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-40@3x.png"
	icon_602x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-60@2x.png"
	icon_603x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-60@3x.png"
	icon_72 = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-72.png"
	icon_722x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-72@2x.png"
	icon_76 = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-76.png"
	icon_762x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-76@2x.png"
	icon_8352x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-83.5@2x.png"

	icon_small_50 = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-small-50.png"
	icon_small_502x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-small-50@2x.png"
	icon_small = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-small.png"
	icon_small2x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-small@2x.png"
	icon_small3x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon-small@3x.png"
	icon = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon.png"
	icon2x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/icon@2x.png"
	ios_marketing = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/ios-marketing.png"
	notification_icon2x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/notification-icon@2x.png"
	notification_icon3x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/notification-icon@3x.png"
	notification_iconipad = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/notification-icon~ipad.png"
	notification_iconipad2x = f"{folder_path}/Yelm.ProjectX/Yelm.ProjectX/Assets.xcassets/AppIcon.appiconset/notification-icon~ipad@2x.png"







	r = requests.get(image_url, stream = True)

	# Check if the image was retrieved successfully
	if r.status_code == 200:
		# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
		r.raw.decode_content = True
		

		f = open(filename, 'wb')
		shutil.copyfileobj(r.raw, f)
		image = Image.open(icon_40)
		new_image = image.resize((1024, 1024))
		new_image.save(icon_40)
		f.close()


		shutil.copy2(filename, icon_40)
		image = Image.open(icon_40)
		new_image = image.resize((40, 40))
		new_image.save(icon_40)

		shutil.copy2(filename, icon_402x)
		image = Image.open(icon_402x)
		new_image = image.resize((80, 80))
		new_image.save(icon_402x)

		shutil.copy2(filename, icon_403x)
		image = Image.open(icon_403x)
		new_image = image.resize((120, 120))
		new_image.save(icon_403x)

		shutil.copy2(filename, icon_602x)
		image = Image.open(icon_602x)
		new_image = image.resize((120, 120))
		new_image.save(icon_602x)

		shutil.copy2(filename, icon_603x)
		image = Image.open(icon_603x)
		new_image = image.resize((180, 180))
		new_image.save(icon_603x)

		shutil.copy2(filename, icon_72)
		image = Image.open(icon_72)
		new_image = image.resize((72, 72))
		new_image.save(icon_72)

		shutil.copy2(filename, icon_722x)
		image = Image.open(icon_722x)
		new_image = image.resize((144, 144))
		new_image.save(icon_722x)

		shutil.copy2(filename, icon_76)
		image = Image.open(icon_76)
		new_image = image.resize((76, 76))
		new_image.save(icon_76)

		shutil.copy2(filename, icon_762x)
		image = Image.open(icon_762x)
		new_image = image.resize((152, 152))
		new_image.save(icon_762x)

		shutil.copy2(filename, icon_8352x)
		image = Image.open(icon_8352x)
		new_image = image.resize((167, 167))
		new_image.save(icon_8352x)


		shutil.copy2(filename, icon_small_50)
		image = Image.open(icon_small_50)
		new_image = image.resize((50, 50))
		new_image.save(icon_small_50)

		shutil.copy2(filename, icon_small_502x)
		image = Image.open(icon_small_502x)
		new_image = image.resize((100, 100))
		new_image.save(icon_small_502x)

		shutil.copy2(filename, icon_small)
		image = Image.open(icon_small)
		new_image = image.resize((29, 29))
		new_image.save(icon_small)

		shutil.copy2(filename, icon_small2x)
		image = Image.open(icon_small2x)
		new_image = image.resize((58, 58))
		new_image.save(icon_small2x)

		shutil.copy2(filename, icon_small3x)
		image = Image.open(icon_small3x)
		new_image = image.resize((87, 87))
		new_image.save(icon_small3x)

		shutil.copy2(filename, icon)
		image = Image.open(icon)
		new_image = image.resize((57, 57))
		new_image.save(icon)

		shutil.copy2(filename, icon2x)
		image = Image.open(icon2x)
		new_image = image.resize((114, 114))
		new_image.save(icon2x)

		shutil.copy2(filename, ios_marketing)
		image = Image.open(ios_marketing)
		new_image = image.resize((1024, 1024))
		new_image.save(ios_marketing)

		shutil.copy2(filename, notification_icon2x)
		image = Image.open(notification_icon2x)
		new_image = image.resize((40, 40))
		new_image.save(notification_icon2x)

		shutil.copy2(filename, notification_icon3x)
		image = Image.open(notification_icon3x)
		new_image = image.resize((60, 60))
		new_image.save(notification_icon3x)

		shutil.copy2(filename, notification_iconipad)
		image = Image.open(notification_iconipad)
		new_image = image.resize((20, 20))
		new_image.save(notification_iconipad)

		shutil.copy2(filename, notification_iconipad2x)
		image = Image.open(notification_iconipad2x)
		new_image = image.resize((40, 40))
		new_image.save(notification_iconipad2x)
		


		
			

		

			
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


	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/color.swift", 'static var theme = Color.init(hex: "5DC837")', f'static var theme = Color.init(hex: "{theme}")')
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/variables.swift", 'var platform : String = "5fd33466e17963.29052139"', new_platform)
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/variables.swift", 'var platform : String = "yelmio"', new_platform)
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/variables.swift", 'var distribution : Bool = false', 'var distribution : Bool = true')
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/Info.plist", 'Енот', name)
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/Info.plist", '<string>yelm.io.projects.Yelm-ProjectX</string>', f'<string>yelm.io.projects.{platform}</string>')
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/Info.plist", '<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>', f'<string>yelm.io.projects.{platform}</string>')
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/variables.swift", 'var merchant : String = "merchant.5fd33466e17963.29052139.yelm.io"', new_merchant)
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX/extensions/variables.swift", 'var merchant : String = "merchant.yelmio.yelm.io"', new_merchant)
	replace(folder_path+"/Yelm.ProjectX/Yelm.ProjectX.xcodeproj/project.pbxproj", 'PRODUCT_BUNDLE_IDENTIFIER = "yelm.io.projects.Yelm-ProjectX"', f'PRODUCT_BUNDLE_IDENTIFIER = "yelm.io.projects.{platform}"')


	load_icon(folder_path, platform, icon)
	out.log(term.OKCYAN, "ready to build")

	if (action == "download"):
		out.log(term.OK, "download done")
		out.log(term.WARNING, "pod install")
		for path in run("pod install", platform):
			print(path.decode('utf-8'))

	out.log(term.OKCYAN, "ready pods")
	out.log(term.WARNING, "git clear")
	for path in run("rm -rf .git", platform):
		print(path.decode('utf-8'))

	time.sleep(2)
	out.log(term.OK, "init git")
	for path in run("git init", platform):
		print(path.decode('utf-8'))

		exit()
	run_build(platform, action)
	pass

def load(platform, action):
	out.log(term.OK, "git function init start")
	out.log(term.OK, "platform - " + platform)

	out.log(term.NONE, "create folder - " + platform)
	try: 

		if (path.exists(f"projects/{platform}")):
			shutil.rmtree(f"projects/{platform}", ignore_errors=True)
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
		if (sys.argv[1] == "download"):
			load(sys.argv[2], "download")
		pass
