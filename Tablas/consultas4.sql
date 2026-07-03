-- ==========================================================
-- CONSULTA 1
-- Pregunta:
-- ¿Qué aerolíneas obtuvieron el mayor ingreso por la venta
-- de boletos en vuelos programados dentro de un período de
-- tiempo determinado?
--
-- Objetivo:
-- Mostrar el número de boletos vendidos, el precio promedio
-- y el ingreso total generado por cada aerolínea para los
-- vuelos programados comprendidos entre dos fechas.
--
-- Índice recomendado:
-- CREATE INDEX idx_vuelo_estado_fecha
-- ON Vuelo(estado, fecha);
-- ==========================================================

SELECT
    ae.nombre AS aerolinea,
    ae.pais_origen AS pais,
    COUNT(b.id_boleto) AS boletos_vendidos,
    ROUND(AVG(b.precio),2) AS precio_promedio,
    ROUND(SUM(b.precio),2) AS total_recaudado

FROM Aerolinea ae

JOIN Vuelo v
ON v.codigo_icao = ae.codigo_icao

JOIN Boleto b
ON b.codigo_vuelo = v.codigo_vuelo

WHERE
    v.estado = 'Programado'
AND
    v.fecha BETWEEN '2024-04-01'
               AND '2024-08-31'

GROUP BY
    ae.codigo_icao,
    ae.nombre,
    ae.pais_origen

ORDER BY
    total_recaudado DESC;



-- ==========================================================
-- CONSULTA 2
-- Pregunta:
-- ¿Cuántas reservas ha realizado un pasajero específico y
-- cuál fue la fecha de su última reserva?
--
-- Objetivo:
-- Obtener el historial resumido de reservas de un pasajero
-- identificado mediante su DNI.
-- ==========================================================

SELECT
    p.nombre,
    p.apellido,
    p.nacionalidad,
    COUNT(r.id_reserva) AS total_reservas,
    MAX(r.fecha) AS ultima_reserva

FROM Pasajero p

JOIN Reserva r
ON r.dni_pasajero=p.dni_pasajero

WHERE
p.dni_pasajero='70543210'

GROUP BY
p.dni_pasajero,
p.nombre,
p.apellido,
p.nacionalidad;



-- ==========================================================
-- CONSULTA 3
-- Pregunta:
-- ¿Cuál es el estado operativo de los vuelos programados
-- dentro de un período determinado, indicando la aerolínea,
-- el avión asignado, la puerta de embarque y la cantidad de
-- pasajeros registrados?
--
-- Objetivo:
-- Generar un panel operativo resumido para supervisar los
-- vuelos programados durante un intervalo de fechas.
-- ==========================================================

SELECT
    v.codigo_vuelo,
    v.origen,
    v.destino,
    v.hora_salida,
    ae.nombre AS aerolinea,
    av.matricula,
    ap.numero_puerta,
    COUNT(b.id_boleto) AS pasajeros

FROM Vuelo v

JOIN Realiza r
ON r.codigo_vuelo = v.codigo_vuelo

JOIN Avion av
ON av.matricula = r.matricula

JOIN Aerolinea ae
ON ae.codigo_icao = av.codigo_icao

LEFT JOIN Asignado_puerta ap
ON ap.codigo_vuelo = v.codigo_vuelo

LEFT JOIN Boleto b
ON b.codigo_vuelo = v.codigo_vuelo

WHERE
v.estado='Programado'
AND
v.hora_salida BETWEEN
'2024-04-01'
AND
'2024-08-31'

GROUP BY
v.codigo_vuelo,
v.origen,
v.destino,
v.hora_salida,
ae.nombre,
av.matricula,
ap.numero_puerta

ORDER BY
v.hora_salida;


-- ==========================================================
-- CONSULTA 4
-- Pregunta:
-- ¿Cuántas reservas ha realizado un pasajero específico?
--
-- Objetivo:
-- Obtener la información del pasajero junto con el número de
-- reservas registradas en el sistema.
--
-- Índice recomendado:
-- CREATE INDEX idx_hash_dni
-- ON Pasajero USING HASH(dni_pasajero);
-- ==========================================================

SELECT
    p.dni_pasajero,
    p.nombre,
    p.apellido,
    p.nacionalidad,
    COUNT(r.id_reserva) AS total_reservas

FROM Pasajero p

JOIN Reserva r
ON r.dni_pasajero = p.dni_pasajero

WHERE
p.dni_pasajero = '70543210'

GROUP BY
p.dni_pasajero,
p.nombre,
p.apellido,
p.nacionalidad;