def EscribirCentrado(texto):
  """
  Esta función centra un texto en una pantalla de 80 columnas y lo subraya.

  Args:
    texto: El texto a centrar y subrayar.
  """

  # Calcula el número de espacios necesarios para centrar
  espacios = 80 - len(texto) // 2

  # Imprime los espacios, el texto y el subrayado
  print(" " * espacios + texto)
  print(" " * espacios + "=" * len(texto))

# Ejemplo de uso:
texto = "Este es un mensaje centrado y subrayado"
EscribirCentrado(texto)