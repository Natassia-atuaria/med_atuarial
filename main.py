import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração visual de SaaS moderno
st.set_page_config(page_title="MédicoGestão Atuarial", layout="wide")

# Barra Lateral de Navegação
with st.sidebar:
    st.title("🏥 MédicoGestão")
    st.markdown("---")
    aba = st.radio("Módulos", ["Dashboard Geral", "Gestão Contábil", "Gestão Atuarial","Plano tributação", "Planejamento financeiro"])
    st.markdown("---")
    st.info("Versão 1.0 - Natassia Atuária")

# Conteúdo de cada módulo
if aba == "Dashboard Geral":
    st.title("📊 Painel de Controle Executivo")
    
    # Cards de métricas
    m1, m2, m3 = st.columns(3)
    m1.metric("Médicos na Base", "50.000", "+12%")
    m2.metric("Receita Estimada", "R$ 1.5M", "Gestão Atuarial")
    m3.metric("Economia Fiscal", "R$ 320k", "IA")

    # Gráfico interativo
    st.subheader("Evolução Mensal")
    dados = pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr"],
        "Receita": [10000, 15000, 12000, 18000]
    })
    fig = px.line(dados, x="Mês", y="Receita", markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif aba == "IA Atuarial":
    st.title("📉 Inteligência de Risco e Reservas")
    st.write("Aqui você poderá inserir suas fórmulas de tabelas biométricas e projeções de longo prazo.")
    st.warning("Módulo em desenvolvimento: cálculos de reserva matemática ativos.")

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MédicoGestão IA", layout="wide")

# Menu Lateral
with st.sidebar:
    st.title("🏥 MédicoGestão")
    menu = st.radio("Navegação", ["Início", "Cálculo Atuarial", "IA Contábil"])

if menu == "Início":
    st.title("📊 Painel Executivo")
    c1, c2, c3 = st.columns(3)
    c1.metric("Médicos na Base", "50.000", "+12%")
    c2.metric("Receita Processada", "R$ 1.5M", "8%")
    c3.metric("Economia Gerada", "R$ 420k", "IA")
    
    # Gráfico de exemplo
    df = pd.DataFrame({"Mês": ["Jan", "Fev", "Mar"], "Valor": [10, 25, 20]})
    fig = px.line(df, x="Mês", y="Valor", title="Evolução de Contratos")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Cálculo Atuarial":
    st.title("📉 Inteligência de Risco")
    st.write("Módulo para projeção de reservas e tabelas biométricas.")

MédicoGestão - Sistema Contábil e CRM para Médicos

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-v16+-green)](https://nodejs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-v12+-blue)](https://www.postgresql.org/)
[![React](https://img.shields.io/badge/React-v18+-lightblue)](https://react.dev/)

> **Sistema SaaS completo para gestão de clientes, projetos e contabilidade de consultórios médicos**

## 🎯 Visão Geral

MédicoGestão é uma plataforma integrada que oferece:

- 👥 **CRM Profissional**: Pacientes, histórico, contatos
- 📋 **Gestão de Projetos**: Casos, procedimentos, timeline — fluxo completo para procedimentos clínicos (triagem, avaliação, agendamento, execução, pós-op e fechamento). Cada projeto suporta `etapas` (checklist), responsáveis, orçamento e vínculo com transações financeiras.
- 💰 **Financeiro**: Receitas, despesas, fluxo de caixa
- 📊 **Contabilidade**: Cálculos de impostos, regime tributário
- 🏥 **Empresa**: Dados da clínica/consultório

## ⚡ Características Principais

✅ Autenticação JWT com bcryptjs  
✅ Banco PostgreSQL com 6 modelos  
✅ 35+ endpoints REST funcionais  
✅ Frontend React responsivo  
✅ Dashboard com métricas em tempo real  
✅ Múltiplos regimes tributários  
✅ Validação de entrada completa  
✅ Arquitetura escalável e moderna  

## 🚀 Início Rápido em 5 Minutos

### 1. Instale os pré-requisitos
- Node.js 16+
- PostgreSQL 12+

### 2. Configure o Backend
```bash
cd backend
cp .env.example .env
npm install
npm run dev
```

### 3. Configure o Frontend (novo terminal)
```bash
cd frontend
cp .env.example .env
npm install
npm start
```

Acesse `http://localhost:3000` e cadastre-se!

**[→ Guia Completo de Início](./QUICKSTART.md)**

## 📚 Documentação Completa

| Documento | Conteúdo |
|-----------|----------|
| [QUICKSTART.md](./QUICKSTART.md) | Como instalar em 5 minutos |
| [README_SISTEMA.md](./README_SISTEMA.md) | Documentação técnica detalhada |
| [ARQUITETURA.md](./ARQUITETURA.md) | Diagramas e fluxos de dados |
| [DESENVOLVIMENTO.md](./DESENVOLVIMENTO.md) | Guia para contribuintes |
| [SUMARIO_EXECUTIVO.md](./SUMARIO_EXECUTIVO.md) | Visão de negócio e ROI |
| [ESTRUTURA_FINAL.md](./ESTRUTURA_FINAL.md) | Resumo técnico do projeto |

## 📊 O que foi Criado

### Backend - Node.js + Express
- ✅ 6 Modelos de Dados (User, Cliente, Projeto, Financeiro, Contabilidade, Empresa)
- ✅ 6 Controllers com CRUD completo
- ✅ 6 Rotas com mais de 35 endpoints
- ✅ Middleware de autenticação JWT
- ✅ Validação de dados
- ✅ Segurança com bcryptjs e Helmet

### Frontend - React
- ✅ 14 Páginas implementadas
- ✅ Dashboard com métricas
- ✅ Gestão de clientes (CRUD)
- ✅ Gestão de projetos
- ✅ Autenticação e roteamento protegido
- ✅ UI responsiva em Tailwind CSS

### Banco de Dados
- ✅ PostgreSQL com schema completo
- ✅ Relacionamentos complexos
- ✅ Índices para performance
- ✅ Migrations prontas

## 🔌 API REST (35+ Endpoints)

```
Autenticação: 3 endpoints
Clientes: 6 endpoints  
Projetos: 6 endpoints
Financeiro: 7 endpoints
Contabilidade: 5 endpoints
Empresa: 4 endpoints
```

[Ver todos os endpoints →](./README_SISTEMA.md#-api-endpoints)

## 🏗️ Stack Tecnológico

**Backend:**
- Node.js 16+
- Express 4.18 (framework)
- Sequelize 6.35 (ORM)
- PostgreSQL 12+ (database)
- JWT (autenticação)
- bcryptjs (criptografia)

**Frontend:**
- React 18.2
- React Router 6.20 (navegação)
- Axios (HTTP client)
- Tailwind CSS (styling)
- React Toastify (notificações)
- Recharts (gráficos)

## 🔐 Segurança

- ✅ Autenticação JWT com expiração
- ✅ Senhas com hash bcryptjs (10 rounds)
- ✅ CORS configurado
- ✅ Headers de segurança (Helmet)
- ✅ Validação de entrada
- ✅ Proteção de rotas privadas
- ✅ LGPD e CFM compliant

## 📈 Estatísticas do Projeto

| Métrica | Valor |
|---------|-------|
| Arquivos Criados | 40+ |
| Linhas Backend | ~1.500 |
| Linhas Frontend | ~800 |
| Linhas Documentação | ~2.000 |
| Endpoints API | 35+ |
| Componentes | 15+ |
| Modelos Dados | 6 |
| Controllers | 6 |
| Páginas | 14 |

## 🎯 Casos de Uso

### Para Médicos
- Gerenciar 100+ pacientes
- Acompanhar casos e procedimentos
- Registrar receitas e despesas
- Cumprir obrigações fiscais
- Analisar lucratividade por especialidade

### Para Contadores
- Gerar declarações contábeis
- Calcular impostos automático
- Acompanhar regimes tributários
- Exportar relatórios

### Para Gestores
- Dashboard com métricas principais
- Análise de pacientes mais lucrativos
- Planejar melhorias na clínica
- Monitorar saúde financeira

## 🚀 Próximas Funcionalidades

**Curto Prazo (1-2 meses):**
- [ ] Integração com Stripe/MercadoPago
- [ ] Testes unitários completos
- [ ] Geração de PDF para relatórios
- [ ] Upload de documentos (AWS S3)
- [ ] Autenticação 2FA

**Médio Prazo (2-4 meses):**
- [ ] App mobile (React Native)
- [ ] Agendamento de consultas
- [ ] Integração fiscal (NFe)
- [ ] Dashboard com gráficos avançados
- [ ] Backup automático

**Longo Prazo (4+ meses):**
- [ ] Telemedicina integrada
- [ ] Prontuário eletrônico completo
- [ ] Integração com laboratórios
- [ ] IA para análises preditivas
- [ ] Assinatura digital

## 📦 Estrutura de Diretórios

```
medico-gestao/
├── backend/
│   ├── src/
│   │   ├── controllers/   (6 controllers)
│   │   ├── models/        (6 models)
│   │   ├── routes/        (6 rotas)
│   │   ├── middleware/    (autenticação)
│   │   └── index.js       (servidor)
│   ├── package.json
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── pages/         (14 páginas)
│   │   ├── components/    (3 componentes)
│   │   ├── services/      (API client)
│   │   └── App.js
│   ├── package.json
│   └── .env.example
│
├── QUICKSTART.md          (5 minutos)
├── README_SISTEMA.md      (documentação)
├── ARQUITETURA.md         (diagramas)
├── DESENVOLVIMENTO.md     (para devs)
├── SUMARIO_EXECUTIVO.md   (negócio)
└── ESTRUTURA_FINAL.md     (resumo)
```

## 💼 Modelo de Negócio

**Planos SaaS Sugeridos:**

| Plano | Preço | Pacientes | Suporte |
|-------|-------|-----------|---------|
| Iniciante | R$ 400/mês | 30 | Email |
| Profissional | R$ 600/mês | 50 | Email |
| Empresa | R$ 1000/mês | Ilimitados | 24/7 |

## 📄 Licença

Proprietário - Todos os direitos reservados © 2026

## 👥 Contribuindo

1. Fork o projeto
2. Crie feature branch (`git checkout -b feature/Feature`)
3. Commit mudanças (`git commit -m 'Add Feature'`)
4. Push (`git push origin feature/Feature`)
5. Abra Pull Request

[Veja guia completo →](./DESENVOLVIMENTO.md#contribuindo)

## 📞 Suporte

- 📧 Email: suporte@medico-gestao.com
- 💬 Issues: GitHub Issues
- 📚 Docs: Veja a seção de documentação acima

## ✨ Status do Projeto

| Item | Status |
|------|--------|
| MVP Completo | ✅ |
| Documentação | ✅ |
| Testes | 🚧 |
| Deploy | 🚀 |

---

**Desenvolvido com ❤️ para médicos brasileiros**

Versão: 1.0.0 | Data: Fevereiro 2026 | [Visite a Documentação →](./ESTRUTURA_FINAL.md)

MédicoGestão - Sistema Contábil e CRM para Médicos

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-v16+-green)](https://nodejs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-v12+-blue)](https://www.postgresql.org/)
[![React](https://img.shields.io/badge/React-v18+-lightblue)](https://react.dev/)

> **Sistema SaaS completo para gestão de clientes, projetos e contabilidade de consultórios médicos**

## 🎯 Visão Geral

MédicoGestão é uma plataforma integrada que oferece:

- 👥 **CRM Profissional**: Pacientes, histórico, contatos
- 📋 **Gestão de Projetos**: Casos, procedimentos, timeline — fluxo completo para procedimentos clínicos (triagem, avaliação, agendamento, execução, pós-op e fechamento). Cada projeto suporta `etapas` (checklist), responsáveis, orçamento e vínculo com transações financeiras.
- 💰 **Financeiro**: Receitas, despesas, fluxo de caixa
- 📊 **Contabilidade**: Cálculos de impostos, regime tributário
- 🏥 **Empresa**: Dados da clínica/consultório

## ⚡ Características Principais

✅ Autenticação JWT com bcryptjs  
✅ Banco PostgreSQL com 6 modelos  
✅ 35+ endpoints REST funcionais  
✅ Frontend React responsivo  
✅ Dashboard com métricas em tempo real  
✅ Múltiplos regimes tributários  
✅ Validação de entrada completa  
✅ Arquitetura escalável e moderna  

## 🚀 Início Rápido em 5 Minutos

### 1. Instale os pré-requisitos
- Node.js 16+
- PostgreSQL 12+

### 2. Configure o Backend
```bash
cd backend
cp .env.example .env
npm install
npm run dev
```

### 3. Configure o Frontend (novo terminal)
```bash
cd frontend
cp .env.example .env
npm install
npm start
```

Acesse `http://localhost:3000` e cadastre-se!

**[→ Guia Completo de Início](./QUICKSTART.md)**

## 📚 Documentação Completa

| Documento | Conteúdo |
|-----------|----------|
| [QUICKSTART.md](./QUICKSTART.md) | Como instalar em 5 minutos |
| [README_SISTEMA.md](./README_SISTEMA.md) | Documentação técnica detalhada |
| [ARQUITETURA.md](./ARQUITETURA.md) | Diagramas e fluxos de dados |
| [DESENVOLVIMENTO.md](./DESENVOLVIMENTO.md) | Guia para contribuintes |
| [SUMARIO_EXECUTIVO.md](./SUMARIO_EXECUTIVO.md) | Visão de negócio e ROI |
| [ESTRUTURA_FINAL.md](./ESTRUTURA_FINAL.md) | Resumo técnico do projeto |

## 📊 O que foi Criado

### Backend - Node.js + Express
- ✅ 6 Modelos de Dados (User, Cliente, Projeto, Financeiro, Contabilidade, Empresa)
- ✅ 6 Controllers com CRUD completo
- ✅ 6 Rotas com mais de 35 endpoints
- ✅ Middleware de autenticação JWT
- ✅ Validação de dados
- ✅ Segurança com bcryptjs e Helmet

### Frontend - React
- ✅ 14 Páginas implementadas
- ✅ Dashboard com métricas
- ✅ Gestão de clientes (CRUD)
- ✅ Gestão de projetos
- ✅ Autenticação e roteamento protegido
- ✅ UI responsiva em Tailwind CSS

### Banco de Dados
- ✅ PostgreSQL com schema completo
- ✅ Relacionamentos complexos
- ✅ Índices para performance
- ✅ Migrations prontas

## 🔌 API REST (35+ Endpoints)

```
Autenticação: 3 endpoints
Clientes: 6 endpoints  
Projetos: 6 endpoints
Financeiro: 7 endpoints
Contabilidade: 5 endpoints
Empresa: 4 endpoints
```

[Ver todos os endpoints →](./README_SISTEMA.md#-api-endpoints)

## 🏗️ Stack Tecnológico

**Backend:**
- Node.js 16+
- Express 4.18 (framework)
- Sequelize 6.35 (ORM)
- PostgreSQL 12+ (database)
- JWT (autenticação)
- bcryptjs (criptografia)

**Frontend:**
- React 18.2
- React Router 6.20 (navegação)
- Axios (HTTP client)
- Tailwind CSS (styling)
- React Toastify (notificações)
- Recharts (gráficos)

## 🔐 Segurança

- ✅ Autenticação JWT com expiração
- ✅ Senhas com hash bcryptjs (10 rounds)
- ✅ CORS configurado
- ✅ Headers de segurança (Helmet)
- ✅ Validação de entrada
- ✅ Proteção de rotas privadas
- ✅ LGPD e CFM compliant

## 📈 Estatísticas do Projeto

| Métrica | Valor |
|---------|-------|
| Arquivos Criados | 40+ |
| Linhas Backend | ~1.500 |
| Linhas Frontend | ~800 |
| Linhas Documentação | ~2.000 |
| Endpoints API | 35+ |
| Componentes | 15+ |
| Modelos Dados | 6 |
| Controllers | 6 |
| Páginas | 14 |

## 🎯 Casos de Uso

### Para Médicos
- Gerenciar 100+ pacientes
- Acompanhar casos e procedimentos
- Registrar receitas e despesas
- Cumprir obrigações fiscais
- Analisar lucratividade por especialidade

### Para Contadores
- Gerar declarações contábeis
- Calcular impostos automático
- Acompanhar regimes tributários
- Exportar relatórios

### Para Gestores
- Dashboard com métricas principais
- Análise de pacientes mais lucrativos
- Planejar melhorias na clínica
- Monitorar saúde financeira

## 🚀 Próximas Funcionalidades

**Curto Prazo (1-2 meses):**
- [ ] Integração com Stripe/MercadoPago
- [ ] Testes unitários completos
- [ ] Geração de PDF para relatórios
- [ ] Upload de documentos (AWS S3)
- [ ] Autenticação 2FA

**Médio Prazo (2-4 meses):**
- [ ] App mobile (React Native)
- [ ] Agendamento de consultas
- [ ] Integração fiscal (NFe)
- [ ] Dashboard com gráficos avançados
- [ ] Backup automático

**Longo Prazo (4+ meses):**
- [ ] Telemedicina integrada
- [ ] Prontuário eletrônico completo
- [ ] Integração com laboratórios
- [ ] IA para análises preditivas
- [ ] Assinatura digital

## 📦 Estrutura de Diretórios

```
medico-gestao/
├── backend/
│   ├── src/
│   │   ├── controllers/   (6 controllers)
│   │   ├── models/        (6 models)
│   │   ├── routes/        (6 rotas)
│   │   ├── middleware/    (autenticação)
│   │   └── index.js       (servidor)
│   ├── package.json
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── pages/         (14 páginas)
│   │   ├── components/    (3 componentes)
│   │   ├── services/      (API client)
│   │   └── App.js
│   ├── package.json
│   └── .env.example
│
├── QUICKSTART.md          (5 minutos)
├── README_SISTEMA.md      (documentação)
├── ARQUITETURA.md         (diagramas)
├── DESENVOLVIMENTO.md     (para devs)
├── SUMARIO_EXECUTIVO.md   (negócio)
└── ESTRUTURA_FINAL.md     (resumo)
```

## 💼 Modelo de Negócio

**Planos SaaS Sugeridos:**

| Plano | Preço | Pacientes | Suporte |
|-------|-------|-----------|---------|
| Iniciante | R$ 400/mês | 30 | Email |
| Profissional | R$ 600/mês | 50 | Email |
| Empresa | R$ 1000/mês | Ilimitados | 24/7 |

## 📄 Licença

Proprietário - Todos os direitos reservados © 2026

## 👥 Contribuindo

1. Fork o projeto
2. Crie feature branch (`git checkout -b feature/Feature`)
3. Commit mudanças (`git commit -m 'Add Feature'`)
4. Push (`git push origin feature/Feature`)
5. Abra Pull Request

[Veja guia completo →](./DESENVOLVIMENTO.md#contribuindo)

## 📞 Suporte

- 📧 Email: natassiamcampos@usp.br
- 💬 Issues: GitHub Issues
- 📚 Docs: Veja a seção de documentação acima

## ✨ Status do Projeto

| Item | Status |
|------|--------|
| MVP Completo | ✅ |
| Documentação | ✅ |
| Testes | 🚧 |
| Deploy | 🚀 |

---

**Desenvolvido com ❤️ para médicos brasileiros**

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MédicoGestão IA", layout="wide")

# Menu Lateral
with st.sidebar:
    st.title("🏥 MédicoGestão")
    menu = st.radio("Navegação", ["Início", "Cálculo Atuarial", "IA Contábil"])

if menu == "Início":
    st.title("📊 Painel Executivo")
    c1, c2, c3 = st.columns(3)
    c1.metric("Médicos na Base", "50.000", "+12%")
    c2.metric("Receita Processada", "R$ 1.5M", "8%")
    c3.metric("Economia Gerada", "R$ 420k", "IA")
    
    # Gráfico de exemplo
    df = pd.DataFrame({"Mês": ["Jan", "Fev", "Mar"], "Valor": [10, 25, 20]})
    fig = px.line(df, x="Mês", y="Valor", title="Evolução de Contratos")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Cálculo Atuarial":
    st.title("📉 Inteligência de Risco")
    st.write("Módulo para projeção de reservas e tabelas biométricas.")

Versão: 1.0.0 | Data: Fevereiro 2026 | [Visite a Documentação →](./ESTRUTURA_FINAL.md)

