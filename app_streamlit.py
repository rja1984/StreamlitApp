import streamlit as st #pip install streamlit #local http://localhost:8501 o http://192.168.1.119:8501
import pandas as pd #pip install pandas
import streamlit.components.v1 as components # Para html
#import matplotlib.pylab as plt
#import numpy as np

from st_aggrid import AgGrid, JsCode #pip install streamlit-aggrid #Componente agGrid https://docs.streamlit.io/library/components
from st_aggrid.grid_options_builder import GridOptionsBuilder

cabecera = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
<div class="container-fluid p-3 bg-primary text-white text-center">
  <b><i><h1>Programa de Postitulación para Docentes.</i><b></h1>
  <i><h6>Python</i></h6>
</div>
"""
#<HR align="CENTER" size="2" width="400" color="Red" noshade>
components.html(cabecera)

# Dump any DataFrame
d = {'Productos':['Notebook', 'Tv Samsung 49', 'Parlante jbl'] ,'Cantidad': [1, 1, 1],'Precios': [70000, 100000, 60000]} #Productos que aparecen de manera predeterminada
df = pd.DataFrame(data = d)

# Dump as AgGrid Table
# AgGrid(df)

# JavaScript function 
# api.applyTransaction({add: [{}]})   # Esta linea termina la fila al final 
# Encontrar el índice de fila es importante para agregar una fila justo después del índice seleccionado
js_add_row = JsCode("""
function(e) {
    let api = e.api;
    let rowPos = e.rowIndex + 1; 
    api.applyTransaction({addIndex: rowPos, add: [{}]})    
};
"""     
)

# cellRenderer with a button component.
# Recursos:
# https://blog.ag-grid.com/cell-renderers-in-ag-grid-every-different-flavour/
# https://www.w3schools.com/css/css3_buttons.asp

#boton agregar y su diseño
cellRenderer_addButton = JsCode('''
    class BtnCellRenderer {
        init(params) {
            this.params = params;
            this.eGui = document.createElement('div');
            this.eGui.innerHTML = `
            <span>
                <style>
                .btn_add {
                    background-color: #00ff00; 
                    border: 2px solid black;
                    color: #D05732;
                    text-align: center;
                    display: inline-block;
                    font-size: 12px;
                    font-weight: bold;
                    height: 2em;
                    width: 10em;
                    border-radius: 12px;
                    padding: 0px;
                }
                </style>
                <button id='click-button' 
                    class="btn_add" 
                    >&#x2193; Agregar</button>
            </span>
        `;
        }
        getGui() {
            return this.eGui;
        }
    };
    ''')

# Dump como tabla AgGrid
# AgGrid(df)

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_default_column(editable=True)
gd.configure_column(field = '🔧',  
                    onCellClicked = js_add_row,
                    cellRenderer = cellRenderer_addButton,
                    lockPosition='left')
gridoptions = gd.build()

# Esta parte para actualizar la cuadrícula para que Streamlit no se vuelva a ejecutar en su totalidad
with st.form('Productos') as f:
    st.header('Listado de productos 📝')
    st.write("❗ Clic derecho dentro de la tabla para exportar")
    response = AgGrid(df,
                    gridOptions = gridoptions, 
                    editable=True,
                    allow_unsafe_jscode = True,
                    theme = 'balham',
                    height = 200,
                    fit_columns_on_grid_load = True) 

    st.form_submit_button("Confirmar lista ☑", type="primary")

# Dump
# hacemos un registro no estructurado del contenido                     
st.subheader("Lista actualizada 📖")
res = response['data']
st.table(res)

#Productos gráficados
grafica = """
<div align=left> <h1> Gráfica </h1>
</div>
<h1>  </h1> <img src="https://creatiabusiness.com/wp-content/uploads/2015/09/graficos-excel-scaled.jpg" width="700" height="60">
"""
components.html(grafica)

st.bar_chart(data=res, x = 'Productos', y = 'Precios')

pie = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
<div class="container-fluid p-1 bg-dark text-white text-center">
  <i><h6> Autor: Ricardo J. Agosta &copy; 2022 </i></h6>
</div>
"""
components.html(pie)