# * Only works for Powershell at the moment

import subprocess, sys
import argparse

# Configure command line arguments
parser = argparse.ArgumentParser(description='Data Scraper command line interface!')
parser.add_argument("--location")
parser.add_argument("--search_terms")

# Parse command line arguments into python variables
args = parser.parse_args()
location = args.location
search_terms = args.search_terms

# Run powershell script with command line vars
p = subprocess.Popen(["powershell.exe", 
                        ".\\yp",
                        "-location", location,
                        "-search_terms", search_terms],
                        stdout=sys.stdout)
p.communicate()

