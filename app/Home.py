import streamlit as st

st.set_page_config(page_title="ChatGPT-Powered Azure Cognitive (Smart) Search", page_icon="📖", layout="wide")

st.image("https://user-images.githubusercontent.com/113465005/226238596-cc76039e-67c2-46b6-b0bb-35d037ae66e1.png")
st.image("https://raw.githubusercontent.com/markvogt-avanade/GPT-Azure-Search-Engine/main/.github/images/logo-avanade-transparent.png", width=381)

st.header("ChatGPT-Powered Azure Cognitive (Smart) Search Engine")


st.markdown("---")
st.markdown("""
    GPT Smart Search allows you to ask questions about your documents and get accurate answers with instant citations.
    
    This Avanade-Microsoft demonstration engine combines the power of Azure Cognitive Search and Azure OpenAI's ChatGPT to deliver a powerful new search experience. 
    
    Our demo searches and "generates" (summarizes/distills) information from the following narrow-topic document corpuses:
    - Arxiv Computer Science publications from 2020-2021 (10,000 articles)
    - Medical Covid-19 Publications from 2020 (52,000 records)
    - Avanade Library on SISAs (25+ documents)
    - Library of Industrial Electrical Machinery (350+ documents)
    - Accenture Library on Customer Data Protection (10+ documents)
    
    
    **👈 Select a demo from the sidebar** to see some examples of what Azure Cognitive Search and Azure OpenAI Service can do!
    ### Want to learn more?
    - Check out [Github Repo](https://github.com/pablomarin/GPT-Azure-Search-Engine/)
    - Jump into [Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
    - Ask a question or submit a [GitHub Issue!](https://github.com/pablomarin/GPT-Azure-Search-Engine/issues/new)


    
"""
)
st.markdown("---")


st.sidebar.success("Select a demo above.")
