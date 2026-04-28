# EchoFeed AI

**EchoFeed AI** é um protótipo acadêmico sobre **Streaming & Social + IA Generativa**.

Ele simula como algoritmos de redes sociais podem transformar um mesmo tema em feeds diferentes para dois perfis de usuário. O objetivo é demonstrar bolhas algorítmicas, hiperpersonalização, pressão de retenção e mudança de enquadramento emocional.

## Stack

- Python
- Flask
- Jinja2
- CSS puro
- OpenRouter no backend
- JSON Schema para resposta estruturada
- Sem JavaScript próprio no frontend

## O que o app faz

1. O usuário escolhe um tema.
2. O usuário define dois perfis.
3. O app envia o prompt para a OpenRouter usando uma chave escondida no servidor.
4. O modelo retorna JSON estruturado.
5. O backend valida o JSON.
6. A interface exibe dois feeds lado a lado e um diagnóstico comparativo.

## Como rodar localmente

### 1. Criar ambiente virtual

No Windows, dentro da pasta do projeto:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar a chave OpenRouter

Copie `.env.example` para `.env`:

```bash
copy .env.example .env
```

No macOS/Linux:

```bash
cp .env.example .env
```

Edite o `.env` e coloque sua chave:

```env
OPENROUTER_API_KEY=sk-or-sua-chave-aqui
OPENROUTER_MODEL=openrouter/free
```

**Nunca envie o arquivo `.env` para o GitHub.** Ele já está protegido pelo `.gitignore`.

### 4. Rodar o servidor

```bash
python app.py
```

Abra no navegador:

```text
http://localhost:5000
```

## Como usar

- Clique em **Gerar com IA** para chamar a OpenRouter.
- Clique em **Carregar demo offline** para apresentar sem depender de API.

## Como a resposta vem no formato certo

O projeto usa uma defesa em camadas:

1. `response_format` com `json_schema`.
2. `strict: true` no schema.
3. `provider.require_parameters: true` para exigir suporte aos parâmetros.
4. Plugin `response-healing` para reduzir problemas comuns de JSON.
5. Validação no backend com `jsonschema`.
6. Retry com `json_object` se o modelo não aceitar JSON Schema.
7. Demo offline como plano B.

## Deploy recomendado: Render

Este projeto não é ideal para GitHub Pages, porque GitHub Pages não roda backend. Como a chave da OpenRouter precisa ficar escondida, use Render, Railway, Fly.io ou outro host com backend Python.

### Passo a passo no Render

1. Suba este projeto para o GitHub.
2. Entre no Render.
3. Clique em **New > Web Service**.
4. Conecte o repositório do GitHub.
5. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Em **Environment Variables**, adicione:
   - `OPENROUTER_API_KEY`: sua chave real
   - `OPENROUTER_MODEL`: `openrouter/free`
   - `OPENROUTER_APP_TITLE`: `EchoFeed`
7. Faça o deploy.
8. Use o link público gerado pelo Render como entrega.

## Como colocar no GitHub pelo terminal

```bash
git init
git branch -M main
git add .
git commit -m "Add EchoFeed AI prototype"
git remote add origin https://github.com/SEU-USUARIO/echofeed-ai.git
git push -u origin main
```

## Entrega da atividade

Use o texto do arquivo `ENTREGA.md` e substitua o campo do link pelo link do deploy.

## Correção de riscos numéricos

Nesta versão, a IA gera os textos, mas o backend recalcula os números de risco com uma heurística do próprio experimento. Isso evita casos em que um modelo gratuito retorna `0%` para bolha, manipulação ou polarização mesmo quando o próprio texto mostra uma bolha clara.

A pontuação considera:

- intensidade da personalização;
- objetivo dominante do algoritmo;
- plataforma simulada;
- divergência de vocabulário entre os dois feeds;
- presença de termos de medo, urgência, certeza absoluta e identidade de grupo.

## Erro HTTP 429 no OpenRouter

HTTP 429 significa limite temporário do modelo/provedor gratuito. O app agora tenta novamente algumas vezes. Também existe a variável opcional `OPENROUTER_MODEL_FALLBACKS`, onde você pode listar outros modelos separados por vírgula.

O botão **Carregar demo offline** continua sendo o plano B para apresentação.

## Motor de pontuação v3

A IA gera os textos, mas o backend recalcula todos os números. A matriz de pontuação considera todas as opções do formulário:

- Plataformas: TikTok, Instagram Reels, YouTube Shorts, LinkedIn e Feed misto.
- Intensidade: Baixa, Média e Alta.
- Objetivo: Informar, Reter atenção, Engajar, Vender e Polarizar.

Isso evita resultados incoerentes como uma simulação com personalização alta e objetivo de polarização aparecer com 0% de risco.
