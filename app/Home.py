import streamlit as st

st.set_page_config(page_title="ChatGPT-Powered Azure Cognitive (Smart) Search", page_icon="📖", layout="wide")

st.image("https://user-images.githubusercontent.com/113465005/226238596-cc76039e-67c2-46b6-b0bb-35d037ae66e1.png")
st.image("https://raw.githubusercontent.com/markvogt-avanade/GPT-Azure-Search-Engine/main/.github/images/logo-avanade-transparent.png", width=381)

st.header("ChatGPT-Powered Azure Cognitive (Smart) Search Engine")


st.markdown("---")
st.markdown("""
    GPT Smart Search allows you to ask questions about your
    documents and get accurate answers with instant citations.
    
    This Avanade-Microsoft demonstration engine combines the power of Azure Cognitive Search and Azure OpenAI's ChatGPT to deliver a powerful new search experience. 
    This demo searches and summarizes/distills information from the following narrow-topic document corpuses:
    - ~100 [Documents related specifically to System Integration Solution Architects](https://avanade.sharepoint.com/sites/NASolutionArchitectCommunity)
    - ~100 [Industrial-grade electrical machinery commonly used & maintained by field engineers in the Utilities field](https://www.google.com/search?q=industrial+electrical+equipment&sxsrf=APwXEde4jg3_N697hUeuWgc-S9DIkMHCEg%3A1682735938332&source=hp&ei=QoNMZL3ZD6iI0PEPwN2xYA&iflsig=AOEireoAAAAAZEyRUsc80i1AI4cB11H6lylvJ0KLe0y1&ved=0ahUKEwi9gufuh87-AhUoBDQIHcBuDAwQ4dUDCAs&uact=5&oq=industrial+electrical+equipment&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yCAgAEBYQHhAPMggIABAWEB4QDzoHCCMQ6gIQJzoHCCMQigUQJzoECCMQJzoLCAAQgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOgsILhCABBDHARDRAzoICC4QgAQQsQM6CAguEIAEENQCOg4IABCABBCxAxCDARDJAzoICAAQigUQkgM6CwguEIMBELEDEIoFOgsILhCABBCxAxCDAToOCC4QgAQQsQMQgwEQ1AI6BQguEIAEOggIABCABBCxAzoLCC4QgAQQsQMQ1AI6CwguENQCELEDEIAEOgsILhCABBDHARCvAToLCAAQigUQsQMQgwE6CwguEK8BEMcBEIAEULoGWIE6YKo-aAFwAHgAgAHYAogBzBiSAQgyMi43LjEuMZgBAKABAbABCg&sclient=gws-wiz#bsht=Cgdic2h3Y2hwEgQIBDAB)
    
    **👈 Select a demo from the sidebar** to see some examples of what Azure Cognitive Search and Azure OpenAI Service can do!
    ### Want to learn more?
    - Check out [Github Repo](https://github.com/pablomarin/GPT-Azure-Search-Engine/)
    - Jump into [Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
    - Ask a question or submit a [GitHub Issue!](https://github.com/pablomarin/GPT-Azure-Search-Engine/issues/new)


    
"""
)
st.markdown("---")


st.sidebar.success("Select a demo above.")
