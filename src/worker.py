import time
from threading import Thread

from src.model.work import Work
from src.queue.consumer import start_consumer
from src.util.person_detection import person_detection, get_image_ndarray_for_job


def run_detection_consumer(tid: int) -> None:
    def detection_task(work: Work) -> str:
        print(f"[{tid}] Starting detection task for job id={work.work_id}")
        return str(person_detection(image=get_image_ndarray_for_job(work)))

    start_consumer(detection_task)


if __name__ == "__main__":
    print("Starting detection consumer")
    NUM_THREADS = 16

    threads = [Thread(target=run_detection_consumer, args=(tid,)) for tid in range(NUM_THREADS)]

    for thread in threads:
        print("Starting thread", thread.name)
        thread.start()
        time.sleep(0.01)

    for thread in threads:
        thread.join()
        print("joining thread", thread.name)
