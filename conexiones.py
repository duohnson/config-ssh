import subprocess as sp
import datos_ as dt

class AbrirOpciones:
    def __init__(self):
        self.controlador = True

    def opciones(self):
        while self.controlador:
            opcion = input(
                f"--| Sistema de Conexiones SSH |--"
                f"\n[1] Conexión SSH - Mantener terminal abierta."
                f"\n[2] Extraer valor HTOP."
                f"\nIngresando el valor: \n"
            )

            if opcion == "1":
                sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}"])
                self.controlador = False
            elif opcion == "2":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "top -b -n 1"],
                capture_output=True,
                text=True
                )
                print("Datos del servidor:")
                print(clave.stdout)
            elif opcion == "0":
                print("Cerrado.")
                self.controlador = False
            else:
                print ("Opción invalida, favor usar un número apropiado.")

arrancar = AbrirOpciones()
arrancar.opciones()
