import clases

persona = clases.Persona()
persona.setNombre("Adrián")
persona.setApellidos("Cañuelo")
persona.setAltura("1'74 cm")
persona.setEdad("30 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("----------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Adrián")
informatico.setApellidos("Cañuelo")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)
print("----------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Pedro")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())