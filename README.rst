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

- Make sure that your `VISUAL` or `EDITOR` environment variable is set.

To start blogging::

    $ cd ~/projects/blog
    $ fab blog

To build your docs and see them::

    $ cd ~/projects/blog
    $ fab bd
    $ firefox docs/.build/index.html

To publish your docs::

    $ cd ~/projects/blog
    $ fab pd

Before this last step can work, you need to configure where your blog
is to be published.

- you need an SSH account on some public server. For example
  `john@doe.org`.

- Modify the file `~/projects/blog/fabfile.py`, adding this content::

    env.docs_rsync_dest = 'john@doe.org:~/public_html/%s'
    env.blogref_url = "http://www.doe.org"

  More about this in the `atelier documentation
  <http://atelier.lino-framework.org/dev/api/atelier.fablib.html#configuration-files>`_.

- And then you must configure the web server at `doe.org` to serve
  `/home/john/public_html/blog_docs` to the outside.  For example if
  you want your blog to be visible under `http://www.doe.org` you
  point your browser's "/" location to `public_html/blog_docs`.

