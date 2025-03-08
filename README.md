# Catavento com Pygame e OpenGL

Este projeto implementa um catavento interativo usando **Python**, **Pygame** e **PyOpenGL**. O usuário pode girar as pás do catavento utilizando o teclado.

## 🎮 Controles
- Pressione **A** para girar no sentido **anti-horário**
- Pressione **D** para girar no sentido **horário**

## 🛠️ Pré-requisitos
Antes de rodar o código, instale as dependências necessárias:
```sh
pip install pygame PyOpenGL PyOpenGL_accelerate
```

## 🚀 Como Rodar
1. **Baixe ou clone o projeto**
2. **Execute o script Python**:
   ```sh
   python catavento.py
   ```

## 📝 Explicação do Código
O código segue a seguinte estrutura:
1. **Inicializa o Pygame e OpenGL**
   - Configura a janela e a projeção ortográfica
2. **Desenha o Catavento**
   - O eixo central é desenhado como um retângulo cinza
   - As pás são triângulos coloridos que giram conforme o usuário pressiona A ou D
3. **Loop Principal**
   - Captura eventos do teclado
   - Atualiza a tela e aplica a rotação nas pás

## 📌 Observações
- Caso o código não rode, verifique se as bibliotecas foram instaladas corretamente.
- Para fechar a janela, pressione o botão de fechar ou **ALT+F4**.

---
Projeto desenvolvido para a matéria de Computação Gráfica ministrada pelo professor Marcelo Costa Oliveira, para a prática de OpenGL  com Python.

