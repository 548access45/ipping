import speedtest
import subprocess

# Fonction pour trouver l'adresse IP
def get_ip_address():
    process = subprocess.Popen(['hostname', '-I'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    ip_address = output.decode().strip()
    return ip_address

# Fonction pour trouver le ping
def get_ping():
    process = subprocess.Popen(['ping', 'google.com', '-n', '1'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    ping = output.decode().strip()
    return ping

# Fonction pour trouver le débit descendant et le débit montant
def get_speed():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    return download_speed, upload_speed

# Appeler les fonctions pour trouver l'adresse IP, le ping et les débits
ip_address = get_ip_address()
ping = get_ping()
download_speed, upload_speed = get_speed()

# Afficher les résultats
print("Adresse IP : ", ip_address)
print("Ping : ", ping)
print("Débit descendant : ", round(download_speed / 1000000, 2), "Mbps")
print("Débit montant : ", round(upload_speed / 1000000, 2), "Mbps")
