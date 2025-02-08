O código automatiza a interação com uma interface gráfica de um ERP, utilizando coordenadas de elementos na tela e imagens para localizá-los. Ele lê uma planilha Excel contendo códigos de veículos, e para cada código, 
realiza as seguintes ações: preenche o campo de código, verifica e desmarca checkboxes específicos, navega entre abas e salva as alterações. Após processar todos os códigos, o código exibe uma mensagem de conclusão. 
A automação é feita com a biblioteca pyautogui para controle de mouse e teclado, pandas para manipulação de dados, e tkinter para exibir a mensagem final.
