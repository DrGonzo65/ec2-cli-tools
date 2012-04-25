"""
EC2-CLI-Tools
=======

Helpful CLI utilities to filter and connect to EC2 instances.

ec2who:

::

    % ec2who nginx2
    # or
    % ec2who 10.13.12.205
    # or
    % ec2who ec2-204-236-192-148
    nginx2  i-d5236fbd      us-east-1c      10.13.12.205  ec2-204-236-192-148.compute-1.amazonaws.com

    % ec2who "nginx*"
    nginx1  i-d5236fbd      us-east-1c      10.13.12.205  ec2-204-236-192-148.compute-1.amazonaws.com
    nginx2  i-d5237fbd      us-east-1c      10.13.12.206  ec2-204-236-192-149.compute-1.amazonaws.com
    nginx3  i-d5238fbd      us-east-1c      10.13.12.207  ec2-204-236-192-150.compute-1.amazonaws.com

    % ec2who "10.*.207"
    nginx3  i-d5238fbd      us-east-1c      10.13.12.207  ec2-204-236-192-150.compute-1.amazonaws.com


ec2ssh and ec2host:

::

    % ec2ssh nginx2
    # equivalent to
    # ssh ubuntu@ec2-123-45-67-89.compute-1.amazonaws.com

    % ec2ssh root@appserver
    % ec2ssh deploy@nginx2 sudo restart nginx

    # accompanying ec2host script

    # w/o arg: prints all active instances
    % ec2host
    django1 ec2-123-45-67-89.compute-1.amazonaws.com
    django2 ec2-132-45-67-89.compute-1.amazonaws.com
    django3 ec2-231-45-67-89.compute-1.amazonaws.com

    # w/ arg: prints host name of matching instance
    % ec2host django2
    django2 ec2-132-45-67-89.compute-1.amazonaws.com


ec2getsnaps:

::
    % ec2getsnaps db1
    2012-01-28T02:04:18+0000 db1-xlog 100%


Links
`````

* `Original Project, ec2-ssh <http://github.com/Instagram/ec2-ssh>`
* `Instagram <http://instagram.com>`

Changelog
`````````

* 1.0 - initial release, addition of ec2who and migration of deprecated ec2ssh project
"""


from setuptools import setup


setup(
    name = "ec2-cli-tools",
    version = "1.2",
    author = "Shayne Sweeney & Tyler Smalley & Mike Krieger",
    author_email = "team@flippath.com",
    description = "Helpful CLI utilities for querying and connecting to EC2 instances",
    long_description = __doc__,
    license = "MIT",
    url = "https://github.com/FlipPath/ec2-cli-tools",
    keywords = ["amazon", "aws", "ec2", "ami", "ssh", "cloud", "boto"],
    install_requires = ['boto>=1.0'],
    scripts = ["bin/ec2who", "bin/ec2host", "bin/ec2ssh", "bin/ec2getsnaps"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities"
        ],
)
