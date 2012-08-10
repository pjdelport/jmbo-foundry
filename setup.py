from setuptools import setup, find_packages

setup(
    name='jmbo-foundry',
    version='0.2.0.a',
    description='Jmbo foundry behaviour/templates app.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-foundry',
    packages = find_packages(),
    dependency_links = ['http://github.com/praekelt/django-category/tarball/master#egg=django-category',
                        'http://github.com/shaunsephton/django-ckeditor/tarball/master#egg=django-ckeditor',
                        'http://github.com/praekelt/django-export/tarball/master#egg=django-export',
                        'http://github.com/praekelt/django-generate/tarball/master#egg=django-generate',
                        'http://github.com/praekelt/django-gizmo/tarball/master#egg=django-gizmo',
                        'http://github.com/praekelt/django-googlesearch/tarball/master#egg=django-googlesearch',
                        'http://github.com/praekelt/django-likes/tarball/master#egg=django-likes',
                        'http://github.com/praekelt/django-object-tools/tarball/master#egg=django-object-tools',
                        'http://github.com/praekelt/django-photologue/tarball/master#egg=django-photologue',
                        'http://github.com/praekelt/django-preferences/tarball/master#egg=django-preferences',
                        'http://github.com/praekelt/django-publisher/tarball/master#egg=django-publisher',
                        'http://github.com/praekelt/django-recaptcha/tarball/master#egg=django-recaptcha',
                        'http://github.com/praekelt/django-richcomments/tarball/master#egg=django-richcomments',
                        'http://github.com/praekelt/django-section/tarball/master#egg=django-section',
                        'http://github.com/praekelt/django-setuptest-recipe/tarball/master#egg=django-setuptest-recipe',
                        'http://github.com/praekelt/django-simple-autocomplete/tarball/master#egg=django-simple-autocomplete',
                        'http://github.com/praekelt/django-snippetscream/tarball/master#egg=django-snippetscream',
                        'http://github.com/praekelt/jmbo/tarball/master#egg=jmbo',
                        'http://github.com/praekelt/jmbo-analytics/tarball/master#egg=jmbo-analytics',
                        'http://github.com/praekelt/jmbo-banner/tarball/master#egg=jmbo-banner',
                        'http://github.com/praekelt/jmbo-calendar/tarball/master#egg=jmbo-calendar',
                        'http://github.com/praekelt/jmbo-chart/tarball/master#egg=jmbo-chart',
                        'http://github.com/praekelt/jmbo-competition/tarball/master#egg=jmbo-competition',
                        'http://github.com/praekelt/jmbo-contact/tarball/master#egg=jmbo-contact',
                        'http://github.com/praekelt/jmbo-event/tarball/master#egg=jmbo-event',
                        'http://github.com/praekelt/jmbo-gallery/tarball/master#egg=jmbo-gallery',
                        'http://github.com/praekelt/jmbo-foundry/tarball/master#egg=jmbo-foundry',
                        'http://github.com/praekelt/jmbo-music/tarball/master#egg=jmbo-music',
                        'http://github.com/praekelt/jmbo-paste/tarball/master#egg=jmbo-paste',
                        'http://github.com/praekelt/jmbo-poll/tarball/master#egg=jmbo-poll',
                        'http://github.com/praekelt/jmbo-post/tarball/master#egg=jmbo-post',
                        'http://github.com/praekelt/jmbo-show/tarball/master#egg=jmbo-show',
                        'http://github.com/praekelt/jmbo-social/tarball/master#egg=jmbo-social',
                        'http://github.com/unomena/jmbo-friends/tarball/0.1.0#egg=jmbo-friends-0.1.0',
                        'http://github.com/unomena/jmbo-activity/tarball/0.0.6#egg=jmbo-activity-0.0.6',
                        ],
    install_requires = [
        # todo: eliminate dependencies handled by apps themselves
        'django-geckoboard',
        'django-analytics',
        'django-section',
        'jmbo-gallery',
        'django-googlesearch',
        'jmbo-music',
        'django-export',
        'django-snippetscream',
        'django-generate',
        'jmbo-calendar',
        'jmbo',
        'jmbo-chart',
        'django-recaptcha',
        'django-secretballot',
        'django-richcomments',
        'django-publisher',
        'django-category',
        'jmbo-post',
        'django-likes',
        'django-gizmo',
        'django-object-tools',
#        'django-registration',    # Not used at all.
        'jmbo-show',
        'jmbo-event',
        'django-preferences',
        'jmbo-banner',
        'jmbo-competition',
        'django-ckeditor',
        'jmbo-contact',
        'jmbo-poll',
        'django-debug-toolbar',
        'django-simple-autocomplete',
        'django-pagination',
        'south',
        'BeautifulSoup',
        'django_compressor',
        'jmbo_analytics',
        'jmbo-friends==0.1.0',
        'jmbo-activity==0.0.6',
        'jellyfish'
    ],
    include_package_data=True,
    tests_require=[
        'django-setuptest',
    ],
    test_suite="setuptest.SetupTestSuite",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
