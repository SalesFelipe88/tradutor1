from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='pt', target='en')
tradutor_1 = GoogleTranslator(source='en', target='pt')

while True:
    escolha_linguagem = input('Escolha a linguagem do seu texto original: para Português digite (p), para Inglês digite (e), ou digite "sair" para encerrar: ')
    
    if escolha_linguagem.lower() == 'sair':
        print("Encerrando o programa...")
        break  # Sai do loop e encerra o programa
    
    texto = input('Digite seu texto: ')
    
    if escolha_linguagem.lower() == 'p':
        traducao = tradutor.translate(texto)
        print(f"Tradução para Inglês: {traducao}")
    elif escolha_linguagem.lower() == 'e':
        traducao_1 = tradutor_1.translate(texto)
        print(f"Tradução para Português: {traducao_1}")
    else:
        print('Não é uma opção válida. Tente novamente.')



