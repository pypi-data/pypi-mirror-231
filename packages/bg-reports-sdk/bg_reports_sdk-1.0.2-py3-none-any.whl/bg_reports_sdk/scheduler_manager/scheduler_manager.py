import json
from abc import ABC, abstractmethod

import requests

from bg_reports_sdk.config import *
from bg_reports_sdk.data_provider.data_provider import DataProvider
from bg_reports_sdk.scheduler_manager.scheduler import Scheduler


class SchedulerSDKError(Exception):
    pass


class SchedulerExecutionError(Exception):
    pass


class SchedulerManager(ABC):
    _SSO_CURRENT = "https://lambda.focustech.xyz/core-current"
    _BACKEND_URL = f"{BACKEND_HOST}/api"

    _ACCESS_FIELD_KEYS_MAP = {
        "pl_id": "available_project_locations",
        "project_id": "available_projects",
        "owner_id": "available_owners",
    }

    report_type = None

    data_provider = None

    created_schedulers_count = 0

    def __init__(self, master_token):
        self._master_token = master_token
        self._request_headers = {"x-token": self._master_token}
        self.data_provider = DataProvider(x_app_key=self.report_type)
        self._report_type_json = self._get_report_type_by_name(self.report_type)
        self._current_json = self._get_current()

    def _get_current(self):
        """
        Получение информации о пользователе
        """
        response = requests.get(
            self._SSO_CURRENT, headers={"x-token": self._master_token}
        )
        if response.ok and "error" not in response.json():
            return response.json()
        else:
            raise SchedulerSDKError("Invalid token")

    def _get_schedulers(self):
        """
        Получение всех планировщиков для конкретного типа отчета

        Returns:
            list: Scheduler[]
        """

        response = requests.get(
            f"{self._BACKEND_URL}/background-report-schedulers/?report_type={self.report_type}",
            headers=self._request_headers,
        )

        if response.ok:
            return response.json()

        raise SchedulerSDKError(
            f"An error accrued while getting schedulers. {response.text}"
        )

    def _get_report_type_by_name(self, name):
        """
        Получение типа отчета по его имени

        Args:
            name (str): Имя отчета

        Returns:
            dict: Объект типа отчета
        """
        response = requests.get(
            f"{self._BACKEND_URL}/background-report-types/?name={name}",
            headers=self._request_headers,
        )

        if response.ok:
            result = response.json()
            if len(result) > 0:
                return result[0]

        raise SchedulerSDKError(
            f"An error accrued while getting report type with name {name}. {response.text}"
        )

    def _generate_schedule_payload(self, scheduler):
        """
        Генерация тела запроса для создания планировщика

        Args:
            scheduler (Scheduler): instance Scheduler

        Returns:
            json: тело запроса для создания планировщика
        """
        if isinstance(scheduler, Scheduler) and scheduler.is_valid():
            payload = scheduler.to_dict()
            if payload[self._report_type_json["access_field"]] is not None:
                if (
                    payload[self._report_type_json["access_field"]]
                    in self._current_json[
                        self._ACCESS_FIELD_KEYS_MAP[
                            self._report_type_json["access_field"]
                        ]
                    ]
                ):
                    payload["user_id"] = self._current_json["id"]
                    payload["report_type"] = self._report_type_json["id"]
                else:
                    raise SchedulerSDKError(
                        f"You dont have permissions for {self._report_type_json['access_field']}: {payload[self._report_type_json['access_field']]}"
                    )

                return payload
            else:
                raise SchedulerSDKError(
                    f"Schedule has invalid access field. Valid access field is {self._report_type_json.get('access_field')}"
                )

        raise SchedulerSDKError(f"Schedule is invalid")

    def _create_scheduler(self, payload):
        """
        Создание планировщика. Если планировщик был создан полу created_schedulers_count
        увеличивается на 1

        Args:
            scheduler (Scheduler): Scheduler

        Returns:
            None: Ничего не возвращает
        """

        response = requests.post(
            f"{self._BACKEND_URL}/create-background-report-schedule/",
            headers={
                **self._request_headers,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            data=json.dumps(payload),
        )

        if response.ok:
            self.created_schedulers_count += 1
            return

        raise SchedulerSDKError(
            f"An error accrued while creating scheduler. {response.text}"
        )

    def _patch_scheduler(self, scheduler):
        if scheduler.get("id", None) is None:
            raise SchedulerSDKError(f"An error accrued while patch scheduler (no ID).")

        payload = {"is_active": False}
        response = requests.patch(
            f"{self._BACKEND_URL}/background-report-schedulers/{scheduler['id']}/",
            headers={
                **self._request_headers,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            data=json.dumps(payload),
        )

        if response.ok:
            return
        else:
            raise SchedulerSDKError(
                f"An error accrued while patch scheduler. {response.text}"
            )

    @staticmethod
    def _hash_dict(d, fields_to_compare):
        # Вспомогательная функция для преобразования словаря в хэшируемый кортеж пар ключ-значение
        return tuple(sorted((key, d[key]) for key in fields_to_compare))

    def _compare_arrays_of_dicts(self, array1, array2, fields_to_compare):
        """
        Сравнение массивов словарей
        """

        # Создаем список хешей для каждого словаря в массивах array1 и array2
        array1_hashes = [self._hash_dict(item, fields_to_compare) for item in array1]
        array2_hashes = [self._hash_dict(item, fields_to_compare) for item in array2]

        # Находим элементы, которые различаются между array2 и array1
        different_elements = [
            item
            for item in array2
            if self._hash_dict(item, fields_to_compare) not in array1_hashes
        ]

        # Находим новые элементы в array2, которых нет в different_elements
        new_elements = [
            item
            for item in array2
            if self._hash_dict(item, fields_to_compare) not in array1_hashes
            and item not in different_elements
        ]

        # Находим элементы в array1, которых нет в array2
        array1_new_elements = [
            item
            for item in array1
            if self._hash_dict(item, fields_to_compare) not in array2_hashes
        ]

        return different_elements + new_elements, array1_new_elements

    @abstractmethod
    def _check_schedulers(self, master_token):
        """
        Функция для проверки существующих планировщиков. Для работы класса ее необходимо
        переопределить.

        Args:
            master_token (str): токен авторизации

        Return:
            list: Метод должен вернуть список планировщиков, которые нужно создать
        """
        raise SchedulerExecutionError("You should implement _check_schedulers method")

    def run(self):
        """
        Запуск проверки планировщиков. Если метод _check_schedulers вернул планировщики,
        то они будут созданы
        """

        try:
            all_schedulers = self._get_schedulers()
            try:
                checked_schedulers = self._check_schedulers(
                    master_token=self._master_token
                )
            except Exception as e:
                raise SchedulerExecutionError(e.__traceback__)

            checked_scheduler_dicts = []
            for scheduler in checked_schedulers:
                try:
                    checked_scheduler_dicts.append(
                        self._generate_schedule_payload(scheduler=scheduler)
                    )
                except SchedulerSDKError as e:
                    print(e)

            if len(checked_schedulers) != 0:
                (
                    different_elements,
                    new_elements,
                ) = self._compare_arrays_of_dicts(
                    checked_scheduler_dicts,
                    all_schedulers,
                    [
                        "pl_id",
                        "project_id",
                        "owner_id",
                        "input_parameters",
                        "start_date",
                        "frequency",
                        "start_delay",
                        "user_id",
                    ],
                )

                for new_element in new_elements:
                    try:
                        self._create_scheduler(payload=new_element)
                    except SchedulerSDKError as e:
                        print(e)

                for different_element in different_elements:
                    try:
                        self._patch_scheduler(scheduler=different_element)
                    except SchedulerSDKError as e:
                        print(e)

        except SchedulerSDKError as e:
            raise e
        except SchedulerExecutionError as e:
            raise e
