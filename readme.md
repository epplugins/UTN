<table>
<tr style="border:none;">
<td style="border:none;"><a href="https://fra.utn.edu.ar/">
<image src="https://raw.githubusercontent.com/epplugins/UTN/main/assets/img/logoUTN-500.svg"  width="100">
</a></td>
<td style="border:none;">Universidad Tecnológica Nacional<br>Facultad Regional Avellaneda<br>Argentina
</td>
</tr>
</table>

# Física 2


Acceso al material a través del sitio web:
https://epplugins.github.io/UTN/

Invitación - presentación.

Disclaimer:

<!--

Optica con matplotlib:
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/epplugins/UTN/blob/main/optica/matplotlib-optica_diferencia-de-CO.ipynb)

Optica con plotly:
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/epplugins/UTN/blob/main/optica/op_diferencia-de-CO.ipynb)



Potencial Eléctrico de cargas puntuales
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/epplugins/UTN/blob/main/electromagnetismo/em_potencial.ipynb)

Potencial Eléctrico con conductores
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/epplugins/UTN/blob/main/electromagnetismo/em_poisson_solver.ipynb)
 -->

## Entorno

Instalar miniconda y crear el entorno:
```bash
conda create -n utn -c conda-forge python=3.11
```

```bash
conda install -n utn -c conda-forge jupyter
```

Para crear gráficos interactivos dentro de VS Code:
```bash
conda install -n utn -c conda-forge ipympl
```

```bash
conda install -n utn -c conda-forge matplotlib numpy pandas scikit-image tikzplotlib sympy
```

No instalado aun:
Animations:
```bash
conda install -n utn -c conda-forge manim
```


No instalado:
```bash
conda install -n utn -c plotly plotly
```

Puede ser necesario agregar esto en settings.json:
[(https://github.com/microsoft/vscode-jupyter/wiki/IPyWidget-Support-in-VS-Code-Python)](https://github.com/microsoft/vscode-jupyter/wiki/IPyWidget-Support-in-VS-Code-Python)
```bash
"jupyter.widgetScriptSources": ["jsdelivr.com", "unpkg.com"],
```


