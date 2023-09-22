
Developer install
=================


To install a developer version of parchords_jupyter, you will first need to clone
the repository::

    git clone https://github.com/fhstp/parchords-jupyter
    cd parchords-jupyter

Next, install it with a develop install using pip::

    pip install -e .


If you are planning on working on the JS/frontend code, you should also do
a link installation of the extension::

    jupyter nbextension install [--sys-prefix / --user / --system] --symlink --py parchords_jupyter

    jupyter nbextension enable [--sys-prefix / --user / --system] --py parchords_jupyter

with the `appropriate flag`_. Or, if you are using Jupyterlab::

    jupyter labextension install .


.. links

.. _`appropriate flag`: https://jupyter-notebook.readthedocs.io/en/stable/extending/frontend_extensions.html#installing-and-enabling-extensions
