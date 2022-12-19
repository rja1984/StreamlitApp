Autor: Ricardo J. Agosta

# Esta aplicación web se desarrolló para poder agregar y ir actualizando una lista de productos con sus costos de forma eficiente, y para que haya un mejor entendimiento de los datos que se van a ir visualizaando en una gráfica, además se va a poder exportar o descargar la tabla a la computadora local.
# Si bién esta app esta terminada, se podría decir que esto es un prototipo, se podría mejorar y implementar para otros temas específicos.

* import streamlit as st #pip install streamlit
* import pandas as pd #pip install pandas
* import streamlit.components.v1 as components # Para html
* from st_aggrid import AgGrid, JsCode #pip install streamlit-aggrid
* from st_aggrid.grid_options_builder import GridOptionsBuilder
