import asyncio
import time
try:
    import aiohttp
    async_http_req = True
except ModuleNotFoundError:
    print("Can't load aiohttp library. Using plain urllib requests.")
    async_http_req = False

test_times = 10
server = "https://ya.ru"
import urllib.request as u_request 

async def  _get_response(req, encoding, session = None, async_http_req = False):
    if not async_http_req:
        try:
            with u_request.urlopen(req) as f:
                return {"data":f.read().decode(encoding), "code":f.code}
        except u_request.HTTPError as error:
            with error as f:
                return {"data":f.read().decode(encoding), "code":f.code}
    elif session:
        url = req.get_full_url()
        method = req.get_method()
        data = req.data
        headers = {"Content-Type": f"application/json"}
        if method == "GET":
            request_handler = session.get
        elif method == "POST":
            request_handler = session.post
        elif method == "PUT":
            request_handler = session.put
        elif method == "DELETE":
            request_handler = session.delete
        else:
            raise ValueError(f"Wrong request method {method}. check your request method.")
        async with request_handler(url, data=data, headers=headers) as resp:
            # ~ print(resp.status)
            txt = await resp.text()
            # ~ print(txt)
            return "async finish"
    else:
        raise ValueError("Parameter 'session' should be specified when using aiohttp")

def mt(req, encoding):
    try:
        with u_request.urlopen(req) as f:
            return {"data":f.read().decode(encoding), "code":f.code}
    except u_request.HTTPError as error:
        with error as f:
            return {"data":f.read().decode(encoding), "code":f.code}

async def main(encoding):
    global async_http_req, test_times
    
    async with aiohttp.ClientSession() as session:
        btime = time.time()
        for i in range(test_times):
            # ~ req = u_request.Request(url="https://track.iscrasec.ru/users.json?key=77c55129febeb6063853a007a1a73f3fe4e7fcf0", data=None, method="GET")
            req = u_request.Request(url=server, data=None, method="GET")
            await _get_response(req, encoding, session, True)
        print(f"aiohttp: {time.time()-btime:4f}s")

    btime = time.time()
    for i in range(test_times):
        # ~ req = u_request.Request(url="https://track.iscrasec.ru/users.json?key=77c55129febeb6063853a007a1a73f3fe4e7fcf0", data=None, method="GET")
        req = u_request.Request(url=server, data=None, method="GET")
        await _get_response(req, encoding, None, False)
    print(f"plain urllib: {time.time()-btime:4f}s")

encoding = "utf-8"

print (f"Test passes: {test_times}")
asyncio.run(main(encoding))

from threading import Thread
btime = time.time()
t_pool = list()
for i in range(test_times):
    req = u_request.Request(url=server, data=None, method="GET")
    t_pool.append(Thread(target=mt, args=(req, encoding,)))
    t_pool[-1].start()
for t in t_pool:
    t.join()
print(f"mtreading: {time.time()-btime:4f}s")
