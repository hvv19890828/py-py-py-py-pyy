#!/usr/bin/python3

# ------------------------------------------------
# Program by hvv19890828
#
#
# Version      Date           Info
# 1.0          19-08-2022     First born unicorn
#
# ----------------------------------------------

import docker
import re
from datetime import datetime
from dateutil.parser import isoparse


def match_repo_name(tag_tmplt, tag_list):
   repo_name = str(tag_list)
   repo_name_match = re.findall(tag_tmplt, repo_name)
   return repo_name_match

def time_diff(image_list, t_fmt):
   creation_date = str(isoparse(image_list.attrs["Created"]))
   creation_date_fmtd = re.sub(r"\..*", "", creation_date)
   current_date = str(datetime.now())
   current_date_fmtd = re.sub(r"\..*", "", current_date)
   tstamp1 = datetime.strptime(current_date_fmtd, t_fmt)
   tstamp2 = datetime.strptime(creation_date_fmtd, t_fmt)
   tdiff = tstamp1 - tstamp2
   tdiff_mins = int(round(tdiff.total_seconds() / 60))
   return tdiff_mins


# Termination filters prompt
tag_pattern = input('Enter image tag pattern: ')
termination_age = int(input('Enter termination age (in minutes): '))
imgs_to_save = int(input('Enter a number of images to preserve: '))
time_fmt = '%Y-%m-%d %H:%M:%S'
client = docker.from_env()

for i in client.images.list():
   # Image match markers collection
   repo_name_match_i = match_repo_name(tag_pattern, i.tags)
   # Image age calculation
   tdiff_mins_i = time_diff(i, time_fmt)

   # Image deletion approval
   deletion_approval = False
   img_amount = 0
   for j in client.images.list():
      # Image match markers collection
      repo_name_match_j = match_repo_name(tag_pattern, j.tags)
      # Image age calculation
      tdiff_mins_j = time_diff(j, time_fmt)
      # Comparison
      if len(repo_name_match_j) > 0 and tdiff_mins_i >= tdiff_mins_j:
         img_amount += 1
         if img_amount > imgs_to_save :
            deletion_approval = True
         else:
            deletion_approval = False

   # Image deletion
   image_id = (str(i.id).replace("sha256:", ""))
   if tdiff_mins_i >= termination_age and deletion_approval and len(repo_name_match_i) > 0 :
      client.images.remove(image=image_id, force=True)
      print("Deleted: " + str(i.tags)  + " " + str(i.id))

