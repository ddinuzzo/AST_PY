"""Calcolo velocità oraria"""
distanza_percorsa = 4.1
miglio_terrestre = 1609.344
tempo_minuti = 21
tempo_secondi = 34
sec_totali = 21 * 60 + 34
m_s = distanza_percorsa * 1000 / sec_totali
print("Velocità:", round(m_s, 2), "m/s")
k_h = distanza_percorsa * 3600 / sec_totali
print("Velocità:", round(k_h, 2), "km/h")
m_h = ((distanza_percorsa * 1000 / miglio_terrestre) * 3600) / sec_totali
print("Velocità:", round(m_h, 2), "mph")
