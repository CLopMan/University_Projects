insert into Interprete (select distinct band, band_nation, band_language from fsdb.artists where band is not NULL); 
--Insercion de los grupos en Interprete

insert into Musico(select distinct passport, musician, nationality, birthdate from fsdb.artists where passport is not NULL and musician is not NULL and nationality is not NULL and birthdate is not NULL); 
-- Insercion de los musicos (se puede porque interprete ya esta creado)

insert into Pertenece(select distinct passport, band, role, to_date(start_date), to_date(end_date) from fsdb.artists where role is not NULL and band is not NULL and start_date is not NULL and to_date(start_date) < to_date(end_date));

insert into Manager (select to_number(man_mobile), manager_name, man_fam_name, man_surname from fsdb.recordings union select distinct to_number(man_mobile), manager_name, man_fam_name, man_surname from fsdb.livesingings where man_mobile is not NULL);
-- insercion de los grupos en manager. Se ignoran los datos de managers que no estén completos 

insert into Estudio (select distinct studio, stud_address from fsdb.recordings where studio is not NULL and stud_address is not NULL); 
-- insert estudio 

insert into Discografica (select distinct publisher, to_number(pub_phone) from fsdb.recordings where publisher is not NULL);

insert into Asistente (select distinct e_mail, dni,name, surn1, surn2, to_date(birthdate, 'DD-MM-YYYY'), to_number(phone), address from fsdb.melomaniacs where e_mail is not NULL); 
-- insercion de asistente

insert into Gira (select distinct performer, tour, man_mobile from fsdb.livesingings where performer is not NULL and tour is not NULL and man_mobile is not NULL); 
-- Insercion de gira 

insert into Concierto (select distinct performer, when, municipality, country, performer, tour, to_number(man_mobile), duration_min, address, attendance from fsdb.livesingings where performer is not NULL and when is not NULL and municipality is not NULL and country is not NULL and address is not NULL and to_number(man_mobile) is not NULL);

insert into Tema (select distinct song, writer, cowriter from fsdb.recordings union select distinct song, writer, cowriter from fsdb.livesingings where song is not NULL);

insert into Interpreta (select distinct song, writer, performer, when, duration_sec, seqnumber from fsdb.livesingings where seqnumber is not NULL and song is not NULL and writer is not NULL and performer is not NULL and when is not NULL);

insert into Album (select distinct album_pair, release_date, format, publisher, performer, album_title, album_length, to_number(man_mobile) from fsdb.recordings where album_pair is not NULL and release_date is not NULL and format is not NULL and publisher is not NULL and performer is not NULL and album_title is not NULL and album_length is not NULL);

insert into Pista (select distinct album_pair, tracknum, song, writer, rec_date, studio, engineer, duration from fsdb.recordings where album_pair is not NULL and tracknum is not NULL and song is not NULL and writer is not NULL and rec_date is not NULL and studio is not NULL and engineer is not NULL and duration is not NULL and song != 'Die and thyme');

insert into Ficha (select distinct rfid, E_MAIL, performer, when, purchase, birthdate from fsdb.melomaniacs where rfid is not NULL and E_MAIL is not NULL and performer is not NULL and when is not NULL and purchase is not NULL and birthdate is not NULL and performer != 'Cunegunda ' and performer != 'CUNEGUNDA' and performer != 'Cunegunda Ibarra');

COMMIT;





