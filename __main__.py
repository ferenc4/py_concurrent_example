import concurrent
import time
from concurrent.futures import Future


def process_fn(v):
    cpu_intensive()
    print("v is {}".format(v))
    return v + 1


def cpu_intensive():
    for l in range(0, 1000):
        for i in range(0, 100):
            j = (i ** 2) ** (i / 2)


def test():
    resource = dict()
    for i in range(0, 100):
        resource[i] = i
    start = time.time()
    results = []
    print("Starting")
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
        for k in resource.keys():
            v = resource[k]
            print("Submitting ", v)
            future: Future = pool.submit(process_fn, v)
            results.append((k, future,))

        for key, future in results:
            exception = future.exception()
            if exception:
                raise exception
            resource[key] = future.result()
    print('That took {} seconds'.format(time.time() - start))
    print("results {} ".format(resource))


if __name__ == "__main__":
    test()
