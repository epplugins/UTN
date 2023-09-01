
Potencial Eléctrico
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/epplugins/UTN/blob/main/electromagnetismo/em_potencial.ipynb)



## Entorno

Instalar miniconda y crear el entorno:
```bash
conda create -n utn -c conda-forge python=3.11
```

```bash
conda install -n utn -c conda-forge matplotlib numpy pandas jupyter_server scikit-image tikzplotlib
```

Para crear gráficos interactivos dentro de VS Code:
```bash
conda install -n utn -c conda-forge ipympl
```

```bash
conda install -n utn -c plotly plotly
```

Puede ser necesario agregar esto en settings.json:
[(https://github.com/microsoft/vscode-jupyter/wiki/IPyWidget-Support-in-VS-Code-Python)](https://github.com/microsoft/vscode-jupyter/wiki/IPyWidget-Support-in-VS-Code-Python)
```bash
"jupyter.widgetScriptSources": ["jsdelivr.com", "unpkg.com"],
```
