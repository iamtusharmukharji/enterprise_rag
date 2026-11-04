from app.graph.graph import build_support_graph


graph = build_support_graph()


test_queries = [
    'What is deployment policy ?',
    # 'Tell me the resturant name that we went last friday.',
    # "What is the company's policy for underwater mining operations on Europa?",
    # 'What was the exact restaurant name where I had dinner last Friday, and what did I order?'


]

def run_test():
    for qry in test_queries:
        state = graph.invoke({'question' : qry, 'retry_count' : 0, 'max_retries' : 2})
        r = f"""\n------------------------------
User Query: {state.get('question')}
Rewritten Question : {state.get('rewritten_question')}
documents : {state.get('documents')}
is_relevant : {state.get('is_relevant')}
sources : {state.get('sources')}
retries : {state.get('retry_count')}
final_response : {state.get('answer')}
------------------------------------------
        """

        print(r)



if __name__ == '__main__':
    run_test()