# Charlie
# date:2020/3/18 15:38
# file_name:run3
from celery.result import AsyncResult
if __name__ == '__main__':
    task = AsyncResult('')
    print(task.result)