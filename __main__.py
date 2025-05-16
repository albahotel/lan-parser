import socket
import sys
# import struct # Нужен для реализации префикса длины, если сервер его ожидает

# Импорт сгенерированного кода Protocol Buffers
try:
    import message_pb2
except ImportError:
    print("Ошибка: Не удалось импортировать message_pb2.")
    print("Пожалуйста, убедитесь, что вы создали файл message.proto и сгенерировали message_pb2.py командой:")
    print("  protoc --python_out=. message.proto")
    sys.exit(1)

# Константы для подключения к контроллеру
SERVER_IP = "192.168.1.100" # IP адрес контроллера
SERVER_PORT = 7000           # Порт TCP сервера на контроллере

def get_controller_info():
    """
    Подключается к контроллеру по TCP, запрашивает информацию
    и выводит полученные данные.
    """
    client_socket = None
    try:
        # 1. Создание TCP сокета
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("TCP сокет создан.")

        # Установка таймаута для операций сокетом (опционально, но рекомендуется)
        client_socket.settimeout(5) # Таймаут 5 секунд

        # 2. Установление соединения с контроллером
        print(f"Попытка соединения с {SERVER_IP}:{SERVER_PORT}...")
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"Соединение установлено успешно.")

        # 3. Создание Protobuf сообщения ClientMessage с запросом get_info
        client_message = message_pb2.ClientMessage(get_info=message_pb2.GetInfo())

        # === ИСПРАВЛЕНИЕ ЗДЕСЬ ===
        # Чтобы установить поле 'get_info' в oneof 'message',
        # просто обращаемся к полю 'get_info'. Это активирует его в oneof
        # и возвращает экземпляр message_pb2.GetInfo().
        # Если бы message_pb2.GetInfo() имело поля, мы бы могли установить их вот так:
        # client_message.get_info.какое_то_поле = значение
        # Но GetInfo пустое, поэтому достаточно простого обращения к полю get_info.
        # =========================

        print("Создано ClientMessage с запросом get_info.")

        # active_field = client_message.WhichOneof('message')
        # print(f"Проверка состояния client_message перед сериализацией:")
        # print(f"Активное поле в oneof 'message': {active_field}")
        # if active_field != 'get_info':
        #     print("ВНИМАНИЕ: Поле 'get_info' не установлено как активное в oneof 'message'!")

        # 4. Сериализация сообщения в байты
        request_data = client_message.SerializeToString()
        print(f"ClientMessage сериализовано в {len(request_data)} байт.")

        # --- ВАЖНЫЙ МОМЕНТ: Определение границ сообщений по TCP ---
        # (Тот же комментарий, что и раньше - при необходимости используйте префикс длины)
        data_to_send = request_data # В этом упрощенном примере отправляем только данные

        print(f"Отправка {len(request_data)} байт данных сообщения.")
        client_socket.sendall(data_to_send)

        print("Protobuf запрос отправлен.")

        # 5. Чтение ответа от контроллера
        # (Тот же комментарий, что и раньше - чтение упрощенное)
        print("Ожидание ответа от контроллера...")
        response_data = client_socket.recv(1024) # Читаем максимум 1024 байт
        print(f"Получено {len(response_data)} байт.")

        if not response_data:
            print("Получены пустые данные ответа. Возможно, сервер закрыл соединение.")
            return

        # 6. Десериализация полученных байтов в ControllerResponse
        controller_response = message_pb2.ControllerResponse(info=message_pb2.Info())
        try:
            controller_response.ParseFromString(response_data)
            print("Ответ успешно десериализован.")
            print(controller_response)

            # 7. Проверка, какое поле установлено в oneof "response"
            # if controller_response.response == "info":
            #     info_message = controller_response.info
            #     print("\n--- Информация о контроллере (message.response.info): ---")
            #     print(f"  IP: {info_message.ip}")
            #     print(f"  MAC: {info_message.mac}")
            #     print(f"  BLE Name: {info_message.ble_name}")
            #     print(f"  Token: {info_message.token}")
            #     print("------------------------------------------------------")

            # elif controller_response.response == "state":
            #      state_message = controller_response.state
            #      print("\nПолучено сообщение 'state', хотя ожидалось 'info'.")
            #      print(f"  Текущее состояние (число): {state_message.state}")
            #
            # elif controller_response.response == "status":
            #      status_code = controller_response.status
            #      print(f"\nПолучен только код статуса: {message_pb2.Statuses.Name(status_code)} ({status_code})")
            #
            # else:
            #     print("\nПолучен ответ, но поле 'response' не установлено (или установлено в неизвестное значение).")
            #     print(f"Полученное сообщение Protobuf: {controller_response}")


        except Exception as e:
             print(f"Ошибка при десериализации или обработке Protobuf ответа: {e}")
             print(f"Полученные байты: {response_data.hex()}") # Вывести байты в шестнадцатеричном формате для отладки


    except socket.timeout:
         print(f"Ошибка подключения: Истекло время ожидания операции сокетом ({SERVER_IP}:{SERVER_PORT}).")
    except ConnectionRefusedError:
         print(f"Ошибка подключения: Соединение отклонено (WINERROR 10061). Убедитесь, что сервер запущен на {SERVER_IP}:{SERVER_PORT} и нет блокировок брандмауэром.")
    except socket.gaierror as e:
        print(f"Ошибка разрешения адреса: {e} (Проверьте IP адрес или имя хоста)")
    except socket.error as e:
        print(f"Ошибка сокета: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        # 8. Закрытие сокета после использования
        if client_socket:
            client_socket.close()
            print("Соединение закрыто.")

# --- Запуск функции ---
if __name__ == "__main__":
    get_controller_info()