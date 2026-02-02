# Projeto Galactic Codex API

## 🗺️ Roadmap

Este documento rastreia o progresso do desafio técnico para a vaga de Backend Python.
**Prazo Final:** 05/02
**Stack:** Python 3.12, Flask, GCP (Cloud Functions, API Gateway), Pydantic.

### 📅 Fase 1: Fundação & Configuração (Dia 30/01)
- [X] Configurar ambiente local com `uv` (`uv init --python 3.12`).
- [X] Definir estrutura de pastas do projeto (Clean Architecture simplificada).
- [X] Configurar Git e criar repositório remoto.
- [X] Instalar dependências iniciais (`flask`, `requests`, `pydantic`).

### 📅 Fase 2: Core da Aplicação & Regras de Negócio (Dia 31/01)
- [X] **Models (Pydantic)**: Criar schemas para validar dados de entrada e saída (Personagens, Filmes, etc.).
- [X] **Service Layer**: Implementar lógica de consumo da SWAPI (com tratamento de erros).
- [X] **Controller/Routes**: Criar endpoints Flask (`/characters`, `/films`, etc.).
- [ ] Implementar **Filtros**: Permitir busca por nome, ID ou características.
- [ ] Implementar **Ordenação**: Lógica para ordenar resultados (Ex: Alfabética, Ano de lançamento).

### 📅 Fase 3: Infraestrutura Nuvem - GCP (Dia 01/02)
- [X] Criar projeto no Google Cloud Platform.
- [X] Habilitar APIs necessárias (Cloud Functions, Cloud Build, API Gateway).
- [X] Instalar e configurar `gcloud CLI` localmente.
- [X] Ajustar código para compatibilidade com Cloud Functions (Entrypoint).
- [X] **Deploy v1**: Realizar o primeiro deploy da Cloud Function.
- [X] Testar função rodando na nuvem (URL direta).

### 📅 Fase 4: Profissionalização & Segurança (Dia 02/02)
- [X] Configurar **API Gateway** no GCP.
- [X] Configurar rotas do Gateway apontando para a Cloud Function.
- [X] Implementar segurança básica (API Key ou validação de Header).
- [X] Verificar Logs no GCP (Stackdriver/Cloud Logging).

### 📅 Fase 5: Qualidade & Testes (Dia 03/02)
- [ ] Configurar `pytest`.
- [ ] Criar **Testes Unitários** para os Services (usando Mocks para a SWAPI).
- [ ] Criar **Testes de Integração** para os Endpoints.
- [ ] Rodar Linter/Formatter (`ruff` ou `black`) para garantir PEP-8.

### 📅 Fase 6: Documentação & Entrega (Dia 04/02)
- [ ] Escrever **README.md** técnico detalhado (instalação, uso, decisões).
- [ ] Criar **Diagrama de Arquitetura** (Mermaid.js ou imagem).
- [ ] Revisão final dos critérios de aceite.
- [ ] Commit final e envio do link do repositório.

---

### 🌟 Funcionalidades Extras (Diferenciais)
- [ ] Cache (Redis ou simples in-memory se possível no contexto serverless) para evitar chamadas repetidas à SWAPI.
- [ ] Endpoint de correlação (ex: Dado um filme, trazer detalhes completos dos personagens).