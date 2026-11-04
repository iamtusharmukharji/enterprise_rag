from app.graph.state import GraphState
from langgraph.graph import END

def route_query_rewritter(state : GraphState):

    retry_allowed = True if state.get('max_retries') > state.get('retry_count') else False
    is_relevant = state.get('is_relevant')
    empty_documents = True if state.get('documents') == [] else False

    # check condition for if query is not relevant or docuemnts are empty
    if (not is_relevant or empty_documents) and retry_allowed:
        return 'query_rewriter'
    
    return 'response'
    