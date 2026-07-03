SELECT
(
    -- Avion -> Aerolinea
    (SELECT COUNT(*)
     FROM Avion a
     LEFT JOIN Aerolinea al
     ON a.codigo_icao = al.codigo_icao
     WHERE al.codigo_icao IS NULL)

    +

    -- Vuelo -> Aerolinea
    (SELECT COUNT(*)
     FROM Vuelo v
     LEFT JOIN Aerolinea al
     ON v.codigo_icao = al.codigo_icao
     WHERE al.codigo_icao IS NULL)

    +

    -- Puerta -> Area_embarque
    (SELECT COUNT(*)
     FROM Puerta_embarque p
     LEFT JOIN Area_embarque ae
     ON p.id_area = ae.id_area
     WHERE ae.id_area IS NULL)

    +

    -- Reserva -> Pasajero
    (SELECT COUNT(*)
     FROM Reserva r
     LEFT JOIN Pasajero p
     ON r.dni_pasajero = p.dni_pasajero
     WHERE p.dni_pasajero IS NULL)

    +

    -- Boleto -> Vuelo
    (SELECT COUNT(*)
     FROM Boleto b
     LEFT JOIN Vuelo v
     ON b.codigo_vuelo = v.codigo_vuelo
     WHERE v.codigo_vuelo IS NULL)

    +

    -- Equipaje -> Boleto
    (SELECT COUNT(*)
     FROM Equipaje e
     LEFT JOIN Boleto b
     ON e.id_boleto = b.id_boleto
     WHERE b.id_boleto IS NULL)

    +

    -- Equipaje -> Area_equipaje
    (SELECT COUNT(*)
     FROM Equipaje e
     LEFT JOIN Area_equipaje ae
     ON e.id_area = ae.id_area
     WHERE ae.id_area IS NULL)

    +

    -- Asignado_empleado -> Area
    (SELECT COUNT(*)
     FROM Asignado_empleado a
     LEFT JOIN Area ar
     ON a.id_area = ar.id_area
     WHERE ar.id_area IS NULL)

    +

    -- Asignado_empleado -> Empleado
    (SELECT COUNT(*)
     FROM Asignado_empleado a
     LEFT JOIN Empleado e
     ON a.dni_empleado = e.dni_empleado
     WHERE e.dni_empleado IS NULL)

    +

    -- Asignado_puerta -> Vuelo
    (SELECT COUNT(*)
     FROM Asignado_puerta a
     LEFT JOIN Vuelo v
     ON a.codigo_vuelo = v.codigo_vuelo
     WHERE v.codigo_vuelo IS NULL)

    +

    -- Asignado_puerta -> Puerta
    (SELECT COUNT(*)
     FROM Asignado_puerta a
     LEFT JOIN Puerta_embarque p
     ON a.numero_puerta = p.numero_puerta
     WHERE p.numero_puerta IS NULL)

    +

    -- Usa_pista -> Vuelo
    (SELECT COUNT(*)
     FROM Usa_pista u
     LEFT JOIN Vuelo v
     ON u.codigo_vuelo = v.codigo_vuelo
     WHERE v.codigo_vuelo IS NULL)

    +

    -- Usa_pista -> Pista
    (SELECT COUNT(*)
     FROM Usa_pista u
     LEFT JOIN Pista p
     ON u.numero_pista = p.numero_pista
     WHERE p.numero_pista IS NULL)

    +

    -- Realiza -> Vuelo
    (SELECT COUNT(*)
     FROM Realiza r
     LEFT JOIN Vuelo v
     ON r.codigo_vuelo = v.codigo_vuelo
     WHERE v.codigo_vuelo IS NULL)

    +

    -- Realiza -> Avion
    (SELECT COUNT(*)
     FROM Realiza r
     LEFT JOIN Avion a
     ON r.matricula = a.matricula
     WHERE a.matricula IS NULL)

) AS registros_huerfanos;