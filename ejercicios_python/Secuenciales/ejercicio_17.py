#Calcular la hora de llegada
 

h_partida = int(input("Hora de salida: "))
m_partida = int(input("Minutos de salida: "))
s_partida = int(input("Segundos de salida: "))
t_viaje = int(input("Tiempo de viaje en segundos: "))


seg_inicial = (h_partida * 3600) + (m_partida * 60) + s_partida
seg_final = seg_inicial + t_viaje


h_llegada = seg_final // 3600
m_llegada = (seg_final % 3600) // 60
s_llegada = (seg_final % 3600) % 60

print(f"Hora de llegada: {h_llegada:02}:{m_llegada:02}:{s_llegada:02}")