import os
import streamlit as st
from google.cloud import discoveryengine_v1 as discoveryengine
from google.api_core.client_options import ClientOptions

# CREDENCIAIS E DADOS DO PROJETO
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "advogadoia-487123-08f449738c06.json"

Project_id = "advogadoia-487123"
location = "global"
data_store_id = "robertonetorepository_1771903913319"

# BACKEND - LÓGICA DA IA
def search_legal_base(query_text):
    
    Client_Options = ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    client = discoveryengine.SearchServiceClient(client_options=Client_Options)

    serving_config = f"projects/{Project_id}/locations/{location}/collections/default_collection/dataStores/{data_store_id}/servingConfigs/default_search"

    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        snippet_spec = discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
            return_snippet = True
        ),
        summary_spec = discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count = 3,
            include_citations = True,
            ignore_adversarial_query = True,
            ignore_non_summary_seeking_query = True,
            
            model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                preamble="""Você é um advogado sênior e consultor jurídico especialista em Direito Civil e Direito Penal brasileiro.
                Analise a situação do usuário com extrema objetividade e rigor técnico.
                REGRA 1: Baseie-se EXCLUSIVAMENTE nos códigos, leis e súmulas fornecidos.
                REGRA 2: Estruture sua resposta citando o Artigo da lei ou Súmula aplicável e as possíveis consequências processuais.
                REGRA 3: Se não houver previsão legal nos documentos, diga que não encontrou."""
            )
        ),        
    )
    
    request = discoveryengine.SearchRequest(
        serving_config = serving_config,
        query = query_text,
        page_size = 3,
        content_search_spec = content_search_spec,
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
    )
    
    response = client.search(request)

    if response.summary.summary_text:
        return response.summary.summary_text
    else:
        return "Desculpe, não encontrei uma base legal específica para isso nos documentos fornecidos."
   
# FRONTEND
st.set_page_config(page_title="LexAI - Consultor de Direitos", page_icon="⚖️")

st.title("⚖️ LexAI: Seu Assistente de Direitos")
st.markdown("""
**Tire dúvidas sobre Direito Civil e Direito Penal.**
*Exemplos: 'Meu vizinho invadiu meu terreno, o que faço?', 'Qual a diferença entre furto e roubo?'*
""")

st.warning("Este é um projeto de portfólio tecnológico e educativo!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Descreva seu problema jurídico..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Analisando leis e documentos..."):
            try:
                response_text = search_legal_base(prompt)
                st.markdown(response_text)
                st.markdown("---")
                st.caption("Fonte: Base de Dados do Projeto / Vertex AI")
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"Erro no sistema: {e}")