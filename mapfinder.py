import folium
import webbrowser

# Format 
# map = folium.Map(location = [cordinates of the place]).save("x.html")


# For example : Cordinates of Mumbai = [19.0760, 72.8777 in the square brackets
map_cordinates = folium.Map(location = [19.0760, 72.8777]).save("x.html")
webbrowser.open("x.html")