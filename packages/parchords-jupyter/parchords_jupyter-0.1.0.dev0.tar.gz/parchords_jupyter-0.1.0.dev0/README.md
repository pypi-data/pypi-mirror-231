
# parchords-jupyter

jupyter widget with parallel coords that enables interactive sonification

## Installation

You can install using `pip`:

```bash
pip install parchords_jupyter
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```bash
jupyter nbextension enable --py [--sys-prefix|--user|--system] parchords_jupyter
```

## Development Installation

Create a dev environment:
```bash
conda create -n parchords_jupyter-dev -c conda-forge nodejs python jupyterlab
conda activate parchords_jupyter-dev
```
or
```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install -U pip setuptools
pip install 'jupyterlab>=3.6.5,<4' jupyter-packaging # nodejs
```

For a development installation the version of the python package `jupyterlab`
and the npm package `@jupyterlab/builder` need to match.

Install the python. This will also build the TS package.
```bash
pip install -e ".[test, examples]"
```

When developing your extensions, you need to manually enable your extensions with the
notebook / lab frontend. For lab, this is done by the command:

```
jupyter labextension develop --overwrite .
npm run build
```

For classic notebook, you need to run:

```
jupyter nbextension install --sys-prefix --symlink --overwrite --py parchords_jupyter
jupyter nbextension enable --sys-prefix --py parchords_jupyter
```

Note that the `--symlink` flag doesn't work on Windows, so you will here have to run
the `install` command every time that you rebuild your extension. For certain installations
you might also need another flag instead of `--sys-prefix`, but we won't cover the meaning
of those flags here.

### How to see your changes
#### Typescript:
If you use JupyterLab to develop then you can watch the source directory and run JupyterLab at the same time in different
terminals to watch for changes in the extension's source and automatically rebuild the widget.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
npm run watch
# Run JupyterLab in another terminal
jupyter lab
```

After a change wait for the build to finish and then refresh your browser and the changes should take effect.

#### Python:
If you make a change to the python code then you will need to restart the notebook kernel to have it take effect.

## Updating the version

To update the version, install tbump and use it to bump the version.
By default it will also create a tag.

```bash
pip install tbump
tbump <new-version>
```
