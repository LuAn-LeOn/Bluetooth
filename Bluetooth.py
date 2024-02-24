# -*- coding: utf-8 -*-

import subprocess
import bluetooth

def buscar_dispositivos_bluetooth():
    dispositivos = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    if dispositivos:
        print("Dispositivos Bluetooth encontrados:")
        for i, dispositivo in enumerate(dispositivos):
            print(f"{i+1}. Nombre: {dispositivo[1]}, Dirección: {dispositivo[0]}")
        return dispositivos
    else:
        print("No se encontraron dispositivos Bluetooth cercanos.")
        return None

def apagar_bluetooth(direccion_mac):
    try:
        subprocess.run(['rfkill', 'block', 'bluetooth', '-r', direccion_mac], check=True)
        print("Bluetooth apagado.")
    except subprocess.CalledProcessError:
        print("Error al apagar el Bluetooth. Asegúrate de tener permisos suficientes o de que la dirección MAC sea válida.")

if __name__ == "__main__":
    dispositivos = buscar_dispositivos_bluetooth()
    if dispositivos:
        seleccion = int(input("Seleccione el número del dispositivo que desea controlar: "))
        if 1 <= seleccion <= len(dispositivos):
            direccion_mac = dispositivos[seleccion - 1][0]
            print(f"Ha seleccionado el dispositivo con la dirección MAC: {direccion_mac}")
            confirmacion = input("¿Está seguro que desea apagar el Bluetooth de este dispositivo? (s/n): ")
            if confirmacion.lower() == "s":
                apagar_bluetooth(direccion_mac)
            else:
                print("Operación cancelada.")
        else:
            print("Selección inválida.")