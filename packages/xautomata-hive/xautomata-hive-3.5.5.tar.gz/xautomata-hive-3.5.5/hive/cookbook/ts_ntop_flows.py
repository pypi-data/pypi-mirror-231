from hive.api import ApiManager, handling_single_page_methods, warning_wrong_parameters


class TsNtopFlows(ApiManager):
    """Class that handles all the XAutomata ts_ntop_flows APIs"""

    def ts_ntop_flows(self, warm_start: bool = False,
        single_page: bool = False, page_size: int = 5000,
        kwargs: dict = None, **params) -> list:
        """Read Data

        Args:
            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False.
            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False.
            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000.
            kwargs (dict, optional): additional parameters for execute. Default to None.
            **params: additional parameters for the API.

        Keyword Args:
            sort_by (string optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "". - parameter
            null_fields (string optional): additional filter - parameter
            uuid_service (string optional): additional filter - parameter
            l7_proto (integer optional): additional filter - parameter
            ip_src_addr (None optional): additional filter - parameter
            ip_dst_addr (None optional): additional filter - parameter
            l4_dst_port (integer optional): additional filter - parameter
            in_bytes (integer optional): additional filter - parameter
            out_bytes (integer optional): additional filter - parameter
            last_switched_start (string optional): additional filter - parameter
            last_switched_end (string optional): additional filter - parameter
            interface_id (integer optional): additional filter - parameter
            skip (integer optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0. - parameter
            limit (integer optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000. - parameter
            like (boolean optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True. - parameter
            join (boolean optional): Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False - parameter
            count (boolean optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False. - parameter

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        official_params_list = ['sort_by', 'null_fields', 'uuid_service',
            'l7_proto', 'ip_src_addr', 'ip_dst_addr', 'l4_dst_port',
            'in_bytes', 'out_bytes', 'last_switched_start',
            'last_switched_end', 'interface_id', 'skip', 'limit', 'like',
            'join', 'count']
        params.get('sort_by'), params.get('null_fields'), params.get(
            'uuid_service'), params.get('l7_proto'), params.get('ip_src_addr'
            ), params.get('ip_dst_addr'), params.get('l4_dst_port'
            ), params.get('in_bytes'), params.get('out_bytes'), params.get(
            'last_switched_start'), params.get('last_switched_end'
            ), params.get('interface_id'), params.get('skip'), params.get(
            'limit'), params.get('like'), params.get('join'), params.get(
            'count')
        warning_wrong_parameters(self.ts_ntop_flows.__name__, params,
            official_params_list)
        response = self.execute('GET', path=f'/ts_ntop_flows/', single_page
            =single_page, page_size=page_size, warm_start=warm_start,
            params=params, **kwargs)
        return response

    def ts_ntop_flows_create(self, payload: list, single_page: bool = False,
        page_size: int = 5000, kwargs: dict = None) -> list:
        """Create Ts Ntop Flow

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
            "uuid_service": "string", optional
            "l7_proto": "string", optional
            "ip_src_addr": "integer string string", optional
            "ip_dst_addr": "integer string string", optional
            "l4_dst_port": "integer", optional
            "in_bytes": "integer", optional
            "out_bytes": "integer", optional
            "last_switched": "string", optional
            "interface_id": "integer", optional
           }
          ]

        Returns: list"""
        if kwargs is None:
            kwargs = dict()
        response = self.execute('POST', path=f'/ts_ntop_flows/',
            single_page=single_page, page_size=page_size, payload=payload,
            **kwargs)
        return response
