import socket
import os

def iniciar_cliente_udp():
    HOST = '127.0.0.1'
    PORTA = 4545
    
    # Nome do arquivo da imagem que você quer enviar
    nome_arquivo = "teste.jpg" # ou "teste.png" dependendo do seu arquivo
    
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado na pasta.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
            print(f"Enviando nome do arquivo: {nome_arquivo}")
            # 1. Envia o nome do arquivo primeiro
            cliente.sendto(nome_arquivo.encode('utf-8'), (HOST, PORTA))
            
            # 2. Lê os bytes da imagem
            with open(nome_arquivo, "rb") as arquivo:
                dados_imagem = arquivo.read()
                
            print(f"Enviando dados da imagem ({len(dados_imagem)} bytes)...")
            # 3. Envia os bytes da imagem em seguida
            cliente.sendto(dados_imagem, (HOST, PORTA))
            
            print("Envio concluído! Aguardando resposta do servidor...")
            
            # 4. Aguarda o retorno do servidor com o caminho salvo
            resposta, addr = cliente.recvfrom(1024)
            
            print("\n--- Resposta do Servidor ---")
            print(resposta.decode('utf-8'))
            print(f"IP do Servidor: {addr[0]}")
            print(f"Porta: {addr[1]}")
            
    except OSError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    iniciar_cliente_udp()