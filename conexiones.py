import subprocess as sp
import datos_ as dt
import getpass as gp

# libreria getpass para no ver la contraseña escrita

pass_temp = gp.getpass("Si desea utilizar comandos SUDO, ingrese el acceso root temporalmente, de lo contrario ingresar solo Enter.\n")

class AbrirOpciones:
    def __init__(self):
        self.controlador = True
        # controlador se mantiene en True para el bucle

    def opciones(self):

        while self.controlador:
            opcion = input(
                f"--| Sistema de Conexiones SSH |--"
                f"\n[1] Conexión SSH - Mantener terminal abierta."
                f"\n[2] Extraer valor HTOP."
                f"\n[3] Extraer sesiónes activas y ultimos logeos."
                f"\n[4] Revisar cambios en Usuarios y Contraseñas. [SUDO]"
                f"\n[5] Revisar cambios en SUDO y permisos Administradores. [SUDO]"
                f"\n[6] Revisar cambios en /etc y /sshd. [SUDO]"
                f"\n[7] Revisar cambios en Archivos borrados. [SUDO]"
                f"\n[8] Revisar cambios en Permisos recientes. [SUDO]"
                f"\n[9] Revisar cambios en Sofware instalado/gestionado. [SUDO]"
                f"\n[0] Salir."
                f"\nIngresando el valor: \n"
            )

            if opcion == "1":
                sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}"])
                self.controlador = False
            elif opcion == "2":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "top -b -n 1; exit"],
                capture_output=True,
                # muestra salida de comando, no en terminal
                text=True
                # text hace que stdout si se vea en texto y no en bytes
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
            elif opcion == "3":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "w; last -n 20 -i; exit"],
                capture_output=True,
                text=True
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
                print(clave.stderr)
            elif opcion == "4":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "sudo -S -p '' ausearch -k identity -i; exit"],
                input=pass_temp + "\n",
                text=True,
                capture_output=True
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
                print(clave.stderr)
            elif opcion == "5":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "sudo -S -p '' ausearch -k sudo_changes -i; exit"],
                input=pass_temp + "\n",
                text=True,
                capture_output=True
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
                print(clave.stderr)
            elif opcion == "6":
                # sh -c es lo mismo que "abrir un shell y ejecutar la siguiente cadena como comando", se encierra entre ' lo que se ocupa ejecutar '
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "sudo -S -p '' sh -c 'ausearch -k ssh_config -i; ausearch -k etc_changes -i; exit'"],
                input=pass_temp + "\n",
                text=True,
                capture_output=True
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
                print(clave.stderr)
            elif opcion == "7":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "sudo -S -p '' ausearch -k identity -i"],
                input=pass_temp + "\n",
                text=True,
                capture_output=True
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
            elif opcion == "8":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "sudo -S -p '' ausearch -k identity -i"],
                input=pass_temp + "\n",
                text=True,
                capture_output=True
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
            elif opcion == "9":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "sudo -S -p '' ausearch -k identity -i"],
                input=pass_temp + "\n",
                text=True,
                capture_output=True
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
            elif opcion == "10":
                clave = sp.run(["ssh", f"{dt.N_USUARIO}@{dt.N_IP}", "sudo -S -p '' ausearch -k identity -i"],
                input=pass_temp + "\n",
                text=True,
                capture_output=True
                )
                print("\nDatos del servidor:\n")
                print(clave.stdout)
            elif opcion == "0":
                print("\nCerrado.\n")
                self.controlador = False
            else:
                print ("\nOpción invalida, favor usar un número apropiado.\n")

arrancar = AbrirOpciones()
arrancar.opciones()
