import threading


SALDO_INICIAL = 20
MONTO_COMPRA = 15
PERSONAS = ("Ana", "Luis")


def ejecutar_sin_lock():
    print("\n=== Dos compras sin Lock ===")
    cuenta = {"saldo": SALDO_INICIAL}
    compras_aprobadas = []
    barrera = threading.Barrier(len(PERSONAS))

    def pagar(nombre):
        saldo_visto = cuenta["saldo"]
        print(f"{nombre} revisa el presupuesto: {saldo_visto} USD")

        # La barrera hace que ambos hilos lean el saldo antes de descontarlo.
        barrera.wait()

        if saldo_visto >= MONTO_COMPRA:
            cuenta["saldo"] = saldo_visto - MONTO_COMPRA
            compras_aprobadas.append(nombre)
            print(f"{nombre}: compra de {MONTO_COMPRA} USD aprobada")
        else:
            print(f"{nombre}: compra rechazada por falta de saldo")

    hilos = [
        threading.Thread(target=pagar, args=(nombre,))
        for nombre in PERSONAS
    ]

    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    total_aprobado = len(compras_aprobadas) * MONTO_COMPRA
    saldo_esperado = SALDO_INICIAL - total_aprobado
    print(f"Compras aprobadas: {len(compras_aprobadas)}")
    print(f"Saldo registrado: {cuenta['saldo']} USD")
    print(f"Saldo según las compras aprobadas: {saldo_esperado} USD")


def ejecutar_con_lock():
    print("\n=== Dos compras con Lock ===")
    cuenta = {"saldo": SALDO_INICIAL}
    compras_aprobadas = []
    lock_saldo = threading.Lock()

    def pagar(nombre):
        # La consulta y el descuento forman una sola sección protegida.
        with lock_saldo:
            saldo_visto = cuenta["saldo"]
            print(f"{nombre} revisa el presupuesto: {saldo_visto} USD")

            if saldo_visto >= MONTO_COMPRA:
                cuenta["saldo"] = saldo_visto - MONTO_COMPRA
                compras_aprobadas.append(nombre)
                print(f"{nombre}: compra de {MONTO_COMPRA} USD aprobada")
            else:
                print(f"{nombre}: compra rechazada por falta de saldo")

    hilos = [
        threading.Thread(target=pagar, args=(nombre,))
        for nombre in PERSONAS
    ]

    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    print(f"Compras aprobadas: {len(compras_aprobadas)}")
    print(f"Saldo final: {cuenta['saldo']} USD")


def main():
    print("Presupuesto familiar compartido: 20 USD")
    print("Ana y Luis intentan comprar algo que cuesta 15 USD cada uno.")
    ejecutar_sin_lock()
    ejecutar_con_lock()


if __name__ == "__main__":
    main()
