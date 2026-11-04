from fastapi import APIRouter, Request



router = APIRouter(
    prefix='/chat',
    tags= ['Chat']
)

@router.get('/')
async def chat(prompt : str, request : Request, ):
    
    if prompt.strip() == '':
        return {"success":False, "message":"User prompt can't be empty"}

    rag_graph = request.app.state.graph

    response = await rag_graph.ainvoke({'question':prompt, 'max_retries' : 2, 'retry_count':0}, config = {
        "callbacks" : [request.app.state.langfuse_trace]
    })
    # print(response)

    return {
        'success':True,
        'data' : {
            'response' : response.get('answer'),
            'sources' : response.get('sources')
            }
    }