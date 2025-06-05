
# 🛡️ Detector de Atividades Suspeitas com Machine Learning

Este projeto foi desenvolvido com o objetivo de auxiliar times de SOC e equipes Blue Team em geral. A proposta é apoiar essas equipes na identificação de possíveis ataques, utilizando a inteligência artificial como aliada na detecção e resposta a ameaças.

## 🎯 Objetivo
Detectar padrões incomuns de tráfego de rede que possam indicar atividades maliciosas, como ataques, botnets ou exfiltração de dados.

## 📁 Estrutura do Projeto
- `data/`: Dados brutos e Processados
- `notebooks/`: notebooks de análise e modelagem
- `src/`: código-fonte da aplicação
- `dashboard/`: interface visual com Streamlit
- `tests/`: testes com automatização
- `.github/workflows`: automação com GitHub Actions

## ▶️ Como rodar
```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## 📜 Licença
MIT
