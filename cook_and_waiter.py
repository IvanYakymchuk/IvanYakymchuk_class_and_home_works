import threading
import time


class Cook(threading.Thread):
    def __init__(self, total_orders, event):
        super().__init__()
        self.orders_queue = []
        self.lock = threading.Lock()
        self.total_orders = total_orders
        self.orders_served = 0
        self.event = event

    def run(self):
        while True:
            with self.lock:
                if self.orders_queue:
                    order = self.orders_queue.pop(0)
                    print(f"Повар приготовлює замовлення {order}")
                    time.sleep(3)
                    print(f"Повар виконав замовлення {order}")
                    self.orders_served += 1

                    if self.orders_served == self.total_orders:
                        print("Всі клієнти обслужені. Робота завершена.")
                        self.event.set()
                        return


class Waiter(threading.Thread):
    def __init__(self, name, cook, event, clients):
        super().__init__()
        self.name = name
        self.cook = cook
        self.event = event
        self.clients = clients

    def run(self):
        while not self.event.is_set():
            for client in self.clients:
                with self.cook.lock:
                    if not client["order_taken"]:
                        order = f"Замовлення від {self.name} для клієнта {client['id']}"
                        print(f"Офіціант {self.name} приймає замовлення: {order}")
                        self.cook.orders_queue.append(order)
                        client["order_taken"] = True
                        break
            time.sleep(1)


total_clients = 10
clients = [{"id": i, "order_taken": False} for i in range(1, total_clients + 1)]

event = threading.Event()

cook = Cook(total_clients, event)

waiter1 = Waiter("Офіціант 1", cook, event, clients)
waiter2 = Waiter("Офіціант 2", cook, event, clients)
waiter3 = Waiter("Офіціант 3", cook, event, clients)


cook.start()
waiter1.start()
waiter2.start()
waiter3.start()

event.wait()

cook.join()
waiter1.join()
waiter2.join()
waiter3.join()
