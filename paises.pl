% ============================================================
%  BASE DE CONOCIMIENTO: PAISES Y CONTINENTES
%  Estructura inspirada en: huesos.pl
%  Autor: Generado como ejercicio de BDC en Prolog
% ============================================================

% ============================================================
% HECHOS
% ============================================================

% El mundo se divide en continentes con X paises reconocidos.
% mundo(Continente, NumeroDePaises).

mundo(africa, 54).
mundo(america, 35).
mundo(asia, 49).
mundo(europa, 44).
mundo(oceania, 14).
mundo(antartida, 0).

% ------------------------------------------------------------
% AFRICA - 54 paises (seleccion representativa)
% africa(Pais, NumeroDePaises).
% ------------------------------------------------------------
africa(nigeria, 1).
africa(etiopia, 1).
africa(egipto, 1).
africa(sudafrica, 1).
africa(kenia, 1).
africa(tanzania, 1).
africa(ghana, 1).
africa(angola, 1).
africa(mozambique, 1).
africa(madagascar, 1).
africa(camerun, 1).
africa(zimbabue, 1).
africa(mali, 1).
africa(niger, 1).
africa(senegal, 1).

% ------------------------------------------------------------
% AMERICA - 35 paises
% america(Pais, NumeroDePaises).
% ------------------------------------------------------------
america(mexico, 1).
america(estadosunidos, 1).
america(canada, 1).
america(brasil, 1).
america(argentina, 1).
america(colombia, 1).
america(chile, 1).
america(peru, 1).
america(venezuela, 1).
america(ecuador, 1).
america(bolivia, 1).
america(paraguay, 1).
america(uruguay, 1).
america(cuba, 1).
america(costarica, 1).
america(panama, 1).
america(guatemala, 1).
america(honduras, 1).
america(elsalvador, 1).
america(nicaragua, 1).
america(republicadominicana, 1).
america(haiti, 1).
america(jamaica, 1).
america(trinidadytobago, 1).
america(guyana, 1).
america(surinam, 1).
america(belice, 1).
america(bahamas, 1).
america(barbados, 1).
america(granada, 1).
america(sanlucía, 1).
america(sanvicente, 1).
america(dominica, 1).
america(antiguaybarbuda, 1).
america(sancristobalneves, 1).

% ------------------------------------------------------------
% ASIA - 49 paises (seleccion representativa)
% asia(Pais, NumeroDePaises).
% ------------------------------------------------------------
asia(china, 1).
asia(india, 1).
asia(japon, 1).
asia(coreadelsur, 1).
asia(indonesia, 1).
asia(pakistan, 1).
asia(bangladesh, 1).
asia(rusia, 1).
asia(turquia, 1).
asia(arabia_saudita, 1).
asia(iran, 1).
asia(irak, 1).
asia(tailandia, 1).
asia(vietnam, 1).
asia(filipinas, 1).
asia(malasia, 1).
asia(kazajistan, 1).
asia(uzbekistan, 1).
asia(afganistan, 1).
asia(israel, 1).

% ------------------------------------------------------------
% EUROPA - 44 paises (seleccion representativa)
% europa(Pais, NumeroDePaises).
% ------------------------------------------------------------
europa(alemania, 1).
europa(francia, 1).
europa(italia, 1).
europa(espana, 1).
europa(reinounido, 1).
europa(portugal, 1).
europa(paises_bajos, 1).
europa(belgica, 1).
europa(suiza, 1).
europa(austria, 1).
europa(suecia, 1).
europa(noruega, 1).
europa(dinamarca, 1).
europa(finlandia, 1).
europa(polonia, 1).
europa(chequia, 1).
europa(eslovaquia, 1).
europa(hungria, 1).
europa(rumania, 1).
europa(grecia, 1).

% ------------------------------------------------------------
% OCEANIA - 14 paises
% oceania(Pais, NumeroDePaises).
% ------------------------------------------------------------
oceania(australia, 1).
oceania(nuevazelanda, 1).
oceania(papua_nuevaguinea, 1).
oceania(fiyi, 1).
oceania(salomon, 1).
oceania(vanuatu, 1).
oceania(samoa, 1).
oceania(kiribati, 1).
oceania(tonga, 1).
oceania(micronesia, 1).
oceania(palau, 1).
oceania(marshalls, 1).
oceania(nauru, 1).
oceania(tuvalu, 1).

% ============================================================
% HECHOS ADICIONALES: Capital de cada pais
% capital(Pais, Capital).
% ============================================================
capital(mexico, ciudad_de_mexico).
capital(estadosunidos, washington).
capital(canada, ottawa).
capital(brasil, brasilia).
capital(argentina, buenos_aires).
capital(colombia, bogota).
capital(chile, santiago).
capital(peru, lima).
capital(china, beijing).
capital(india, nueva_delhi).
capital(japon, tokio).
capital(alemania, berlin).
capital(francia, paris).
capital(italia, roma).
capital(espana, madrid).
capital(reinounido, londres).
capital(nigeria, abuja).
capital(egipto, el_cairo).
capital(sudafrica, pretoria).
capital(australia, canberra).
capital(nuevazelanda, wellington).

% ============================================================
% REGLAS
% ============================================================

% Verifica si un pais pertenece al mundo (a algun continente).
es_pais(Pais) :-
    africa(Pais, _) ; america(Pais, _) ;
    asia(Pais, _) ; europa(Pais, _) ;
    oceania(Pais, _).

% Verifica si una entidad es un continente reconocido.
es_continente(Continente) :- mundo(Continente, _).

% Reglas por continente: verifica si un pais pertenece a un continente especifico.
es_africano(Pais)   :- africa(Pais, _).
es_americano(Pais)  :- america(Pais, _).
es_asiatico(Pais)   :- asia(Pais, _).
es_europeo(Pais)    :- europa(Pais, _).
es_oceanico(Pais)   :- oceania(Pais, _).

% Obtiene el continente al que pertenece un pais.
continente_de(Pais, africa)   :- africa(Pais, _).
continente_de(Pais, america)  :- america(Pais, _).
continente_de(Pais, asia)     :- asia(Pais, _).
continente_de(Pais, europa)   :- europa(Pais, _).
continente_de(Pais, oceania)  :- oceania(Pais, _).

% Verifica si dos paises son del mismo continente.
mismo_continente(Pais1, Pais2) :-
    continente_de(Pais1, C),
    continente_de(Pais2, C),
    Pais1 \= Pais2.

% Obtiene la capital de un pais (si esta registrada).
tiene_capital(Pais, Capital) :- capital(Pais, Capital).

% Cuenta cuantos paises tiene registrados un continente en la BDC.
% (Para usar con aggregate_all si el interprete lo soporta, o con findall)
% Ejemplo de uso: findall(P, africa(P,_), L), length(L, N).

% ============================================================
% FIN DEL ARCHIVO
% ============================================================