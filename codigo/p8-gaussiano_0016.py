print("Johan Paulo Aros Reveles NC 0016")

import cv2

# Cargar la imagen
imagen = cv2.imread("jirafa.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original Johan NC 0016", imagen)
cv2.imshow("Imagen suavizada - Filtro Gaussiano", imagen_suavizada)

# Guardar resultado
cv2.imwrite(
    "../resultados/jirafa.jpg",
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/jirafa.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Johan Paulo Aros Reveles NC 0016")