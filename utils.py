import os
import time
import csv

def getdate():
  '''
  yyyy-mm-dd format date text
  '''
  gmt = time.gmtime()
  return '-'.join(list(map(str, [gmt.tm_year, gmt.tm_mon, gmt.tm_mday])))


def esc(text):
  '''
  Escape unicode text
  '''
  return str(text).encode('unicode_escape')


def writelog(task, tags):
  '''
  Save log of task run
  '''
  with open('runs.log', 'a+', newline='\n', encoding='utf-8') as f:
    f.write('{} {} {}'.format(time.ctime(), task, str(tags)))


def fopen(tag, **kwargs):
  '''
  Open a file for the tag
  '''
  cwd = os.getcwd()
  datefmt = getdate()
  fn = '{}{}{}'.format(str(int(time.time())), tag, '.csv') # filename
  filepath = os.path.join('data', datefmt, fn)

  # get file and path names
  dn = os.path.join(cwd, os.path.dirname(filepath))

  if not os.path.exists(dn):
    os.makedirs(dn)

  # write header for new file
  if not os.path.exists(filepath):
    with open(filepath, 'w+', **kwargs) as f:
      writer = csv.writer(f)
      writer.writerow(['tweet_text', 'tweet_id', 'user_name', 'user_screen_name', 'user_location', 'user_description', 'user_follower_count', 'user_friends_count', 'user_listed_count', 'user_statuses_count', 'user_favourites_count', 'user_verified', 'user_default_profile_image', 'user_default_profile', 'user_protected', 'user_created_at'])

  # return the file
  return open(filepath, 'a+', **kwargs)
