'''
Created on 2019年12月2日

@author: baoyi
'''

def dataResp(result):
    if result == False:
        return {"code":200, "info":result}
    else:
        return {"code":200, "info":"", "data": result}