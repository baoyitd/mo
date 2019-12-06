'''
Created on 2019年12月2日

@author: baoyi
'''

def dataResp(result):
    if result == False:
        return {"code":200, "info":None}
    else:
        return {"code":200, "info":"", "data": result}
    
def dataRespSuc(info, result):
    return {"code":200, "info":info, "data": result}

def dataRespFull(code, info, result):
    return {"code":code, "info":info, "data": result}