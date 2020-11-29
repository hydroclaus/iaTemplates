#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hello
"""
import sys
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import shutil


__author__ = "Claus Haslauer (mail@planetwater.org)"
__version__ = "$Revision: 1.2 $"
__date__ = datetime.date(2020,11,29)
__copyright__ = "Copyright (c) 2020 Claus Haslauer"
__license__ = "Python"

def generate_info_plist(BUNDLE_NAME, 
                        TEMPLATE_DIRECTORY,
                        TEMPLATE_CSS_FILE,
                        FOOTER_HEIGHT = 40,
                        HEADER_HEIGHT = 40,
                        TEMPLATE_DOCUMENT_FILE="document.html",
                        TEMPLATE_HEADER_FILE="header.html",
                        TEMPLATE_FOOTER_FILE="footer.html"):
    """
    generates a plist for an iA Writer template
    https://github.com/iainc/iA-Writer-Templates
    BUNDLE_NAME     CFBundleName    Template name shown in iA Writer.
    
    """
    
    plist_string=f"""<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
    	<key>CFBundleDevelopmentRegion</key>
    	<string>en</string>
    	<key>CFBundleInfoDictionaryVersion</key>
    	<string>6.0</string>
    	<key>CFBundleIdentifier</key>
    	<string>org.cph.journal_simple</string>
    	<key>CFBundleName</key>
    	<string>{BUNDLE_NAME}</string>
    	<key>CFBundleShortVersionString</key>
    	<string>1.0</string>
    	<key>CFBundleVersion</key>
    	<string>1</string>
    	<key>IATemplateDocumentFile</key>
    	<string>{TEMPLATE_DOCUMENT_FILE}</string>
    	<key>IATemplateTitleFile</key>
    	<string>title</string>
    	<key>IATemplateFooterFile</key>
    	<string>{TEMPLATE_FOOTER_FILE}</string>
    	<key>IATemplateFooterHeight</key>
    	<integer>{FOOTER_HEIGHT}</integer>
    	<key>IATemplateHeaderFile</key>
    	<string>{TEMPLATE_HEADER_FILE}</string>
    	<key>IATemplateHeaderHeight</key>
    	<integer>{HEADER_HEIGHT}</integer>
    	<key>IATemplateDescription</key>
    	<string>Claus Journal</string>
    	<key>IATemplateAuthor</key>
    	<string>cph</string>
    	<key>IATemplateAuthorURL</key>
    	<string>https://claus-haslauer.de</string>
    </dict>
    </plist>"""
    
    # WRITE DOCUMENT FILE
    write_document_file(TEMPLATE_DOCUMENT_FILE,
                        TEMPLATE_DIRECTORY,
                        TEMPLATE_CSS_FILE)
    
    # WRITE HEADER FILE
    write_header_file(TEMPLATE_HEADER_FILE,
                      TEMPLATE_DIRECTORY,
                      TEMPLATE_CSS_FILE)
                      
    # WRITE FOOTER FILE
    write_footer_file(TEMPLATE_FOOTER_FILE,
                      TEMPLATE_DIRECTORY,
                      TEMPLATE_CSS_FILE)
    # WRITE PLIST FILE
    file = open(TEMPLATE_DIRECTORY/"Contents"/"info.plist", "w")
    file.write(plist_string)
    file.close()
    print(f"\t done writing info.plist")
    


def write_document_file(TEMPLATE_DOCUMENT_FILE,
                        TEMPLATE_DIRECTORY,
                        TEMPLATE_CSS_FILE):
    """
    this writes the document file
    """
    
    document_file_string = f"""<!doctype html>
<html>
<head>
	<meta charset="UTF-8">
  <link rel="stylesheet" media="all" href="{TEMPLATE_CSS_FILE}"/>
  <meta name="viewport" content="initial-scale=1, viewport-fit=cover">
</head>
<body class="markdown-body" data-document>&nbsp;</body>
</html>"""

    file = open(TEMPLATE_DIRECTORY/"Contents"/"Resources"/TEMPLATE_DOCUMENT_FILE, "w")
    file.write(document_file_string)
    file.close()
    print(f"\t done writing {TEMPLATE_DOCUMENT_FILE}")
    

def write_header_file(TEMPLATE_HEADER_FILE,
                      TEMPLATE_DIRECTORY,
                      TEMPLATE_CSS_FILE):
    """
    """
    header_file_string = f"""<!doctype html>
<html>
<head>
	<meta charset="UTF-8" />
	<link rel="stylesheet" media="all" href="{TEMPLATE_CSS_FILE}" />
</head>
<body class="header">
<p><span data-title>&nbsp;</span>&nbsp;-&nbsp;<span data-date>&nbsp;</span></p>
</body>
</html>"""
    file = open(TEMPLATE_DIRECTORY/"Contents"/"Resources"/TEMPLATE_HEADER_FILE, "w")
    file.write(header_file_string)
    file.close()
    print(f"\t done writing {TEMPLATE_HEADER_FILE}")

def write_footer_file(TEMPLATE_FOOTER_FILE,
                      TEMPLATE_DIRECTORY,
                      TEMPLATE_CSS_FILE):
    """
    """
    print(f"TEMPLATE_CSS_FILE:{TEMPLATE_CSS_FILE}")
    footer_file_string = f"""<!doctype html>
<html>
<head>
	<meta charset="UTF-8" />
	<link rel="stylesheet" media="all" href="{TEMPLATE_CSS_FILE}"/>
</head>
<body>
<div class="footer">
<p><span data-page-number>&nbsp;</span>&nbsp;/&nbsp;<span data-page-count>&nbsp;</span></p>
</div>
</body>
</html>"""
    file = open(TEMPLATE_DIRECTORY/"Contents"/"Resources"/TEMPLATE_FOOTER_FILE, "w")
    file.write(footer_file_string)
    file.close()
    print(f"\t done writing {TEMPLATE_FOOTER_FILE}")



def main():
    
    TEMPLATE_NAME = "ia_cph_template_01.iatemplate"
    TEMPLATE_CSS_FILE = "ia_claus.css"

    
    ## CREATE THE FILE STRUCTURE
    # this is the path where the current python file lives
    MAIN_PATH = pathlib.Path(__file__).parent.absolute()
    
    # This is where the iA Template lives
    TEMPLATE_DIRECTORY = MAIN_PATH / TEMPLATE_NAME
    
    if os.path.exists(TEMPLATE_DIRECTORY):
        print("delete first")
        shutil.rmtree(TEMPLATE_DIRECTORY)

    os.mkdir(TEMPLATE_DIRECTORY)
    os.mkdir(TEMPLATE_DIRECTORY/"Contents")
    os.mkdir(TEMPLATE_DIRECTORY/"Contents"/"Resources")
    print("Basic folder structure generated")

    ## CREATE THE FILES
    # generate_info_plist generates 
    #   - info.plist
    #   - document.html
    #   - footer.html
    #   - header.html
    generate_info_plist(TEMPLATE_NAME[:-11],
                        TEMPLATE_DIRECTORY,
                        TEMPLATE_CSS_FILE)
    
    print("Done! Yay!")





if __name__ == '__main__':
    main()
    
    
    
