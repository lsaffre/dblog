======
README
======

This is a project template for getting started with Luc's developer
blog. See `Start your own developer blog
<http://noi.lino-framework.org/team/devblog.html>`_ for an
introducton.

Installation:

- Make a clone of this project into some directory of your choice. For
  example::

    $ cd ~/projects
    $ git clone https://github.com/lsaffre/dblog.git blog

  This will create a directory `~/projects/blog` with all necessary
  files.

  Note that we explicitly specified the argument "blog" to the ``git``
  command.  This is your *internal project name*. It is not visible to
  the outside. Don't use "dblog" because one day you might become
  maintainer of the project template itself (whose internal name would
  then be "dblog").  See `Project management using atelier
  <http://noi.lino-framework.org/team/projects.html>`_ for more
  details.

- Install the ``atelier`` Python package::  

    $ pip install atelier

- Edit the following files (replace at least "John Doe" by your name):

  - `~/projects/blog/docs/conf.py`
  - `~/projects/blog/docs/index.rst`

- Create a file :file:`~/.fabricrc` with this content::

    blog_root = /home/johndoe/projects/blog/docs
    blogref_url = http://johndoe.lino-framework.org
    docs_rsync_dest = johndoe@lino-framework.org:~/public_html/%s
    editor_command = vim
    # editor_command = emacsclient -n
    # editor_command = /path/to/pycharm-community-3.4.1/bin/pycharm.sh


To start blogging::

    $ cd ~/projects/blog
    $ fab blog

To build your docs::

    $ fab bd

To see your built doctree::

    $ firefox docs/.build/index.html

To publish your docs::

    $ fab pd

Before this last step can work, you need to configure where your blog
is to be published. 

You need an SSH account on some public server. For example
`john@doe.org`.  And that web server must be configured to serve
`/home/john/public_html/blog_docs` to the outside.  For example if
you want your blog to be visible under `http://www.doe.org` you
point your browser's "/" location to `public_html/blog_docs`.

As a Lino contributor you'll get a free account on
`lino-framework.org`, just ask for it.

