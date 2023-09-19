import json

import requests


class DataProvider:
    _MAIN_HOST = "https://api.focustech.xyz"
    _LAMBDA_HOST = "https://lambda.focustech.xyz"

    _PROJECT_LOCATIONS_URL = f"{_MAIN_HOST}/structure-service/v1/project_locations/"
    _METRICS_URL = f"{_LAMBDA_HOST}/core-data-provider/v1/metric_dynamics"
    _STRUCTURE_URL = f"{_LAMBDA_HOST}/structure-service/v1/cached_structure"

    def __init__(self, x_app_key):
        self._x_app_key = x_app_key

    def get_project_locations(self, token):
        """
        Получение доступных проектных локаций

        Args:
            token (str): Токен авторизации

        Returns:
            list | dict: Список доступных проектных локаций для этого токена или {"error": str}
        """

        response = requests.get(
            self._PROJECT_LOCATIONS_URL, headers=self._get_headers(token)
        )

        if response.ok:
            return response.json()

        return {"error": response.text}

    def get_data_objects(self, token, pl_id):
        """
        Получение отчетных объектов для проектной локации

        Args:
            token (str): Токен авторизации
            pl_id (int): id проектной локации

        Returns:
            list | dict: список отчетных объектов для проектной локации или {"error": str}
        """

        response = requests.get(
            f"{self._MAIN_HOST}/structure-service/v1/project_locations/{pl_id}/data_objects/",
            headers=self._get_headers(token),
        )

        if response.ok:
            return response.json()

        return {"error": response.text}

    def get_metric(
        self,
        token,
        metric,
        obj_ids,
        time_range,
        time_freq=None,
        object_aggregation=False,
        alias="",
    ):
        """
        Получение метрик

        Args:
            token (str): Токен авторизации
            metric (str): Название метрики или выражение метрик
            obj_ids (int[]): Id отчетных объектов по которым нужно получить данные метрики
            time_range ([str, str]): Период за который получить данные
            time_freq (str, optional): null|15MIN|H|D|W-MON|MS - Частота времени. Defaults to None.
            object_aggregation (bool, optional): Получить метрику для каждого объекта или метрика для агрегата. Defaults to False.
            alias (str, optional): _description_. Defaults to "".

        Returns:
            dict: {
                "result": [...], # Список данных
                "error": null,   # null or Строка ошибки
                "log": ""        # Логи
            }
        """

        payload = {
            "input_parameters": {
                "alias": alias,
                "metric": metric,
                "metric_level": "frozen",
                "obj_ids": obj_ids,
                "object_aggregation": object_aggregation,
                "time_range": time_range,
                "time_freq": time_freq,
            },
        }

        response = requests.post(
            self._METRICS_URL,
            headers={
                **self._get_headers(token),
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            data=json.dumps(payload),
        )

        if response.ok:
            return response.json()
        return {"error": response.text}

    def get_structures(self, token, pl_id, queries=[], jq=None):
        """
        Получение структуры

        По дефолту получаются структуры:
            core:
                - elements_admin_data_objects,
                - elements_ms_data_objects
                - relations_tenant2zone
                - relations_tenant2place
                - relations_tenant2location
                - relations_tenant2floor
                - relations_place2zone
                - relations_passway2dataobj
                - relations_dataobj2floor

        Args:
            token (str): Токен авторизации
            pl_id (int): ID проектной локации
            queries (list, optional): {"structure_section": str, "structure_type": str}. Defaults to [].
            jq (str, optional): JQ строка для форматирования. Defaults to None.

        Return dict: {
                "structure_name": {}[]
            } | {"error": str}
        """

        default_structures = [
            {
                "structure_section": "core",
                "structure_type": "elements_admin_data_objects",
            },
            {
                "structure_section": "core",
                "structure_type": "elements_ms_data_objects",
            },
            {
                "structure_section": "core",
                "structure_type": "relations_tenant2zone",
            },
            {
                "structure_section": "core",
                "structure_type": "relations_tenant2place",
            },
            {
                "structure_section": "core",
                "structure_type": "relations_tenant2location",
            },
            {
                "structure_section": "core",
                "structure_type": "relations_tenant2floor",
            },
            {
                "structure_section": "core",
                "structure_type": "relations_place2zone",
            },
            {
                "structure_section": "core",
                "structure_type": "relations_passway2dataobj",
            },
            {
                "structure_section": "core",
                "structure_type": "relations_dataobj2floor",
            },
        ]

        queries_payload = []

        for structure in default_structures if len(queries) == 0 else queries:
            query = f"pl_structure/pl{pl_id}/{structure['structure_section']}/{structure['structure_type']}.json"
            queries_payload.append({"item": query})

        payload = {"auth": {"xtoken": token}, "queries": queries_payload, "jq": jq}

        response = requests.post(self._STRUCTURE_URL, data=json.dumps(payload))

        if response.ok:
            return response.json()

        return {"error": response.text}

    def _get_headers(self, token):
        return {"x-token": token, "x-app-key": self._x_app_key}
