======
README
======

This is a project template for getting started with your developer
blog.  See `Start your own developer blog
<http://www.lino-framework.org/dev/devblog.html>`_ for an
introducton.

Installation:

- Make a clone of this project into some directory of your choice. For
  example::

    $ cd ~/projects
    $ git clone https://github.com/lsaffre/dblog.git blog

  This will create a directory `~/projects/blog` with all necessary
  files. On the Linux command line ``~`` is shorthand for your home
  directory.

  Note that we explicitly specified your *local project name* "blog"
  as an argument to the ``git`` command.  This name is not visible to
  the outside.  Without that argument, ``git`` would use `dblog` as
  local project name, which would be suboptimal since "dblog" is just
  the name of this template project.  See `Setting up your work
  environment <http://www.lino-framework.org/dev/env.html>`_ for more
  details.

  Activate your `virtualenv
  <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_ and
  install the ``atelier`` Python package::

    $ pip install atelier

- Edit the following files and replace at least "John Doe" by your
  name:

  - ``~/projects/blog/docs/conf.py``
  - ``~/projects/blog/docs/index.rst``

- Create a file named ``.invoke.py`` in your home directory with the
  following content (replacing ``john`` by your local username,
  ``johndoe`` by the name of your SSH account)::

    blog_root = '/home/john/projects/blog/docs'
    blogref_url = 'http://johndoe.lino-framework.org'
    docs_rsync_dest = 'johndoe@lino-framework.org:~/public_html/%s'
    editor_command = 'vim'
    # editor_command = 'emacsclient -n'
    # editor_command = '/path/to/pycharm/bin/pycharm.sh'


To start blogging::

    $ cd ~/projects/blog
    $ inv blog

To build your docs locally::

    $ inv bd

To see your built doctree::

    $ firefox docs/.build/index.html

To publish your docs::

    $ inv pd

Before this last step can work, you need to configure where your blog
is to be published. 

You need an SSH account on some public server. For example
`john@doe.org`.  And that web server must be configured to serve
`/home/john/public_html/blog_docs` to the outside.  For example if
you want your blog to be visible under `http://www.doe.org` you
point your browser's "/" location to `public_html/blog_docs`.

As a Lino contributor you'll get a free account on
`lino-framework.org`, just ask for it.

