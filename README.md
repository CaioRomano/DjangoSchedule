# 🗓️ Django Schedules App

Um site desenvolvido com **Django** que permite aos usuários criarem suas próprias agendas (**schedules**) de forma privada e segura.  
Cada usuário pode se registrar, fazer login/logout, criar schedules e incluir **imagens e conteúdo formatado** diretamente nos schedules utilizando uma extensão chamada **TinyMCE** que se integra ao Django.  

🔒 **Importante:** cada schedule é visível **apenas para o seu criador**. Nenhum usuário pode visualizar os schedules de outros usuários.

---

## 🚀 Funcionalidades

- Registro de novos usuários
- Login e Logout
- Criação de **schedules**
- Editor de texto rico com **TinyMCE** integrado com django para inserir imagens e formatações
- Upload de imagens nos schedules
- Apenas o criador de um schedule pode visualizá-lo

---

## 📦 Pré-requisitos

- Python 3.x
- Django 4.x ou superior
- TinyMCE (via `django-tinymce`)
- Virtualenv (recomendado)
- Banco de dados SQLite (padrão do Django)

---

## ⚙️ Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
2. **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
4. **Execute as migrações:**
    ```bash
    python manage.py migrate
5. **Inicie o server local do django:**
    ```bash
    python manage.py runserver
6. **Acesse em:**
    ```bash
    http://localhost:8000

## Integração com TinyMCE

O projeto utiliza o django-tinymce para enriquecer a criação e edição de schedules.
Graças ao TinyMCE, é possível:

 - Inserir texto formatado (negrito, itálico, listas, títulos, etc.)

 - Inserir links e imagens diretamente no conteúdo

 - Melhorar a experiência do usuário ao criar schedules

## 🛠 Tecnologias Utilizadas
 - Python
 - Django
 - django-tinymce
 - SQLite
 - HTML5, CSS3
