from hive.api import ApiManager, handling_single_page_methods, warning_wrong_parameters


class TsCostManagement(ApiManager):
    """Class that handles all the XAutomata ts_cost_management APIs"""

    def ts_cost_management(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Costs

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            uuid_metric (string optional): additional filter - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            cloud_provider (string optional): additional filter - parameter
            resource_location (string optional): additional filter - parameter
            subscription_type (string optional): additional filter - parameter
            subscription_id (string optional): additional filter - parameter
            subscription_name (string optional): additional filter - parameter
            family (string optional): additional filter - parameter
            category (string optional): additional filter - parameter
            subcategory (string optional): additional filter - parameter
            object (string optional): additional filter - parameter
            metric (string optional): additional filter - parameter
            unit (string optional): additional filter - parameter
            resource_group (string optional): additional filter - parameter
            reservation_name (string optional): additional filter - parameter
            publisher_name (string optional): additional filter - parameter
            local_currency (string optional): additional filter - parameter
            provider_currency (string optional): additional filter - parameter
            uuid_customer (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['sort_by', 'null_fields', 'uuid_metric',
            'date_start', 'date_end', 'cloud_provider', 'resource_location',
            'subscription_type', 'subscription_id', 'subscription_name',
            'family', 'category', 'subcategory', 'object', 'metric', 'unit',
            'resource_group', 'reservation_name', 'publisher_name',
            'local_currency', 'provider_currency', 'uuid_customer', 'skip',
            'limit', 'like', 'join', 'count']
        params.get('sort_by'), params.get('null_fields'), params.get(
            'uuid_metric'), params.get('date_start'), params.get('date_end'
            ), params.get('cloud_provider'), params.get('resource_location'
            ), params.get('subscription_type'), params.get('subscription_id'
            ), params.get('subscription_name'), params.get('family'
            ), params.get('category'), params.get('subcategory'), params.get(
            'object'), params.get('metric'), params.get('unit'), params.get(
            'resource_group'), params.get('reservation_name'), params.get(
            'publisher_name'), params.get('local_currency'), params.get(
            'provider_currency'), params.get('uuid_customer'), params.get(
            'skip'), params.get('limit'), params.get('like'), params.get('join'
            ), params.get('count')
        warning_wrong_parameters(self.ts_cost_management.__name__, params,
            official_params_list)
        response = self.execute('GET', path=f'/ts_cost_management/',
            single_page=single_page, page_size=page_size, warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_create(self, kwargs: dict = None, **payload
        ) -> list:
        """Create Cost Multi

        Args:
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **payload: additional parameters for the API.

        Keyword Args:
            uuid_metric (string required): additional filter - payload
            date (string required): additional filter - payload
            cloud_provider (string required): additional filter - payload
            resource_location (string required): additional filter - payload
            subscription_type (string optional): additional filter - payload
            subscription_id (string required): additional filter - payload
            subscription_name (string optional): additional filter - payload
            family (string required): additional filter - payload
            category (string required): additional filter - payload
            subcategory (string required): additional filter - payload
            object (string required): additional filter - payload
            metric (string required): additional filter - payload
            unit (string required): additional filter - payload
            qnt (number optional): additional filter - payload
            local_currency (string required): additional filter - payload
            unit_cost (number required): additional filter - payload
            total_cost (number required): additional filter - payload
            unit_revenue (number required): additional filter - payload
            total_revenue (number required): additional filter - payload
            provider_currency (string required): additional filter - payload
            unit_cost_pc (number required): additional filter - payload
            total_cost_pc (number required): additional filter - payload
            unit_revenue_pc (number required): additional filter - payload
            total_revenue_pc (number required): additional filter - payload
            cumulative_qnt (number required): additional filter - payload
            cumulative_unit_cost (number required): additional filter - payload
            cumulative_total_cost (number required): additional filter - payload
            cumulative_unit_revenue (number required): additional filter - payload
            cumulative_total_revenue (number required): additional filter - payload
            resource_group (string required): additional filter - payload
            reservation_name (string required): additional filter - payload
            publisher_name (string required): additional filter - payload
            tenant_id (string optional): additional filter - payload

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_payload_list = ['uuid_metric', 'date', 'cloud_provider',
            'resource_location', 'subscription_type', 'subscription_id',
            'subscription_name', 'family', 'category', 'subcategory',
            'object', 'metric', 'unit', 'qnt', 'local_currency',
            'unit_cost', 'total_cost', 'unit_revenue', 'total_revenue',
            'provider_currency', 'unit_cost_pc', 'total_cost_pc',
            'unit_revenue_pc', 'total_revenue_pc', 'cumulative_qnt',
            'cumulative_unit_cost', 'cumulative_total_cost',
            'cumulative_unit_revenue', 'cumulative_total_revenue',
            'resource_group', 'reservation_name', 'publisher_name', 'tenant_id'
            ]
        payload.get('uuid_metric'), payload.get('date'), payload.get(
            'cloud_provider'), payload.get('resource_location'), payload.get(
            'subscription_type'), payload.get('subscription_id'), payload.get(
            'subscription_name'), payload.get('family'), payload.get('category'
            ), payload.get('subcategory'), payload.get('object'), payload.get(
            'metric'), payload.get('unit'), payload.get('qnt'), payload.get(
            'local_currency'), payload.get('unit_cost'), payload.get(
            'total_cost'), payload.get('unit_revenue'), payload.get(
            'total_revenue'), payload.get('provider_currency'), payload.get(
            'unit_cost_pc'), payload.get('total_cost_pc'), payload.get(
            'unit_revenue_pc'), payload.get('total_revenue_pc'), payload.get(
            'cumulative_qnt'), payload.get('cumulative_unit_cost'
            ), payload.get('cumulative_total_cost'), payload.get(
            'cumulative_unit_revenue'), payload.get('cumulative_total_revenue'
            ), payload.get('resource_group'), payload.get('reservation_name'
            ), payload.get('publisher_name'), payload.get('tenant_id')
        warning_wrong_parameters(self.ts_cost_management_create.__name__,
            payload, official_payload_list)
        response = self.execute('POST', path=f'/ts_cost_management/',
            payload=payload, **kwargs)
        return response

    def ts_cost_management_grouped(self, uuid_customer: str,
        warm_start: bool = False, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None, **params) -> list:
        """Query Group By Date

        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            cloud_provider (string optional): additional filter - parameter
            resource_group (string optional): additional filter - parameter
            resource_location (string optional): additional filter - parameter
            category (string optional): additional filter - parameter
            subscription (string optional): additional filter - parameter
            subscription_type (string optional): additional filter - parameter
            interval (None optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['sort_by', 'date_start', 'date_end',
            'cloud_provider', 'resource_group', 'resource_location',
            'category', 'subscription', 'subscription_type', 'interval',
            'skip', 'limit', 'like', 'join', 'count']
        params.get('sort_by'), params.get('date_start'), params.get('date_end'
            ), params.get('cloud_provider'), params.get('resource_group'
            ), params.get('resource_location'), params.get('category'
            ), params.get('subscription'), params.get('subscription_type'
            ), params.get('interval'), params.get('skip'), params.get('limit'
            ), params.get('like'), params.get('join'), params.get('count')
        warning_wrong_parameters(self.ts_cost_management_grouped.__name__,
            params, official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/grouped/{uuid_customer}', single_page=
            single_page, page_size=page_size, warm_start=warm_start, params
            =params, **kwargs)
        return response

    def ts_cost_management_uuid_metric(self, uuid_metric: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Read Cost

        Args:
            uuid_metric (str, required): uuid_metric
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            date (string required): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['date']
        params.get('date')
        warning_wrong_parameters(self.ts_cost_management.__name__, params,
            official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/{uuid_metric}', warm_start=warm_start,
            params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_date(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Group By Cloud Provider Subscription Type Resource Group

        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            interval (None optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['count', 'date_start', 'date_end', 'interval']
        params.get('count'), params.get('date_start'), params.get('date_end'
            ), params.get('interval')
        warning_wrong_parameters(self.ts_cost_management_ccm_by_date.
            __name__, params, official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_date/{uuid_customer}', warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_subscription_type(self,
        uuid_customer: str, warm_start: bool = False, kwargs: dict = None,
        **params) -> list:
        """Query Group By Cloud Provider Subscription Type

        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['count', 'date_start', 'date_end']
        params.get('count'), params.get('date_start'), params.get('date_end')
        warning_wrong_parameters(self.
            ts_cost_management_ccm_by_subscription_type.__name__, params,
            official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_subscription_type/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_category(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Group By Category

        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['count', 'date_start', 'date_end']
        params.get('count'), params.get('date_start'), params.get('date_end')
        warning_wrong_parameters(self.ts_cost_management_ccm_by_category.
            __name__, params, official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_category/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_resource_location(self,
        uuid_customer: str, warm_start: bool = False, kwargs: dict = None,
        **params) -> list:
        """Query Group By Resource Location

        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['count', 'date_start', 'date_end']
        params.get('count'), params.get('date_start'), params.get('date_end')
        warning_wrong_parameters(self.
            ts_cost_management_ccm_by_resource_location.__name__, params,
            official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_resource_location/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_resource_group(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Group By Resource Group

        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['count', 'date_start', 'date_end']
        params.get('count'), params.get('date_start'), params.get('date_end')
        warning_wrong_parameters(self.
            ts_cost_management_ccm_by_resource_group.__name__, params,
            official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_resource_group/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_ccm_by_subscription(self, uuid_customer: str,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Group By Subscription

        Args:
            uuid_customer (str, required): uuid_customer
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['count', 'date_start', 'date_end']
        params.get('count'), params.get('date_start'), params.get('date_end')
        warning_wrong_parameters(self.
            ts_cost_management_ccm_by_subscription.__name__, params,
            official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/ccm_by_subscription/{uuid_customer}',
            warm_start=warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_anomalies(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Query Anomalies

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['date_start', 'date_end', 'skip', 'limit',
            'like', 'join', 'count']
        params.get('date_start'), params.get('date_end'), params.get('skip'
            ), params.get('limit'), params.get('like'), params.get('join'
            ), params.get('count')
        warning_wrong_parameters(self.ts_cost_management_anomalies.__name__,
            params, official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/anomalies/', single_page=single_page,
            page_size=page_size, warm_start=warm_start, params=params, **kwargs
            )
        return response

    def ts_cost_management_anomaly_selector(self, warm_start: bool = False,
        kwargs: dict = None, **params) -> list:
        """Query Anomaly Selector

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            sampling (None optional): additional filter - parameter
            uuid_customer (string required): additional filter - parameter
            cloud_provider (string required): additional filter - parameter
            description (string required): additional filter - parameter
            family (string required): additional filter - parameter
            category (string required): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['count', 'date_start', 'date_end',
            'sampling', 'uuid_customer', 'cloud_provider', 'description',
            'family', 'category']
        params.get('count'), params.get('date_start'), params.get('date_end'
            ), params.get('sampling'), params.get('uuid_customer'), params.get(
            'cloud_provider'), params.get('description'), params.get('family'
            ), params.get('category')
        warning_wrong_parameters(self.ts_cost_management_anomaly_selector.
            __name__, params, official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/anomaly_selector/', warm_start=warm_start,
            params=params, **kwargs)
        return response

    def ts_cost_management_anomaly_selector_geo(self,
        warm_start: bool = False, kwargs: dict = None, **params) -> list:
        """Query Anomaly Selector Geo

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            sampling (None optional): additional filter - parameter
            uuid_customer (string required): additional filter - parameter
            cloud_provider (string required): additional filter - parameter
            description (string required): additional filter - parameter
            resource_location (string required): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        kwargs, params = handling_single_page_methods(kwargs=kwargs, params
            =params)
        official_params_list = ['count', 'date_start', 'date_end',
            'sampling', 'uuid_customer', 'cloud_provider', 'description',
            'resource_location']
        params.get('count'), params.get('date_start'), params.get('date_end'
            ), params.get('sampling'), params.get('uuid_customer'), params.get(
            'cloud_provider'), params.get('description'), params.get(
            'resource_location')
        warning_wrong_parameters(self.
            ts_cost_management_anomaly_selector_geo.__name__, params,
            official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/anomaly_selector_geo/', warm_start=
            warm_start, params=params, **kwargs)
        return response

    def ts_cost_management_anomalies_geo(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Query Anomalies Geo

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            date_start (string optional): additional filter - parameter
            date_end (string optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['date_start', 'date_end', 'skip', 'limit',
            'like', 'join', 'count']
        params.get('date_start'), params.get('date_end'), params.get('skip'
            ), params.get('limit'), params.get('like'), params.get('join'
            ), params.get('count')
        warning_wrong_parameters(self.ts_cost_management_anomalies_geo.
            __name__, params, official_params_list)
        response = self.execute('GET', path=
            f'/ts_cost_management/anomalies_geo/', single_page=single_page,
            page_size=page_size, warm_start=warm_start, params=params, **kwargs
            )
        return response

    def ts_cost_management_probe_delete(self, uuid_probe: str,
        kwargs: dict = None, **params) -> list:
        """Delete By Uuid Probe And Date Range

        Args:
            uuid_probe (str, required): uuid_probe
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            tenant_id (string optional): additional filter - parameter
            date_start (string required): additional filter - parameter
            date_end (string required): additional filter - parameter
            profile (string optional): additional filter - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['tenant_id', 'date_start', 'date_end',
            'profile']
        params.get('tenant_id'), params.get('date_start'), params.get(
            'date_end'), params.get('profile')
        warning_wrong_parameters(self.ts_cost_management_probe_delete.
            __name__, params, official_params_list)
        response = self.execute('DELETE', path=
            f'/ts_cost_management/probe/{uuid_probe}/', params=params, **kwargs
            )
        return response
