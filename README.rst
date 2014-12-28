======
README
======

This is a project template for getting started with Luc's developer
blog.

Installation:

- Make a clone of this project into some directory of your choice. For
  example::

    $ cd
    $ git clone https://github.com/lsaffre/dblog.git myblog

  This will create a directory `~/myblog` with all necessary files.

  Note that we explicitly specified the argument "myblog" to the
  :command:`git` command.  This is your *internal* project name. It is
  not visible to the outside. Don't use "dblog" because one day
  you might become maintainer of the project template itself
  (whose internal name would then be "dblog").

- Install the ``atelier`` Python package::  

    $ pip install atelier

- Edit the following files (replace at least "John Doe" by your name):

  - `~/myblog/docs/conf.py`
  - `~/myblog/docs/index.rst`

- Make sure that your `VISUAL` or `EDITOR` environment variable is set.

To start blogging::

    $ cd ~/myblog
    $ fab blog

To build your docs and see them::

    $ cd ~/myblog
    $ fab bd
    $ firefox ~/myblog/.build/index.html

To publish your docs::

    $ cd ~/myblog
    $ fab pd

Before this last step can work, you need to configure where your blog
is to be published.

- you need an SSH account on some public server. For example
  `john@doe.org`.

- Create a file `~/myblog/fabfile.py` with this content::

    env.docs_rsync_dest = 'john@doe.org:~/public_html/%s'
    env.blogref_url = "http://www.doe.org"

  More about this in the `atelier documentation
  <http://atelier.lino-framework.org/dev/api/atelier.fablib.html#configuration-files>`_.

- And then you must configure the web server at `doe.org` to serve
  `/home/john/public_html/myblog_docs` to the outside.  For example if
  you want your blog to be visible under `http://www.doe.org` you
  point your browser's "/" location to `public_html/myblog_docs`.

