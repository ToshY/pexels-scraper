# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 00:50:01 2020

@author: ToshY

Simple scraper with Pexels API
"""

import os
import math
import argparse
import requests
from pathlib import Path

def page_arguments(nmin,nmax):
    """ Limit nargs for argument parser """
    
    class PageArgsCheck(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            vl = len(values)
            if 3<vl<1 or vl==2:
                msg='Argument "{f}" requires either {nmin} or {nmax} arguments'.format(
                    f=self.dest,nmin=nmin,nmax=nmax)
                raise parser.error(msg)
            setattr(args, self.dest, values)
    return PageArgsCheck

def exist_dir():
    """ Check for existing directory """
    
    class DirCheck(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            p = Path(values)
            if not p.exists():
                msg='Argument "{f} denoting the specificed directory "{user_dir}" does not exist. Please check again'.format(
                    f=self.dest,user_dir=values)
                raise parser.error(msg)
            setattr(args, self.dest, values)
    return DirCheck

def api_check():
    """ Check for existing directory """
    
    class ApiKeyCheck(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            if len(values) != 56:
                msg='Argument "{f} denoting the specified API key has an invalid length of "{l}", should be "{g}"'.format(
                    f=self.dest,l=len(values),g=56)
                raise parser.error(msg)
            setattr(args, self.dest, values)
    return ApiKeyCheck

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('true', 't', 'yes', 'y', '1'):
        return True
    elif v.lower() in ('false', 'f', 'no', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
    
def args():
    """ Input arguments parser """
    
    parser = argparse.ArgumentParser(description=__doc__)
    
    parser.add_argument('-k','--key',type=str, required=True,
        help="Your Pexels API key",
    )
    parser.add_argument('-c','--cat', type=str, required=True,
        help="The name of the category you want images from",
    )
    parser.add_argument('-d','--save_dir', type=str, required=True, 
        action=exist_dir(), help="The save directory for the images",
    )
    parser.add_argument('-p','--pages', nargs="+", type=int, required=True,
        action=page_arguments(1,3), help="The start page, end page and per page OR -1 for all",
    )
    parser.add_argument('-v','--verbose',type=str2bool, nargs='?', const=True,
        default=True, help="Verbose mode. Printing when page is completely downloaded.",
    )
    
    args = parser.parse_args()
    
    return args
    
def main(api_key, cat, save_dir, pages, verbose=True):
    """ Get Pexels images """
    
    base = 'https://api.pexels.com/v1/search'
    headers = {'authorization': api_key}
    
    # Single request first for total results
    params = (('query', cat),('page', '1'),('per_page', '1'))
    
    total = (requests.get(base, headers=headers, params=params).json())['total_results']
    
    # Check pages
    if len(pages) == 1 and pages[0] == -1:
        start_page = 1
        per_page = 80
        end_page = math.ceil( total / per_page )
    else:
        start_page = pages[0]
        if pages[2] > 80:
            per_page = 80
        else:
            per_page = pages[2]
        end_page = pages[1]
        total = (end_page-start_page+1)*per_page
    
    # Loop over pages
    for i in range(start_page, end_page+1):
        # Query parameters
        params = (('query', cat),('page', str(i)),('per_page', str(per_page)))
        
        response = (requests.get(base, headers=headers, params=params).json())['photos']
        
        # If no more photos, break loop and give feedback
        if len(response) == 0:
            break
    
        # Loop over photos and save 
        for j in response:
            # Image URL
            dl = j['src']['original']
            
            # Filename
            name = str(j['id']) + '.' + dl.rsplit('.',1)[-1]
            
            # Get image and write
            response = requests.get(dl)
            if response.status_code == 200:
                with open(save_dir+os.sep+name, 'wb') as f:
                    f.write(response.content)
        
        if verbose:
            print('>> Page {sp} out of {ep} complete.'.format(sp=i,ep=(end_page)))
    
    if verbose:
        print('>> Download complete for images of category "{category}" (total={amount}).'.format(amount=total,category=cat))
                
if __name__ == "__main__":
    """ Main """
        
    # Arguments
    user_args = args()
    
    # Get the images
    main(user_args.key, user_args.cat, user_args.save_dir, user_args.pages, user_args.verbose)
