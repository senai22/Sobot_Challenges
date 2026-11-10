#!/usr/bin/python3
"""
Solis Robot - SoBot
Desafio Básico - Sequência de movimentos e cores dos LEDs.

Autores: Alexandre, Gabriel, Julio
Versão: 1.1
"""

from time import sleep
import serial

# Configuração da comunicação serial
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()

# Ativa os motores
usb.write(b"MT0 E1")
sleep(0.5)

# 1 - Avançar (Verde)
usb.write(b"LT E1 RD0 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(2)

# 2 - Esquerda (Azul) - Giro no próprio eixo
usb.write(b"LT E1 RD0 GR0 BL50")
sleep(0.2)
usb.write(b"MT0 E1 D90 L AT3950 DT3950 V10")
sleep(2)

# 3 - Avançar (Verde)
usb.write(b"LT E1 RD0 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(2)

# 4 - Direita (Amarelo) - Giro no próprio eixo
usb.write(b"LT E1 RD50 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(2)

# 5 - Avançar (Verde)
usb.write(b"LT E1 RD0 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(2)

# 6 - Para trás (Vermelho)
usb.write(b"LT E1 RD50 GR0 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D1000 B AT5000 DT5000 V10")
sleep(2)

# 7 - Direita (Amarelo) - Giro no próprio eixo
usb.write(b"LT E1 RD50 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(2)

# 8 - Avançar (Verde)
usb.write(b"LT E1 RD0 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(2)

# 9 - Direita (Amarelo) - Giro no próprio eixo
usb.write(b"LT E1 RD50 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(2)

# 10 - Avançar (Verde)
usb.write(b"LT E1 RD0 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(2)

# 11 - Direita (Amarelo) - Giro no próprio eixo
usb.write(b"LT E1 RD50 GR50 BL0")
sleep(0.2)
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(2)

# Desliga os LEDs
usb.write(b"LT E1 RD0 GR0 BL0")

# Desativa os motores
usb.write(b"MT0 E0")

# Fecha a comunicação serial
usb.close()

  # Fecha a comunicação serial
  usb.close()
