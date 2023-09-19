from hive.api import ApiManager, handling_single_page_methods, warning_wrong_parameters


class TsServiceStatus(ApiManager):
    """Class that handles all the XAutomata ts_service_status APIs"""

    def ts_service_status(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Status Services

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            uuid_service (string optional): additional filter - parameter
            timestamp_start (string optional): additional filter - parameter
            timestamp_end (string optional): additional filter - parameter
            database_timestamp_start (string optional): additional filter - parameter
            database_timestamp_end (string optional): additional filter - parameter
            status (None optional): additional filter - parameter
            ranking (integer optional): additional filter - parameter
            description (string optional): additional filter - parameter
            null_fields (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['sort_by', 'uuid_service',
            'timestamp_start', 'timestamp_end', 'database_timestamp_start',
            'database_timestamp_end', 'status', 'ranking', 'description',
            'null_fields', 'skip', 'limit', 'like', 'join', 'count']
        params.get('sort_by'), params.get('uuid_service'), params.get(
            'timestamp_start'), params.get('timestamp_end'), params.get(
            'database_timestamp_start'), params.get('database_timestamp_end'
            ), params.get('status'), params.get('ranking'), params.get(
            'description'), params.get('null_fields'), params.get('skip'
            ), params.get('limit'), params.get('like'), params.get('join'
            ), params.get('count')
        warning_wrong_parameters(self.ts_service_status.__name__, params,
            official_params_list)
        response = self.execute('GET', path=f'/ts_service_status/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_service_status_create(self, kwargs: dict = None, **payload) -> list:
        """Create Timeseries Service Status

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.

        Keyword Args:
            uuid_service (string required): additional filter - payload
            timestamp (string required): additional filter - payload
            status (None optional): additional filter - payload
            ranking (integer optional): additional filter - payload
            description (string optional): additional filter - payload
            extended_attributes (array object optional): additional filter - payload

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_payload_list = ['uuid_service', 'timestamp', 'status',
            'ranking', 'description', 'extended_attributes']
        payload.get('uuid_service'), payload.get('timestamp'), payload.get(
            'status'), payload.get('ranking'), payload.get('description'
            ), payload.get('extended_attributes')
        warning_wrong_parameters(self.ts_service_status_create.__name__,
            payload, official_payload_list)
        response = self.execute('POST', path=f'/ts_service_status/',
            payload=payload, **kwargs)
        return response

    def ts_service_status_delete(self, uuid_service: str,
        kwargs: dict = None, **params) -> list:
        """Delete Timeseries Service Status

        Args:
            uuid_service (str, required): uuid_service
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            ts_start (string required): additional filter - parameter
            ts_end (string required): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['ts_start', 'ts_end']
        params.get('ts_start'), params.get('ts_end')
        warning_wrong_parameters(self.ts_service_status_delete.__name__,
            params, official_params_list)
        response = self.execute('DELETE', path=
            f'/ts_service_status/{uuid_service}/', params=params, **kwargs)
        return response

    def ts_service_status_query(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Services

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            uuid_parent (string optional): additional filter - parameter
            uuid_customer (string optional): additional filter - parameter
            profile (string optional): additional filter - parameter
            name (string optional): additional filter - parameter
            description (string optional): additional filter - parameter
            status (string optional): additional filter - parameter
            ts_description (string optional): additional filter - parameter
            ts_status (None optional): additional filter - parameter
            ts_timestamp_start (string optional): additional filter - parameter
            ts_timestamp_end (string optional): additional filter - parameter
            ts_ranking (integer optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['sort_by', 'null_fields', 'uuid_parent',
            'uuid_customer', 'profile', 'name', 'description', 'status',
            'ts_description', 'ts_status', 'ts_timestamp_start',
            'ts_timestamp_end', 'ts_ranking', 'skip', 'limit', 'like',
            'join', 'count']
        params.get('sort_by'), params.get('null_fields'), params.get(
            'uuid_parent'), params.get('uuid_customer'), params.get('profile'
            ), params.get('name'), params.get('description'), params.get(
            'status'), params.get('ts_description'), params.get('ts_status'
            ), params.get('ts_timestamp_start'), params.get('ts_timestamp_end'
            ), params.get('ts_ranking'), params.get('skip'), params.get('limit'
            ), params.get('like'), params.get('join'), params.get('count')
        warning_wrong_parameters(self.ts_service_status_query.__name__,
            params, official_params_list)
        response = self.execute('GET', path=f'/ts_service_status/query/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_service_status_bulk(self, payload: list,
        warm_start: bool = False, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Read Status Metrics

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            ts_start (string required): additional filter - parameter
            ts_end (string required): additional filter - parameter

        Examples:
            payload = 
          [
            "uuid": "str", required
          ]

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['ts_start', 'ts_end']
        params.get('ts_start'), params.get('ts_end')
        warning_wrong_parameters(self.ts_service_status_bulk.__name__,
            params, official_params_list)
        response = self.execute('POST', path=
            f'/ts_service_status/bulk/read/', single_page=single_page,
            page_size=page_size, warm_start=warm_start, params=params,
            payload=payload, **kwargs)
        return response

    def ts_service_status_create_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000, kwargs: dict = None
        ) -> list:
        """Bulk Create Ts Service Status

        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.

        Examples:
            payload = 
          [
           {
            "uuid_service": "string", required
            "timestamp": "string", required
            "status": "None", optional
            "ranking": "integer", optional
            "description": "string", optional
            "extended_attributes": "array object", optional
           }
          ]

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=
            f'/ts_service_status/bulk/create/', single_page=single_page,
            page_size=page_size, payload=payload, **kwargs)
        return response

    def ts_service_status_delete_bulk(self, payload: list,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Bulk Delete Ts Service Status

        Args:
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            payload (list[dict], optional): List dict to create.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            ts_start (string required): additional filter - parameter
            ts_end (string required): additional filter - parameter

        Examples:
            payload = 
          [
            "uuid": "str", required
          ]

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['ts_start', 'ts_end']
        params.get('ts_start'), params.get('ts_end')
        warning_wrong_parameters(self.ts_service_status_delete_bulk.
            __name__, params, official_params_list)
        response = self.execute('POST', path=
            f'/ts_service_status/bulk/delete/', single_page=single_page,
            page_size=page_size, params=params, payload=payload, **kwargs)
        return response
