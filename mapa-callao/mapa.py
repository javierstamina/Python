import folium

# Crea un objeto de mapa centrado en el Callao
callao_map = folium.Map(location=[-12.059, -77.128], zoom_start=12)

# Agrega un estilo azulado al mapa
folium.TileLayer('CartoDB positron',name="Light Map",control=False).add_to(callao_map)

# Agrega un marcador en el centro del mapa
folium.Marker([-12.059, -77.128]).add_to(callao_map)

# Muestra el mapa
callao_map