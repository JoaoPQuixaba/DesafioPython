config_filename = "config.txt"

def ler_estados(config_filename):
    try:
        with open(config_filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            estados = content.split(';')
            estados = [estado.strip() for estado in estados if estado.strip()]
        return estados
    except FileNotFoundError:
        print(f"Erro: O arquivo {config_filename} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo {config_filename}: {e}")
        return []

def main():
    estados = ler_estados(config_filename)
    if estados:
        print("Lista de estados:")
        for estado in estados:
            print(estado)
    else:
        print("Nenhum estado encontrado ou erro ao ler o arquivo.")

if __name__ == "__main__":
    main()
