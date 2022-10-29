from concurrent.futures import ThreadPoolExecutor
import time
from flask import Flask
app = Flask(__name__)


def func_one(argument_1, argument_2):
    time.sleep(1)
    return argument_1 * argument_2


def func_two(argument_1, argument_2):
    time.sleep(0.5)
    return argument_1 * argument_2


@app.route('/', methods=["GET"])
def my_func():
    start = time.time()
    with ThreadPoolExecutor() as executor:
        future_1 = executor.submit(func_one, 1, 1)
        future_2 = executor.submit(func_one, 2, 2)
        # future_3 = executor.submit(func_one, 3, 3)
        # future_4 = executor.submit(func_one, 4, 4)
        # future_5 = executor.submit(func_two, 1, 5)
        # future_6 = executor.submit(func_two, 2, 6)
        # future_7 = executor.submit(func_two, 3, 7)
        # future_8 = executor.submit(func_two, 4, 8)
        # future_9 = executor.submit(func_one, 5, 9)
        # future_10 = executor.submit(func_two, 5, 10)
        print("Printing future 1", future_1.result())
        print("Printing future 2", future_2.result())
        # print("Printing future 3", future_3.result())
        # print("Printing future 4", future_4.result())
        # print("Printing future 5", future_5.result())
        # print("Printing future 6", future_6.result())
        # print("Printing future 7", future_7.result())
        # print("Printing future 8", future_8.result())
        # print("Printing future 9", future_9.result())
        # print("Printing future 10", future_10.result())
    print(time.time()-start)
    return {1: 1}


app.run(host='0.0.0.0', port=8000)
