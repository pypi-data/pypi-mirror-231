'''
File: names.py
Author: Michael Lucky
Date: September 22, 2023
Description: Module to abstract the names used in the company_scraper project, this will allow for easier logic within the scraper and data handling. This module will be used as an interface for pulling company names and all associated alias's associated with them. This allows for separate data governance maintenance on a single module that can be used across the entire project without touching the logic of the scraper.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

# ONLY CHANGE THIS IF THERE IS AN UPDATE TO THE NAMES OF A COMPANY OR BRAND. URL CHANGES SHOULD BE DONE IN THE URLS MODULE 

def agency_names() -> dict[str, list[str]]:

    # currently used for testing purposes

    # name used within the data warehouse as the key and all alias's used to scrape data as the values
    return {
        'webfx': {
            'linkedin' : ['webfxinc'],
            'goodfirms' : ['webfx'],
            'sortlist' : ['webfx'],
            'other' : ['web fx', 'web-fx', 'WebFx', 'Web Fx'],
        },
        'smartsites': {
            'linkedin' : ['smartsites'],
            'goodfirms' : ['smartsites'],
            'sortlist' : ['smartsites'],
            'other' : ['smart sites', 'smart-sites', 'SmartSites', 'Smart Sites'],
        },
    }

def brand_names() -> dict[str, list[str]]:

    # currently used for testing purposes

    # name used within the data warehouse as the key and all alias's used to scrape data as the values
    return {
        'webfx': {
            'linkedin' : ['webfxinc'],
            'goodfirms' : ['webfx'],
            'sortlist' : ['webfx'],
            'other' : ['web fx', 'web-fx', 'WebFx', 'Web Fx'],
        },
        'smartsites': {
            'linkedin' : ['smartsites'],
            'goodfirms' : ['smartsites'],
            'sortlist' : ['smartsites'],
            'other' : ['smart sites', 'smart-sites', 'SmartSites', 'Smart Sites'],
        },
    }