from multiprocessing import Process, Manager


def update_status(state):
    state.status = "completed"
    state.progress = 100


if __name__ == "__main__":
    with Manager() as manager:
        state = manager.Namespace()

        state.status = "pending"
        state.progress = 0

        process = Process(
            target=update_status,
            args=(state,)
        )

        process.start()
        process.join()

        print(state.status)
        print(state.progress)