import socket
import os

def iniciar_servidor_udp():
    HOST = '127.0.0.1'
    PORTA = 4545
    
    # Garante que a pasta BD existe
    pasta_bd = "BD"
    os.makedirs(pasta_bd, exist_ok=True)
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
        servidor.bind((HOST, PORTA))
        print("Servidor UDP Ativo e aguardando arquivos...\n")
        
        # 1. Recebe o nome do arquivo enviado pelo cliente
        nome_arquivo_bytes, addr = servidor.recvfrom(1024)
        nome_arquivo = nome_arquivo_bytes.decode('utf-8')
        print(f"Nome do arquivo recebido: {nome_arquivo}")
        
        # 2. Recebe os dados binários da imagem
        dados_imagem, _ = servidor.recvfrom(65535)
        print(f"Dados da imagem recebidos! Tamanho: {len(dados_imagem)} bytes")
        
        # 3. Define o caminho completo dentro da pasta BD mantendo o nome original
        caminho_completo = os.path.join(pasta_bd, nome_arquivo)
        
        # 4. Salva a imagem no disco
        with open(caminho_completo, "wb") as arquivo_imagem:
            arquivo_imagem.write(dados_imagem)
            
        print(f"Imagem salva com sucesso em: {caminho_completo}")
        
        # 5. Retorna o caminho da imagem salva para o cliente
        resposta = f"Caminho da imagem salvo: {caminho_completo}"
        servidor.sendto(resposta.encode('utf-8'), addr)

if __name__ == "__main__":
    try:
        iniciar_servidor_udp()
    except OSError as e:
        print(f"Erro: {e}")