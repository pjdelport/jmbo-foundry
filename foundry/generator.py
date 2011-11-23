import random

from django.conf import settings

from generate import IMAGES

def generate():
    objects = [
        {
            "model": "photologue.PhotoSize",
            "fields": {
                "name": "listing_promo_basic",
                "height": 200,
                "pre_cache": True,
            }
        },
        {
            "model": "photologue.PhotoSize",
            "fields": {
                "name": "listing_vertical_basic",
                "width": 50,
                "height": 50,
                "pre_cache": True,
                "crop": True,
            }
        },
        {
            "model": "foundry.Link",
            "fields": {
                "title": "News",
                "category": {
                    "model": "category.Category",
                    "fields": {
                        "title": "News",
                        "slug": "news",
                    },
                },
            },
        },
        {
            "model": "foundry.NavbarLinkPosition",
            "fields": {
                "position": 1,
                "link": {
                    "model": "foundry.Link",
                    "fields": {
                        "title": "Home",
                        "view_name": "home",
                    },
                },
                "preferences": {
                    "model": "preferences.NavbarPreferences",
                    "fields": {
                        "sites": settings.SITE_ID,
                    },
                },
            },
        },
        {
            "model": "foundry.NavbarLinkPosition",
            "fields": {
                "position": 2,
                "link": {
                    "model": "foundry.Link",
                    "fields": {
                        "title": "News"
                    },
                },
                "preferences": {
                    "model": "preferences.NavbarPreferences",
                    "fields": {
                        "sites": settings.SITE_ID,
                    },
                },
            },
        },
        {
            "model": "foundry.MenuLinkPosition",
            "fields": {
                "position": 1,
                "link": {
                    "model": "foundry.Link",
                    "fields": {
                        "title": "Home",
                        "view_name": "home",
                    },
                },
                "preferences": {
                    "model": "preferences.MenuPreferences",
                    "fields": {
                        "sites": settings.SITE_ID,
                    },
                },
            },
        },
        {
            "model": "foundry.MenuLinkPosition",
            "fields": {
                "position": 2,
                "link": {
                    "model": "foundry.Link",
                    "fields": {
                        "title": "News"
                    },
                },
                "preferences": {
                    "model": "preferences.MenuPreferences",
                    "fields": {
                        "sites": settings.SITE_ID,
                    },
                },
            },
        },
    ] 

    for i in range(1, 14):
        objects.append({
            "model": "post.Post",
            "fields": {
                "title": "News Post %s" % i,
                "description": "News Post %s %s long description." % (i, 'very ' * 50),
                "content": "News Post %s <b>%s</b> long safe content." % (i, 'very ' * 100),
                "state": "published",
                "sites": settings.SITE_ID,
                "image": random.sample(IMAGES, 1)[0],
                "categories": [
                    {
                        "model": "category.Category",
                        "fields": {
                            "title": "News",
                            "slug": "news",
                        }
                    },
                ],
                "primary_category": {
                    "model": "category.Category",
                    "fields": {
                        "slug": "news",
                    },
                },
            },
        })

    objects.append({
        "model": "foundry.PageBlock",
        "fields": {
            "title": "Promos",
            "style": "Promo",
            "position": 1,
            "count": "3",
            "content": [
                { 
                    "model": "post.Post",
                    "fields": {
                        "title": "News Post 1",
                    },
                },
            ],
            "preferences": {
                "model": "preferences.PageBlockPreferences",
                "fields": {
                    "sites": settings.SITE_ID,
                },
            },
        },
    })

    objects.append({
        "model": "foundry.PageBlock",
        "fields": {
            "title": "Updates",
            "style": "Listing",
            "count": 3,
            "position": 2,
            "preferences": {
                "model": "preferences.PageBlockPreferences",
                "fields": {
                    "sites": settings.SITE_ID,
                },
            },
        },
    })
    
    objects.append({
        "model": "jmbo.Pin",
        "fields": {
            "category": {
                "model": "category.Category",
                "fields": {
                    "slug": "news",
                },
            },
            "content": {
                "model": "post.Post",
                "fields": {
                    "title": "News Post 7",
                },
            },
        },
    })

    return objects
