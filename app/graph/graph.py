from langgraph.graph import StateGraph, START, END
from app.graph.state import GraphState
from app.graph import nodes
from app.graph import edges

def build_support_graph(checkpointer = None, ):

    # Graph object  
    graph = StateGraph(GraphState)
 
    # Node defination
    graph.add_node('retrieve_documents', nodes.retrieve_documents)
    graph.add_node('grader', nodes.grade_documents)
    graph.add_node('query_rewriter', nodes.query_rewritting)
    graph.add_node('response', nodes.generate_final_response)

    # Edge routing

    graph.add_edge(START, 'retrieve_documents')
    graph.add_edge('retrieve_documents','grader')
    graph.add_conditional_edges('grader', edges.route_query_rewritter)
    graph.add_edge('query_rewriter', 'retrieve_documents')
    graph.add_edge('response', END)

    # Graph Compilation

    return graph.compile(checkpointer=checkpointer)


