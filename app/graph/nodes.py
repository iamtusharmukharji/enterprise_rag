from app.graph.state import GraphState
from app.retrieval.hybrid_retriever import hybrid_search
from app.retrieval.reranker import rerank_documents
from app.ingestion.pipeline import bm25_retriever
from app.graph.llm import get_llm
from app.graph import structured_output
from langchain_core.messages import HumanMessage, SystemMessage



llm = get_llm(provider='google')


# def retrieve_documents(instrument):
#     # return {
#     #     "documents": [],
#     #     "is_relevant": None,
#     # }
#     @instrument.node_trace
#     def execute(state: GraphState) -> dict:
#         query = state.get('rewritten_question') if state.get('rewritten_question') else state.get('question')
        
#         candidates = hybrid_search(
#             query=query,
#             bm25_retriever=bm25_retriever,
#             top_k=10,
#             candidate_k=20,
#         )

#         results = rerank_documents(
#             query=query,
#             documents=candidates,
#             top_k=5,
#         )

#         return {
#             'documents' : results,
#             'is_relevant' : None
#             }
    
#     return execute

def retrieve_documents(state: GraphState) -> dict:
    query = state.get('rewritten_question') if state.get('rewritten_question') else state.get('question')
    
    candidates = hybrid_search(
        query=query,
        bm25_retriever=bm25_retriever,
        top_k=10,
        candidate_k=20,
    )
    
    results = rerank_documents(
        query=query,
        documents=candidates,
        top_k=5,
    )

    return {
        'documents' : results,
        'is_relevant' : None
        }

def grade_documents(state : GraphState):

    if state.get('documents') == []:
        print('############### Condition met for No Documents found ###################')
        return {
            'is_relevant' : False,
            'sources' : []
        }
    grader = llm.with_structured_output(structured_output.DocumentGrade)

    SYSTEM_PROMPT = f""" You are document evaluator for a RAG system where you need to evaluate retrieved document chunks as per user's question.
    You need to evaluate retrieved chunks of documents as per below and response within below parameters
        - is_relevant : whether fetched documents are relevant to the user's query or not
        - sources : list of document chunks that are relevant and can be used as ground/srouce to build response
    Note:- when no chunk provides relevant evidence, the grader should return is_relevant=False and an empty source list.
    """
    user_query = state.get('rewritten_question') if state.get('rewritten_question') else state.get('question')

    human_message = f"""
        User Query = {user_query}
        Retrieved Document = {state.get('documents')}
    """
    # print(human_message)
    message_array = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=human_message)
    ]

    response : structured_output.DocumentGrade = grader.invoke(message_array)
    return {
        'is_relevant' : response.is_relevant,
        'sources' : response.sources
    }

def query_rewritting(state : GraphState):

    relevant = state.get('is_relevant')
    documents = state.get('documents')
    retries = state.get('retry_count')
    max_retries = state.get('max_retries')

    query = state.get('rewritten_question') if state.get('rewritten_question') else state.get('question')

    if retries >= max_retries:
        return
    
    # if len(documents) > 0 and not relevant:
    if not relevant:
        # apply query rewrtting
        query_rewriter = llm.with_structured_output(structured_output.OptimisedQuery)

        SYSTEM_INS = """You are an intelligent user query/prompt optimiser that optimises a given user's query/prompt so that relevant documents can be fetched from vector databases"""

        message_array = [
            SystemMessage(content=SYSTEM_INS),
            HumanMessage(content=query)
        ]

        response : structured_output.OptimisedQuery = query_rewriter.invoke(message_array)

        return {
            'rewritten_question' : response.rewritten_query,
            'retry_count' : retries+1
        }
    
    return {'retry_count' : retries+1}

def generate_final_response(state : GraphState):

    SYSTEM_INS = f"""You are an AI Assistant that generates a user friendly response to an user based on the fetched doucment sources.
    - You have to generate a response based on the document source only, you are not allowed to give any response without grounding
    - If there is no sources, politely response to user about insufficent source or knowledge 

    Sources : {state.get('sources')} 
    """
    final_query = state.get('question')
    message_array = [
        SystemMessage(content = SYSTEM_INS),
        HumanMessage(content = final_query)
    ]

    response = llm.invoke(message_array)

    return {'answer': response.content}
    
        
    






