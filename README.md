# ⚖️ LexAI - Assistente Jurídico com IA (RAG)

O **LexAI** é um assistente virtual jurídico desenvolvido em Python, focado em Direito Civil e Penal. Utilizando a arquitetura RAG (Retrieval-Augmented Generation) com o Google Vertex AI, o sistema consulta uma base de dados própria contendo Códigos e Súmulas reais para fornecer respostas precisas, citando os artigos de lei e evitando "alucinações" comuns em IAs genéricas.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python
* **Interface:** Streamlit
* **IA e Nuvem:** Google Cloud Platform (Vertex AI Search / Discovery Engine)
* **Engenharia de Prompt:** IA instruída com persona de Advogado Sênior.

## ⚙️ Como rodar localmente
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Adicione sua chave de serviço do Google Cloud (`.json`) na raiz do projeto.
4. Rode o comando: `streamlit run app.py`

*Este é um projeto de portfólio tecnológico e educativo.*