"""Prints a detailed list of all resources that are registered, including the modules, where they have been registered."""

from __future__ import print_function
import bob.bio.base
import os

def resources():

  import argparse
  parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--details", '-d', nargs = '+',
                      choices = ('d', 'database', 'p', 'preprocessor', 'e', 'extractor', 'a', 'algorithm', 'g', 'grid'),
                      default = ('d', 'p', 'e', 'a', 'g'),
                      help = "Select the resource types that should be listed.")

  args = parser.parse_args()

  if 'd' in args.details or 'database' in args.details:
    print ("\nList of registered databases:")
    print (bob.bio.base.list_resources('database'))

  if 'p' in args.details or 'preprocessor' in args.details:
    print ("\nList of registered preprocessors:")
    print (bob.bio.base.list_resources('preprocessor'))

  if 'e' in args.details or 'extractor' in args.details:
    print ("\nList of registered extractors:")
    print (bob.bio.base.list_resources('extractor'))

  if 'a' in args.details or 'algorithm' in args.details:
    print ("\nList of registered algorithms:")
    print (bob.bio.base.list_resources('algorithm'))

  if 'g' in args.details or 'grid' in args.details:
    print ("\nList of registered grid configurations:")
    print (bob.bio.base.list_resources('grid'))

  print()

def databases():
  import argparse
  database_replacement = "%s/.bob_bio_databases.txt" % os.environ["HOME"]

  parser = argparse.ArgumentParser(description="Prints a list of directories for registered databases", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-D', '--database-directories-file', metavar = 'FILE', default = database_replacement, help = 'The file, where database directories are stored (to avoid changing the database configurations)')

  args = parser.parse_args()

  # get registered databases
  databases = bob.bio.base.utils.resources.database_directories(replacements=args.database_directories_file)

  # print directories for all databases
  for d in sorted(databases):
    print ("\n%s:" % d)

    print ("Original data: %s" % databases[d][0])
    if len(databases[d]) > 1:
      print ("Annotations: %s" % databases[d][1])
