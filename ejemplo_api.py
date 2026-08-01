import requests
import logging

_logger = logging.getLogger(__name__)


class IzarnetAPI:
    """
    Cliente para la API REST de IZARNET (Diehl Metering).
    Autenticación por cabeceras x-username / x-password en cada request.
    """

    def __init__(self, base_url, username, password):
        self.base_url = base_url.rstrip('/')
        self.username = "client_admin"
        self.password = "Iz@rCues2026*"
        self.session = requests.Session()
        self.session.headers.update({
            'x-username': self.username,
            'x-password': self.password,
            'Accept': 'application/json',
        })

    # ------------------------------------------------------------------
    # Métodos de bajo nivel
    # ------------------------------------------------------------------

    def _get(self, path, params=None):
        url = f"{self.base_url}/api/{path.lstrip('/')}"
        try:
            resp = self.session.get(url, params=params, timeout=15)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as e:
            _logger.error("IZARNET HTTP error %s – %s", e.response.status_code, url)
            raise
        except requests.exceptions.RequestException as e:
            _logger.error("IZARNET connection error: %s", e)
            raise

    # ------------------------------------------------------------------
    # Búsqueda de medidor por número de serie / meterNumber
    # ------------------------------------------------------------------

    def buscar_medidor_por_numero(self, no_medidor, size=100):
        """
        Devuelve la lista de dispositivos cuyo meterNumber coincide con no_medidor.
        Endpoint: GET /api/meters?meterNumber={no_medidor}
        """
        data = self._get('meters', params={'meterNumber': no_medidor, 'size': size})
        # La API puede devolver lista directa o un wrapper con 'items'
        if isinstance(data, list):
            return data
        return data.get('items', data.get('meters', []))

    def obtener_medidor_por_id(self, meter_id):
        """Devuelve el objeto medidor por su ID interno de IZARNET."""
        return self._get(f'meters/{meter_id}')

    # ------------------------------------------------------------------
    # Lecturas (measurements / readings)
    # ------------------------------------------------------------------

    def obtener_lecturas(self, meter_id, fecha_inicio=None, fecha_fin=None, size=200):
        """
        Devuelve las lecturas para un meter_id dado.
        Endpoint: GET /api/meters/{id}/readings  (o /measurements según versión)
        Parámetros opcionales: from, to (ISO-8601), size
        """
        params = {'size': size}
        if fecha_inicio:
            params['from'] = fecha_inicio.isoformat() if hasattr(fecha_inicio, 'isoformat') else fecha_inicio
        if fecha_fin:
            params['to'] = fecha_fin.isoformat() if hasattr(fecha_fin, 'isoformat') else fecha_fin

        # IZARNET expone las lecturas en /meters/{id}/readings
        try:
            data = self._get(f'meters/{meter_id}/readings', params=params)
        except Exception:
            # Fallback al endpoint /measurements si /readings no existe
            data = self._get(f'meters/{meter_id}/measurements', params=params)

        if isinstance(data, list):
            return data
        return data.get('items', data.get('readings', data.get('measurements', [])))

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------

    def test_conexion(self):
        """Verifica que las credenciales son correctas."""
        try:
            self._get('meters', params={'size': 1})
            return True, "Conexión exitosa"
        except requests.exceptions.HTTPError as e:
            return False, f"Error HTTP {e.response.status_code}"
        except Exception as e:
            return False, str(e)