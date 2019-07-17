def solution(routes):
    routes_ = sorted(routes, key= lambda x: x[1])
    cameras = []
    idx = 0
    for i in routes_:
        if len(cameras) == 0:
            cameras.append(i[1])
        else :
            if cameras[idx] < i[0] :
                cameras.append(i[1])
                idx += 1
    return len(cameras)