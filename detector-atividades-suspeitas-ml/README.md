
# 🛡️ Detector de Atividades Suspeitas com Machine Learning

Projeto elaboraro para um trabalho do primeiro semestre do ano de 2025 da Intituição Uninove.
Curso TGTI

## 🎯 Objetivo
Este projeto foi desenvolvido com o objetivo de auxiliar times de SOC (Security Operations Center) e equipes Blue Team na detecção e resposta a ameaças cibernéticas. A proposta central é utilizar inteligência artificial para identificar padrões incomuns de tráfego de rede que possam indicar atividades maliciosas, como tentativas de ataque, presença de botnets, movimentações laterais ou exfiltração de dados sensíveis.

Em um cenário onde as ameaças estão cada vez mais sofisticadas e frequentes, confiar apenas em métodos tradicionais de monitoramento pode não ser suficiente. Por isso, o uso de algoritmos de aprendizado de máquina e técnicas de análise comportamental tornam-se fundamentais para reconhecer desvios sutis no padrão normal da rede, muitas vezes imperceptíveis a olho nu.

Além disso, este projeto busca não apenas detectar essas anomalias, mas também fornecer insights que apoiem a tomada de decisão rápida pelas equipes de segurança. A ferramenta proposta tem como foco contribuir para um ambiente mais seguro, promovendo uma postura defensiva mais proativa e inteligente, alinhada às necessidades atuais das organizações.

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
