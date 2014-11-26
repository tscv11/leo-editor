#@+leo-ver=5-thin
#@+node:maphew.20141126130213.2: * @file ../../setup.py
'''setup.py for leo

    Nov 2014: strip to bare minimum and rebuild using ONLY
    https://docs.python.org/2/distutils/setupscript.html 
    
    See if we can get all the way to end (painless `python setup.py install` and
    `pip install .` on all platforms) without having to leave standard library
    or leverage hacks.
'''
from distutils.core import setup
#@+others
#@-others
import leo.core.leoVersion
#long_description = get_long_description()

setup(
    name = 'leo',
    version = leo.core.leoVersion.version,
    author = "Edward K. Ream",
    author_email = 'edreamleo@gmail.com',
    url = 'http://leoeditor.com',
    license = 'MIT License',
    description = "Leo: Leonine Editor with Outlines", # becomes "Summary" in pkg-info
    #long_description = long_description,
    platforms = ['Linux','Windows','MacOS'],
    download_url = 'http://sourceforge.net/projects/leo/files/Leo/',
    requires = ['docutils'],
        # only include dependencies which can be installed by pip (so not PyQt or SIP)
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Text Editors',
        'Topic :: Text Processing',
    ],
    #zip_safe = False,
    entry_points = {
        'console_scripts': ['leoc = leo.core.runLeo:run'],
        'gui_scripts' : ['leo = leo.core.runLeo:run'],
    }
)

#@@language python
#@@tabwidth -4
#@-leo
